# 🍲 Yummo: Bringing People Together Through Food 🍲

## Overview

**Yummo** is a web application designed to unite people through the joy of food while catering to diverse dietary needs. Leveraging AI, Yummo seamlessly transforms recipes to fit various dietary preferences—whether vegan, keto, gluten-free, Jain, vegetarian, or non-vegetarian—without compromising flavor or authenticity. Powered by MindsDB and Google's Gemini Pro model, Yummo provides an inclusive culinary experience, making cooking accessible, enjoyable, and health-conscious.

## Table of Contents 📑
- [Features](#features)
- [Project Highlights](#project-highlights)
- [Technology Stack](#technology-stack)
- [YouTube Demonstration](#youtube-demonstration)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Business Model & Social Impact](#business-model--social-impact)
- [Support](#support)

## Features 🌟

- **Recipe Management**: Add and manage a library of recipes in a local database.
- **Recipe Transformation**: Convert recipes to cater to specific dietary needs:
  - Vegan
  - Keto
  - Gluten-Free
  - Jain
  - Vegetarian
  - Non-Vegetarian
- **User-Friendly Interface**: Simplified web interface for adding recipes and transforming them in real-time.
- **AI-Powered Transformations**: Uses AI to maintain the essence and flavor profile of each recipe after dietary changes.
- **Dual Display**: View both original and transformed recipes side by side.
- **Real-Time Processing**: Quick and efficient AI-based recipe transformations.

## Project Highlights

- **AI-Powered Dietary Transformations**: Utilize the powerful combination of MindsDB and Google’s Gemini Pro model for intelligent and flavor-preserving dietary adaptations.
- **Focus on Accessibility**: Yummo is designed to make cooking enjoyable and accessible for everyone, regardless of dietary needs or restrictions.
- **Community Engagement**: A platform to connect users with a shared love for cooking, encouraging recipe sharing, feedback, and collaboration.

## Technology Stack
- **Backend**: Python with Flask framework
- **Database**: SQLite for local storage
- **AI Integration**: MindsDB 
- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **API**: RESTful API endpoints for recipe management and transformation

## YouTube Demonstration

[Watch the video](https://www.youtube.com/watch?v=rqy8YLz9l-w)

## Requirements
- Python 3.7 or higher
- MindsDB SDK
- SQLite3
  
## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/FaycalZM/dietary-remix
    cd dietary-remix
    ```

2. **Create a virtual environment, activate it, and install required packages**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set up MindsDB**:
    - Follow the [MindsDB installation guide](https://docs.mindsdb.com/install) to install and run MindsDB locally.
    - Make sure to note the server address and port (default is `http://127.0.0.1:47334`).
    - Create a `.env` file with your Google Gemini API key:
      ```bash
      API_KEY='YOUR_KEY'
      ```
    - Start MindsDB with Docker:
      ```bash
      docker run -p 47334:47334 mindsdb/mindsdb
      ```

4. **Create and populate the SQLite database**:
    ```bash
    python data.py
    ```

## Usage
1. **Run the Flask server**:
    ```bash
    flask --app main run --debug
    ```

2. **Add a Recipe**: Enter a recipe name and instructions in the 'add recipe' form.

3. **Transform a Recipe**: Provide a recipe name and select the desired dietary transformation (e.g., vegan, keto, gluten-free, Jain, vegetarian, or non-vegetarian) to see the adjusted recipe.

4. **Access Recipe Data**: Visit [http://localhost:5000/get_recipes](http://localhost:5000/get_recipes) to retrieve all stored recipes.

## Business Model & Social Impact

Yummo's mission extends beyond food to foster community connections and social service:
- **Subscription-Based Model**: A freemium model with basic access to recipe transformation tools and a premium tier for personalized recommendations, in-depth nutritional breakdowns, and advanced AI transformation.
- **Collaborative Cookbook**: Users can contribute recipes and transformations to create a community-driven cookbook, with a percentage of profits donated to food-related charities.
- **Educational Initiatives**: Partnerships with nutritionists and chefs to educate communities about dietary diversity and food inclusivity.
- **Accessibility and Inclusivity**: Emphasis on transforming recipes for diverse diets helps make meals accessible to people with allergies, health conditions, or dietary restrictions.

## Support 💬

If you like this project, please support it by upvoting on Quira and starring the GitHub repository!

[![Quira Repo](https://img.shields.io/badge/Quira-View%20Repo-blue)](https://quira.sh/repo/FaycalZM-dietary-remix-828689730?utm_source=copy&utm_share_context=rdp)

Thank you for your support!
