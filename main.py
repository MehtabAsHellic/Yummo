from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from typing import Optional
import sqlite3
from functools import wraps

# Configuration
class Config:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    DATABASE_PATH = 'recipes.db'
    MODEL_NAME = 'gemini-pro'

# Initialize Flask app
app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize Gemini
def initialize_gemini() -> Optional[genai.GenerativeModel]:
    try:
        genai.configure(api_key=Config.GEMINI_API_KEY)
        model = genai.GenerativeModel(Config.MODEL_NAME)
        return model
    except Exception as e:
        print(f"Error initializing Gemini: {str(e)}")
        return None

# Error handling decorator
def handle_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return decorated_function

# Initialize the model
model = initialize_gemini()

# Routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/transform_recipe', methods=['POST'])
@handle_errors
def transform_recipe():
    if not model:
        return jsonify({"error": "AI model not initialized"}), 503
    
    recipe_name = request.form.get('recipe_name')
    original_recipe_text = request.form.get('recipe_text')
    diet = request.form.get('diet')
    print(diet)
    allergy=request.form.get('Allergy')
    place=request.form.get('Place')
    calories=request.form.get('Calories')

    if not all([recipe_name, original_recipe_text, diet,allergy,place,calories]):
        return jsonify({"error": "Missing required fields"}), 400
    
    prompt = f"""Transform this recipe:
    Name: {recipe_name}
    Diet: {diet}
    Recipe: {original_recipe_text}
    Allergy: {allergy}
    Place: {place}
    Desired Calories: {calories}
    
    Please provide a modified version that follows the diet requirements while maintaining the essence of the original recipe and it must be available at the Place and must not include the allergy contents and it must be in the range of desired calories. Also mention the calories and protein content in the input recipe and the generated recipe"""
    
    prompt_costs = f"""Calculate the initial cost of preparation and reduced cost of preparation for the following recipe:
    Name: {recipe_name}
    Recipe: {original_recipe_text}
    Diet: {diet}
    Allergy: {allergy}
    Place: {place}"""
    
    prompt_nutrition = f"""Provide the nutritional information (initial protein and calorie content) for the following recipe:
    Name: {recipe_name}
    Recipe: {original_recipe_text}"""

    try:
        response = model.generate_content(prompt)
        transformed_recipe = response.text

        response_costs = model.generate_content(prompt_costs)
        costs_info = response_costs.text

        # Call 3: Nutrition information
        response_nutrition = model.generate_content(prompt_nutrition)
        nutrition_info = response_nutrition.text

        return jsonify({
            "costs_info": costs_info,
            "nutrition_info": nutrition_info,
            "diet": diet,
            "allergy": allergy,
            "place": place,
            "calories": calories,
            "recipe_name": recipe_name,
            "original_recipe": original_recipe_text,
            "transformed_recipe": transformed_recipe,
        })

    except Exception as e:
        return jsonify({"error": f"Failed to transform recipe: {str(e)}"}), 500

@app.route('/add_recipe', methods=['POST'])
@handle_errors
def add_recipe():
    recipe_name = request.form.get('recipe_name')
    recipe_text = request.form.get('recipe_text')
    
    if not recipe_name or not recipe_text:
        return jsonify({"error": "Both recipe name and text are required"}), 400
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO recipes (recipe_name, recipe_text) VALUES (?, ?)",
            (recipe_name, recipe_text)
        )
        recipe_id = cursor.lastrowid
        conn.commit()
    
    return jsonify({
        "message": "Recipe added successfully",
        "recipe_id": recipe_id
    }), 201

@app.route('/get_recipes', methods=['GET'])
@handle_errors
def get_recipes():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT recipe_id, recipe_name FROM recipes")
        recipes = cursor.fetchall()
    
    return jsonify([{
        "id": recipe['recipe_id'],
        "name": recipe['recipe_name']
    } for recipe in recipes])

# Database initialization
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS recipes (
                recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe_name TEXT NOT NULL,
                recipe_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)