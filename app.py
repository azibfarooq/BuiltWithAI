from flask import Flask, render_template, request

app = Flask(__name__)


grades = {
    "Ali": {2018: 3.97, 2019: 3.94, 2020: 3.99, "prediction": 4.00},
    "Kamran": {2018: 3.10, 2019: 2.98, 2020: 3.21, "prediction": 2.50},
    "Sana": {2018: 3.80, 2019: 3.98, 2020: 3.95, "prediction": 3.73}
}


parents_survey_data = {
    "Ali": {"last_submission": None, "wakeup_time": None, "sleep_time": None, "eating_habbits": None, "family_time": None, "lifestyle_habbits": None},
    "Kamran": {"last_submission": None, "wakeup_time": None, "sleep_time": None, "eating_habbits": None, "family_time": None, "lifestyle_habbits": None},
    "Sana": {"last_submission": None, "wakeup_time": None, "sleep_time": None, "eating_habbits": None, "family_time": None, "lifestyle_habbits": None}
}

CURRENT_STUDENT = "Kamran"  # currently logged in student


@app.route("/")
def index():
    # calculating cgpa for current_student 
    current_student_grades = grades[CURRENT_STUDENT].values() if grades.get(CURRENT_STUDENT) else grades["Kamran"].values()  # all grades
    self_grade = round((sum(current_student_grades) / len(current_student_grades)), 3)  # average of all grades

    predicted_grade = 3.61
    recommended_courses = ["Fundamentals Of Computer Engineering", "Basic Electrical Engineering", "Basic Mechanical Engineering", "German Language", "Intro To Programming"]

    # return parents_survey_data
    return render_template("index.html", self_grade=self_grade, predicted_grade=predicted_grade, recommended_courses=recommended_courses, all_grades=grades, current_student=CURRENT_STUDENT, parents_survey_data=parents_survey_data)


@app.route("/submit_parent_checkin_survey", methods=["POST"])
def submit_parent_checkin_survey():
    form_result = request.form
    student_name = request.form.get("student_name")
    if student_name not in grades:
        grades[student_name] = {2018: 3.20, 2019: 3.18, 2020: 2.85, "prediction": 3.33}
    if student_name:
        global parents_survey_data
        parents_survey_data[student_name] = {}
        parents_survey_data[student_name]["last_submission"] = form_result.get("submission") if form_result.get("submission") else None
        parents_survey_data[student_name]["wakeup_time"] = form_result.get("wakeup_time") if form_result.get("wakeup_time") else None
        parents_survey_data[student_name]["sleep_time"] = form_result.get("sleep_time") if form_result.get("sleep_time") else None
        parents_survey_data[student_name]["eating_habbits"] = form_result.getlist("eating_habbits") if form_result.getlist("eating_habbits") else None
        parents_survey_data[student_name]["lifestyle_habbits"] = form_result.get("lifestyle_habbits") if form_result.get("lifestyle_habbits") else None
        parents_survey_data[student_name]["family_time"] = form_result.get("family_time") if form_result.get("family_time") else None
        global CURRENT_STUDENT
        CURRENT_STUDENT = student_name
    


    
    return str(parents_survey_data)+ "<br><br><br><br>" + str(request.form) 

app.run(debug=True)