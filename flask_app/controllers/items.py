from flask import Flask, render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.restaurant import Restaurant
from flask_app.models.ingredient import Ingredient
from flask_app.models.preference import Preference


# GET Routes
# Render page to Display Restaurant's Item
@app.route("/restaurant/<restaurant_id>/<item_id>")
def item_detail(restaurant_id, item_id):
    print("We're on the item detail page!: ", restaurant_id, item_id)
    # TO DO Need to get item details from the database
    # TO DO Need to pass item details into the template
    return render_template("item_detail.html")

# Render page to Create Restaurant's Item
@app.route("/restaurant/<restaurant_id>")
def create_item_page():
    print("In the create route")
    return render_template("create_item.html")

# Render page to Edit Restaurant's Item
@app.route("/restaurant/<restaurant_id>/edit/<item_id>")
def edit_item_page(restaurant_id, item_id):
    print("In the edit item page: ", restaurant_id, item_id)
    # TO DO Need to get recipe from the database
    return render_template("edit_item.html")

# Delete Restaurant's Item
@app.route("/restaurant/<restaurant_id>/delete/<item_id>")
def delete_item(restaurant_id, item_id):
    print("In the delete route:", restaurant_id, item_id)
    # call delete method
    return redirect("/restaurant/<restaurant_id>")

# CREATE Item (Process Form)
@app.route("/restaurant/<restaurant_id>", methods=['POST'])
def create_item(restaurant_id):
    print("we are in the item creation (POST) route!", restaurant_id, request.form)
    return redirect("/restaurant/<restaurant_id>")


# UPDATE Item (Process Form)
@app.route("/restaurant/<restaurant_id>/edit", methods=['POST'])
def edit_item(restaurant_id):
    print("In the edit item (POST) route: ", restaurant_id, request.form)
    # Should this be redirected to the item detail page instead? If yes, how do we pass the item_id? 
    return redirect("/restaurant/<restaurant_id>")



