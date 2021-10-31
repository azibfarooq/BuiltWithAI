from flask import Flask, render_template, request

app = Flask(__name__)


grades = {
    "Ali": {2018: 3.97, 2019: 3.94, 2020: 3.99},
    "Kamran": {2018: 3.10, 2019: 2.98, 2020: 3.21},
    "Sana": {2018: 3.80, 2019: 3.98, 2020: 3.95}
}

parents_survey_data = {
    "Ali": {"lifestyle_habbits": None, "eating_habbits": None, "wakeup_time": None, "family_time": None},
    "Kamran": {"lifestyle_habbits": None, "eating_habbits": None, "wakeup_time": None, "family_time": None},
    "Sana": {"lifestyle_habbits": None, "eating_habbits": None, "wakeup_time": None, "family_time": None}
}

CURRENT_STUDENT = "Kamran"  # currently logged in student


@app.route("/")
def index():
    # calculating cgpa for current_student 
    current_student_grades = grades[CURRENT_STUDENT].values()  # all grades
    self_grade = round(sum(current_student_grades) / len(current_student_grades), 3)  # average of all grades

    predicted_grade = 3.61
    recommended_courses = ["Fundamentals Of Computer Engineering", "Basic Electrical Engineering", "Basic Mechanical Engineering", "German Language", "Intro To Programming"]

    return render_template("index.html", self_grade=self_grade, predicted_grade=predicted_grade, recommended_courses=recommended_courses, all_grades=grades, current_student=CURRENT_STUDENT, parents_survey_data=parents_survey_data)


@app.route("/submit_parent_checkin_survey", methods=["POST"])
def submit_parent_checkin_survey():
    parents_survey_data[CURRENT_STUDENT] = dict(request.form)
    print(parents_survey_data)
    return str(request.form) + str(request.args)

app.run(debug=True)