from flask import Flask, render_template, request
from questions import questions

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    score = None

    if request.method == "POST":

        score = 0

        for number, question in enumerate(questions, 1):

            answer = request.form.get(f"question{number}")

            if answer == question["answer"]:
                score += 1

    return render_template(
        "index.html",
        questions=questions,
        score=score
    )


if __name__ == "__main__":
    app.run(debug=True)
    