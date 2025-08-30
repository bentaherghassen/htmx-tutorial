from flask import Flask, render_template, request, jsonify
import requests
from cars_model import car_models
app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", car_models=car_models)  # Pass car_models HERE

# just comment 
@app.route("/cars", methods=["GET"])
def cars():
    car_maker = request.args.get("maker")
    if car_maker:
        list_of_models = car_models.get(car_maker, []) # Get models, empty list if maker not found
        return render_template("available_models.html", list_of_models=list_of_models)
    return ""  # Important for HTMX - return empty string if no maker

@app.route("/search_coins")
def search_coins():
    query = request.args.get("query")
    if query:
        r = requests.get(f"https://api.coingecko.com/api/v3/search?query={query}")
        coins = r.json()["coins"]

        return render_template("coins.html", coins=coins)
    return ""


if __name__ == "__main__":
    app.run(debug=True)
