#AI-Resume-Builder-ML
from flask import Flask, render_template, request
import pickle
import openai
import os

app = Flask(__name__)

# Load ML Model
try:
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
except:
    model = None
    vectorizer = None

# Add your API Key later
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    education = request.form["education"]
    skills = request.form["skills"]
    projects = request.form["projects"]

    # Skill Classification (ML Part)
    category = "General"
    if model and vectorizer:
        skills_vector = vectorizer.transform([skills])
        category = model.predict(skills_vector)[0]

    # Resume Generation (AI Part)
    prompt = f"""
    Create a professional resume with proper sections:

    Name: {name}
    Education: {education}
    Skills: {skills}
    Projects: {projects}
    Skill Domain: {category}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        resume = response["choices"][0]["message"]["content"]
    except:
        resume = "AI response will appear here after API key setup."

    return render_template("result.html", resume=resume, category=category)

if __name__ == "__main__":
    app.run(debug=True)
