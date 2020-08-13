# Import modules


import os
import bcrypt
import math
from os import path
from flask import (
  Flask, render_template, redirect, request, url_for, session, redirect, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


# Import Git ignored file contatining sensitive data


if path.exists("env.py"):
    import env


# Create app instance


app = Flask(__name__)


# mongoDB config


app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


# Constant Variables


mongo = PyMongo(app)
users = mongo.db.users
recipe = mongo.db.recipes
cuisine = mongo.db.cuisines
difficulty = mongo.db.difficulty
allergens = mongo.db.allergens


# Pagination variable


limit = 8


# Index - Displays Public recipes
# Includes pagination logic


@app.route("/")
@app.route("/home")
def index():
    # find all recipes
    recipes = recipe.find()
    # count all recipes
    count = recipe.count_documents({})
    # Find the requested page number (or default to page 1)
    page_number = int(request.args.get('page_number', 1))
    # identify how many recipe records to be skipped based on page number
    skip = (page_number - 1) * limit
    # skip relevant number of recipes
    recipes.skip(skip).limit(limit)
    # identify how many pages of results are needed
    pages = int(math.ceil(count / limit))
    # create a page range
    total_pages = range(1, pages + 1)
    # render the results
    return render_template("index.html",
                           recipes=recipes,
                           page_number=page_number,
                           pages=total_pages,
                           count=count)


# Register - Allows user creation


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Search the database for the requted username
        user_exists = users.find_one(
            {"username": request.form["username"].lower()})
        if not user_exists:
            # If a new username, confirm the user has retyped the password correctly
            if request.form["password"] == request.form["passwordcheck"]:
                #hash the password to improve data security
                hashpass = bcrypt.hashpw(
                    request.form["password"].encode("utf-8"), bcrypt.gensalt())
                #Create a record of the username and hashed password in the database.
                users.insert({"username": request.form["username"].lower(),
                              "password": hashpass})
                # Create a new session for the username
                session["username"] = request.form["username"].lower()
                return redirect(url_for("index"))
            # Display a message to the user that the password entered do not match
            else:
                flash("Passwords do not match, please try again.", "error")
        # Display a message to the user that the username already exists
        else:
            flash("This username already exists. "
                  "Please try again with another username.", "error")
    return render_template("register.html")


# Login - User can log into session


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Search the database for the requted username
        user_exists = users.find_one(
            {"username": request.form["username"].lower()})
        if user_exists:
            # If the user exists, hash pw the user has entered and compare hashed pw in the database
            if bcrypt.hashpw(
                    request.form["password"].encode("utf-8"),
                    user_exists["password"]) == user_exists["password"]:
                    # if the passwords match, create a session for the user
                    session["username"] = request.form["username"].lower()
                    return redirect(url_for("index"))
            # Display a generic message that the login credentials are incorrect.
            else:
                flash("Invalid username/password combination",  "error")
        # Display a generic message that the login credentials are incorrect.
        else:
            flash("Invalid username/password combination",  "error")
    return render_template("login.html")


# Logout - User can log out of session


@app.route("/logout")
def logout():
    # If a user selects to log out, then clear the session
    session.clear()
    # Display a confirmation message to the user.
    flash("Log out successful. We hope you found something tasty.", "success")
    return redirect(url_for("login"))


# My Recipes
# View all recipes that a user has added themselves (public or private)


@app.route("/my_recipes")
def my_recipes():
    return render_template("myrecipes.html",
                           recipes=recipe.find())


# Add Recipe - Allows user to enter their own recipes


@app.route("/add_recipe")
def add_recipe():
    return render_template("addrecipe.html",
                           recipes=recipe.find(),
                           cuisines=cuisine.find(),
                           difficulty=difficulty.find(),
                           allergens=allergens.find())


# Insert Recipe - Submits a recipe to MongoDB


@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    # Take the data input by the user in the form
    data = {"created_by": session["username"],
            "soft_delete": False,
            "recipe_name": request.form.get("recipe_name"),
            "image": request.form.get("image"),
            "cuisine": ObjectId(request.form.get("cuisine")),
            "difficulty": ObjectId(request.form.get("difficulty")),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "allergens": request.form.getlist("allergens"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation": request.form.getlist("preparation"),
            }
    if request.form.getlist("public"):
        data.update({"public": True})
    else:
        data.update({"public": False})
    # Insert the data into the database
    recipe.insert_one(data)
    # find the object ID of the recipe created
    new_recipe = recipe.find_one({"recipe_name": data["recipe_name"]})["_id"]
    # pass the object ID into the view_recipe route
    return redirect(url_for("view_recipe", recipe_id=new_recipe))


# View Recipe - Allows a user to view details of a recipe


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    # find the unique recipe in the database
    my_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})
    # Identify the cuisine type based on the object ID stored in the recipe
    cuisine_type = cuisine.find_one({"_id": ObjectId(my_recipe["cuisine"])})
    # Identify the skill level based on the object ID stored in the recipe
    skill_level = difficulty.find_one(
        {"_id": ObjectId(my_recipe["difficulty"])})
    # Render the relevant recipe details in the viewrecipe.html
    return render_template("viewrecipe.html",
                           recipe=my_recipe,
                           cuisines=cuisine_type,
                           difficulty=skill_level)


# Edit Recipe - Allows a user to edit their own recipes


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    # Find the recipe details 
    my_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})
    # Render the relevant recipe details in the editrecipe.html
    return render_template("editrecipe.html",
                           recipe=my_recipe,
                           cuisines=cuisine.find(),
                           difficulty=difficulty.find(),
                           allergens=allergens.find())


# Update Recipe - Submits an edited recipe to MongoDB


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    # Take the data input by the user in the form
    data = {"created_by": session["username"],
            "soft_delete": False,
            "recipe_name": request.form.get("recipe_name"),
            "image": request.form.get("image"),
            "cuisine": ObjectId(request.form.get("cuisine")),
            "difficulty": ObjectId(request.form.get("difficulty")),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "allergens": request.form.getlist("allergens"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation": request.form.getlist("preparation[]"),
            }
    if request.form.getlist("public"):
        data.update({"public": True})
    else:
        data.update({"public": False})
    # Update the data into the database
    recipe.update({"_id": ObjectId(recipe_id)}, data)
    # Render the relevant recipe details in the viewrecipe.html
    return redirect(url_for("view_recipe", recipe_id=recipe_id))


# Delete Recipe - Allows recipe owner to "soft delete" a recipe record.
# Enables the "admin" user to delete the record from the db.


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    if session["username"] != "admin":
        # If the username is not admin, update the soft_delete boolean.
        recipe.update(
            {"_id": ObjectId(recipe_id)}, {"$set": {"soft_delete": True}})
    else:
        # If the username is admin, delete the record from the database.
        recipe.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("my_recipes", recipes=recipe.find()))


# Search - Allows a user to search for recipes and have results displayed.


@app.route("/search/", methods=["POST"])
def search():
    # Search the database for the users search value, and find applicable recipes
    search_results = recipe.find(
        {"$text": {"$search": request.form["search"]}})
    # Count the number of results
    count = recipe.count_documents(
        {"$text": {"$search": request.form["search"]}})
    # Render the results of the search
    return render_template("index.html",
                           recipes=search_results,
                           count=count,
                           search=True)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
