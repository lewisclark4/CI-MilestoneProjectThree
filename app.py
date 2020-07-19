import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, session, redirect, flash
from flask_pymongo import PyMongo
import bcrypt

if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://lcadmin:Password1@myfirstcluster-y3iip.mongodb.net/foodology?retryWrites=true&w=majority"
app.config["MONGO_DBNAME"] = "foodology"
app.config["SECRET_KEY"] = "MYSUPERSECRETKEY123"

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


## https://www.youtube.com/watch?v=vVx1737auSE
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['username'] = request.form['username']
        users = mongo.db.users
        user_exists = users.find_one(
                      {'username': request.form['username']})

        if user_exists is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),
                                     bcrypt.gensalt())
            users.insert({'username': request.form['username'].lower(),
                         'password': hashpass})
            session['username'] = request.form['username'].lower()
            return redirect(url_for('index'))

        session.pop('username', None)
        return render_template('register.html')

    return render_template('register.html')


@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)