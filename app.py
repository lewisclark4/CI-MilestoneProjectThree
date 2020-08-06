# Import modules
import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, session, redirect, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

# Import Git ignored file contatining sensitive data
if path.exists("env.py"):
    import env

# Create app instance
app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] =  os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] =  os.environ.get('MONGO_DBNAME')
# mongoDB config
app.config["MONGO_URI"] =  os.environ.get('MONGO_URI')


# Constant Variables
mongo = PyMongo(app)
users = mongo.db.users
recipe = mongo.db.recipes
cuisine = mongo.db.cuisines
difficulty = mongo.db.difficulty
allergens = mongo.db.allergens

# Index - Displays Public recipes#
@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html",
                            recipes=recipe.find())

# Register - Allows user creation
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
                return render_template('index.html',
                                        recipes=recipe.find())
            else:
                flash('Passwords do not match, please try again.', 'error')
        else:
            flash('This username already exists. Please try again with another username.', 'error')
    return render_template('register.html')

# Login - User can log into session
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_exists = users.find_one({'username': request.form['username'].lower()})
        if user_exists:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                user_exists['password']) == user_exists['password']:
                session["username"] = request.form["username"].lower()
                flash('Login successful', 'success')
                return render_template("index.html",
                                        recipes=recipe.find())
            else:
                flash('Invalid username/password combination',  'error')
        else:
            flash('Invalid username/password combination',  'error')
    
    return render_template("login.html")
    

# Logout - User can log out of session
@app.route('/logout')
def logout():
    session.clear()
    flash('Log out successful. We hope you found something tasty.', 'success')
    return render_template("login.html")

# My Recipes - View all recipes that a user has added themselves (public or private)
@app.route('/my_recipes')
def my_recipes():
    return render_template("myrecipes.html",
                            recipes=recipe.find())

# Add Recipe - Allows user to enter their own recipes
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
                           recipes=recipe.find(),
                           cuisines=cuisine.find(),
                           difficulty=difficulty.find(),
                           allergens=allergens.find())

# Insert Recipe - Submits a recipe to MongoDB 
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    data = {    'created_by': session['username'],
                'soft_delete': False,
                'recipe_name': request.form.get('recipe_name'),
                'image': request.form.get('image'),
                'cuisine': ObjectId(request.form.get('cuisine')),
                'difficulty': ObjectId(request.form.get('difficulty')),
                'prep_time': request.form.get('prep_time'),
                'cook_time': request.form.get('cook_time'),
                'serves': request.form.get('serves'),
                'allergens': request.form.getlist('allergens'),
                'ingredients': request.form.getlist('ingredients'),
                'preparation': request.form.getlist('preparation'),
            }
    if request.form.getlist('public'):
        data.update({'public': True}) 
    else:
        data.update({'public': False}) 
    recipe.insert_one(data)
    
    return redirect(url_for('add_recipe'))

# View Recipe - Allows a user to view details of a recipe 
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    my_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})
    cuisine_type = cuisine.find_one({"_id": ObjectId(my_recipe["cuisine"])})
    skill_level = difficulty.find_one({"_id": ObjectId(my_recipe["difficulty"])})
    return render_template('viewrecipe.html',
                           recipe = my_recipe,
                           cuisines=cuisine_type,
                           difficulty=skill_level)

# Edit Recipe - Allows a user to edit their own recipes
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    my_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("editrecipe.html",
                           recipe=my_recipe,
                           cuisines=cuisine.find(),
                           difficulty=difficulty.find(),
                           allergens=allergens.find())

# Update Recipe - Submits an edited recipe to MongoDB 
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    data = {    'created_by': session['username'],
                'soft_delete': False,
                'recipe_name': request.form.get('recipe_name'),
                'image': request.form.get('image'),
                'cuisine': ObjectId(request.form.get('cuisine')),
                'difficulty': ObjectId(request.form.get('difficulty')),
                'prep_time': request.form.get('prep_time'),
                'cook_time': request.form.get('cook_time'),
                'serves': request.form.get('serves'),
                'allergens': request.form.getlist('allergens'),
                'ingredients': request.form.getlist('ingredients'),
                'preparation': request.form.getlist('preparation[]'),
            }
    if request.form.getlist('public'):
        data.update({'public': True}) 
    else:
        data.update({'public': False}) 
    recipe.update({"_id": ObjectId(recipe_id)}, data)
           
    return redirect(url_for('view_recipe', recipe_id=recipe_id))

# Delete Recipe - 'soft deletes' a recipe record
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe.update({"_id": ObjectId(recipe_id)}, {"$set": {"soft_delete": True}})
    return render_template("myrecipes.html",
                            recipes=recipe.find())

# Search - Allows a user to search for recipes and have results displayed.
@app.route('/search/', methods=['POST'])
def search():
    search_results = recipe.find({'$text': {'$search': request.form['search']}})
    count =  recipe.count_documents({'$text': {'$search': request.form['search']}})
    return render_template('index.html', 
                            recipes=search_results,
                            count=count,
                            search=True)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
