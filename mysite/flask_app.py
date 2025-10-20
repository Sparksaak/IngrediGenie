from flask import *
from openai import *
import json

client = OpenAI(api_key="OPENAI_API_KEY")
app = Flask(__name__)


name = ""
prep_time = ""
cook_time = ""
total_time = ""
yields = ""
description = ""
ingredients = []
recipe_steps = []
view_count = 0


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get-started")
def get_started():
    global view_count, name, prep_time, cook_time, total_time, yields, description, ingredients, recipe_steps
    view_count += 1
    if view_count > 3:
        view_count = 0
        name = ""
        prep_time = ""
        cook_time = ""
        total_time = ""
        yields = ""
        description = ""
        ingredients = []
        recipe_steps = []
    return render_template("get_started.html", name=name, prep_time=prep_time, cook_time=cook_time, total_time=total_time, yields=yields, description=description, ingredients=ingredients, recipe_steps=recipe_steps)


@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    leftovers, cuisine, diet, requests = data.get('ingredients'), data.get(
        'cuisine'), data.get('diet'), data.get('requests')
    prompt = f"""Pretend you are an expert recipe creator. You need to use the given ingredients, cuisine, dietary restrictions, and any other requests I might have to generate a delicious and edible recipe. Follow the provided instructions to the letter.

    Here are the parameters you need to use:
    Ingredients: {leftovers}
    Cuisine: {cuisine}
    Dietary Restrictions: {diet}
    Special Requests: {requests}

    Make sure to provide recipes that use at least 80% of the ingredients or more, if possible. If you need to use any more ingredients, make sure to only use common pantry items. Do not use ingredients that the average person might not have.

    Provide your response in the following JSON format with the same keys and nothing else:
    {{
        "name": "Provide the name of the recipe",
        "prep-time": "Provide the amount of time the recipe will take to prepare",
        "cook-time": "Provide the amount of time the recipe will take to cook",
        "total-time": "Provide the total amount of time the recipe will take to cook in all",
        "yields": "Provide the number of people this recipe will serve",
        "description": "Provide a description of what the recipe is",
        "ingredients": "[Provide all of the ingredients you plan to use with quanitities separated by "\\n" characters, one-by-one, without any numbering or bullet points, just a simple list of ingredients and quantities]",
        "recipe": "[Provide the recipe, step-by-step, separated by "\\n" characters without any numbering or bullet points, just a simple list of steps]"
    }}

    Go ahead and whip up some delicious recipes!"""
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    ).output_text
    response = json.loads(response)
    global name, prep_time, cook_time, total_time, yields, description, ingredients, recipe_steps
    name = response["name"]
    prep_time = response["prep-time"]
    cook_time = response["cook-time"]
    total_time = response["total-time"]
    yields = response["yields"]
    description = response["description"]
    ingredients = response["ingredients"].split("\n")
    recipe_steps = response["recipe"].split("\n")
    return redirect(url_for('get_started'))

