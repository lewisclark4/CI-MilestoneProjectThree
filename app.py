import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, session, redirect, flash
from flask_pymongo import PyMongo
import bcrypt

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['SECRET_KEY'] =  os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] =  os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] =  os.environ.get('MONGO_URI')

mongo = PyMongo(app)
users = mongo.db.users


@app.route('/home')
def index():
    return render_template("index.html")


# https://www.youtube.com/watch?v=vVx1737auSE
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
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
