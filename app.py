from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define quiz questions and correct answers
questions = [
    {
        "id": 1,
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "22"],
        "answer": "4"
    },
    {
        "id": 2,
        "question": "The capital of France is?",
        "options": ["London", "Paris", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "id": 3,
        "question": "Which of these is a mammal?",
        "options": ["Shark", "Dolphin", "Eagle", "Turtle"],
        "answer": "Dolphin"
    }
]

@app.route("/")
def index():
    # Render the template with the questions data
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    # Retrieve the submitted form data
    submitted_answers = request.form
    score = 0
    # Calculate score by comparing each answer
    for q in questions:
        selected = submitted_answers.get(f"q{q['id']}")  # e.g., "q1", "q2", etc.
        if selected == q["answer"]:
            score += 1
    # Return the score as JSON
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(debug=True)
