import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, session, redirect, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['SECRET_KEY'] =  os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] =  os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] =  os.environ.get('MONGO_URI')

mongo = PyMongo(app)
users = mongo.db.users
recipe = mongo.db.recipes

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_exists = users.find_one({'username': request.form['username'].lower()})
        if not user_exists:
            if request.form['password'] == request.form['passwordcheck']:
                hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),
                                         bcrypt.gensalt())
                users.insert({'username': request.form['username'].lower(),
                              'password': hashpass})
                session['username'] = request.form['username'].lower()
                flash('Account Created. You are now logged in' , 'success')
                return render_template('index.html')
            else:
                flash('Passwords do not match, please try again.', 'error')
        else:
            flash('This username already exists. Please try again with another username.', 'error')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_exists = users.find_one({'username': request.form['username'].lower()})
        if user_exists:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                user_exists['password']) == user_exists['password']:
                session["username"] = request.form["username"].lower()
                flash('Login successful', 'success')
                return render_template("index.html")
            else:
                flash('Invalid username/password combination',  'error')
        else:
            flash('Invalid username/password combination',  'error')
    
    return render_template("login.html")
    


@app.route('/logout')
def logout():
    session.clear()
    flash('Log out successful. We hope you found something tasty.', 'success')
    return render_template("login.html")

@app.route('/recipes')
def recipes():
    return render_template("recipes.html",
                            recipes=mongo.db.recipes.find())

@app.route('/my_recipes')
def my_recipes():
    return render_template("myrecipes.html",
                            recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find(),
                           cuisines=mongo.db.cuisines.find(),
                           difficulty=mongo.db.difficulty.find(),
                           allergens=mongo.db.allergens.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    data = request.form.to_dict()
    data.update({'created_by': session['username']})
    data.update({'soft_delete': False})
    data.update({'ingredients': request.form.getlist('ingredients')})
    data.update({'preparation': request.form.getlist('preparation')})
    data.update({'allergens': request.form.getlist('allergens')})
    if request.form.getlist('public'):
        data.update({'public': True}) 
    else:
        data.update({'public': False}) 
    recipe.insert_one(data)
    
    return redirect(url_for('add_recipe'))

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    my_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('viewrecipe.html',
                           recipe = my_recipe)

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    my_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("editrecipe.html",
                           recipe=my_recipe,
                           categories=mongo.db.categories.find(),
                           cuisines=mongo.db.cuisines.find(),
                           difficulty=mongo.db.difficulty.find(),
                           allergens=mongo.db.allergens.find())

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    data = {    'created_by': session['username'],
                'soft_delete': False,
                'recipe_name': request.form.get('recipe_name'),
                'image': request.form.get('image'),
                'cuisine': request.form.get('cuisine'),
                'difficulty': request.form.get('difficulty'),
                'prep_time': request.form.get('prep_time'),
                'cook_time': request.form.get('cook_time'),
                'serves': request.form.get('serves'),
                'allergens': request.form.getlist('allergens'),
                'ingredients': request.form.getlist('ingredients[]'),
                'preparation': request.form.getlist('preparation[]'),
                'public':request.form.get('public')
            }
    if request.form.getlist('public'):
        data.update({'public': True}) 
    else:
        data.update({'public': False}) 
    recipe.update({"_id": ObjectId(recipe_id)}, data)
           
    return redirect(url_for('view_recipe', recipe_id=recipe_id))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, {"$set": {"soft_delete": True}})
    return render_template("myrecipes.html",
                            recipes=mongo.db.recipes.find())

@app.route('/search/', methods=['POST'])
def search():
    search_text = request.form['search']
    return redirect(url_for('search_results', search_text=search_text))

@app.route('/search_results/<search_text>')
def search_results(search_text):
    search_results = mongo.db.recipes.find({'$text': {'$search': search_text}})
    return render_template('recipes.html', recipes=search_results)
                               

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
