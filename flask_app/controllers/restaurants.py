from flask import Flask, render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.item import Item

# GET Routes

@app.route("/home")
def menuDB_home():
    if "user_id" not in session:
        flash("You must be logged in to access this page.")
        return redirect("/")
    
    user = User.get_by_id(session["user_id"])

    # TO DO:
    # GET ALL items from all restaurants and send to the template

    return render_template("home.html", user = user)

# Render Restaurant Details page for one restaurant
@app.route("/restaurant/<restaurant_id>")
def restaurant_details(restaurant_id):
    print("In restaurant details: ", restaurant_id)
    return render_template("restaurant_detail.html")

# Future Development: create, edit, delete Restaurants