from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def index():
    self_grade = 3.79
    predicted_grade = 3.61
    recommended_courses = ["Fundamentals Of Computer Engineering", "Basic Electrical Engineering", "Basic Mechanical Engineering", "German Language", "Intro To Programming"]
    return render_template("index.html", self_grade=self_grade, predicted_grade=predicted_grade, recommended_courses=recommended_courses)


app.run(debug=True)