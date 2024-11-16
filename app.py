from flask import Flask, request, render_template, redirect, url_for
from operations import (
    add_seasonal_flavor, add_ingredient, add_customer_feedback,
    get_all_records, update_ingredient_quantity
)

app = Flask(__name__)

@app.route("/")
def home():
   
    seasonal_flavors = get_all_records("SeasonalFlavors")
    ingredients = get_all_records("IngredientInventory")
    feedbacks = get_all_records("CustomerFeedback")
    
   
    return render_template("index.html", 
                           seasonal_flavors=seasonal_flavors, 
                           ingredients=ingredients, 
                           feedbacks=feedbacks)

@app.route("/add_flavor", methods=["POST"])
def add_flavor():
    name = request.form["flavor_name"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    add_seasonal_flavor(name, start_date, end_date)
    return redirect(url_for("home"))

@app.route("/add_ingredient", methods=["POST"])
def add_ingredient_route():
    name = request.form["ingredient_name"]
    quantity = request.form["quantity"]
    add_ingredient(name, quantity)
    return redirect(url_for("home"))

@app.route("/add_feedback", methods=["POST"])
def add_feedback():
    name = request.form["customer_name"]
    flavor = request.form["suggested_flavor"]
    allergy = request.form["allergy_concern"]
    add_customer_feedback(name, flavor, allergy)
    return redirect(url_for("home"))

@app.route("/update_ingredient", methods=["POST"])
def update_ingredient():
    ingredient_name = request.form["ingredient_name"]
    new_quantity = int(request.form["quantity"])
    update_ingredient_quantity(ingredient_name, new_quantity)
    return redirect(url_for("home"))

@app.route("/view_records/<table_name>")
def view_records(table_name):
    records = get_all_records(table_name)
    return {"data": records} 

if __name__ == "__main__":
    app.run(debug=True)
