from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Function to load questions from JSON file
def load_questions():
    file_path = os.path.join(os.path.dirname(__file__), "data/questions.json")
    with open(file_path, "r") as file:
        return json.load(file)

@app.route("/")
def index():
    questions = load_questions()  # ✅ Load questions dynamically
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    submitted_answers = request.form
    questions = load_questions()  # ✅ Load questions for checking
    score = sum(1 for q in questions if submitted_answers.get(f"q{q['id']}") == q["answer"])
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(debug=True)
