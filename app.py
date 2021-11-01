from flask import Flask, render_template, request
from student import Student
import random

app = Flask(__name__)


# grades = {
#     "Ali": {2018: 3.97, 2019: 3.94, 2020: 3.99, "prediction": 4.00},
#     "Kamran": {2018: 3.10, 2019: 2.98, 2020: 3.21, "prediction": 2.50},
#     "Sana": {2018: 3.80, 2019: 3.98, 2020: 3.95, "prediction": 3.73}
# }


parents_survey_data = {
    "Ali": {"last_submission": None, "wakeup_time": None, "sleep_time": None, "eating_habbits": None, "family_time": None, "lifestyle_habbits": None},
    "Kamran": {"last_submission": None, "wakeup_time": None, "sleep_time": None, "eating_habbits": None, "family_time": None, "lifestyle_habbits": None},
    "Sana": {"last_submission": None, "wakeup_time": None, "sleep_time": None, "eating_habbits": None, "family_time": None, "lifestyle_habbits": None},
    "Andrew":  {"last_submission": None, "wakeup_time": None, "sleep_time": None, "eating_habbits": None, "family_time": None, "lifestyle_habbits": None},
    "Simon": {"last_submission": None, "wakeup_time": None, "sleep_time": None, "eating_habbits": None, "family_time": None, "lifestyle_habbits": None},
}

subjects = ["Math", "Science", "IT", "Arabic", "Quran", "English", "French"]
Kamran = Student("Kamran",  {subject: random.randint(1, 100) for subject in subjects}, "M", "lebanon", "lebanon", "MiddleSchool", "G-08", "A", random.choice(subjects), "F", "Father", 15, 14, 12, 60, random.choice(["Yes", "No"]), random.choice(["Under-7", "Above-7"]), random.choice(["M", "L", "H"]),
                 random.choice(["Yes", "No"]), "Male", random.randint(17, 26), random.choice(["Yes", "No"]), random.choice(["Yes", "No"]), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 
                 random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), "Positivity")

Andrew =  Student("Andrew",  {subject: random.randint(1, 100) for subject in subjects}, "M", "Egypt", "Egypt", "MiddleSchool", "G-07", "A", random.choice(subjects), "F", "Father", 8, 10, 20, 90, random.choice(["Yes", "No"]), random.choice(["Under-7", "Above-7"]), random.choice(["M", "L", "H"]),
                 random.choice(["Yes", "No"]), "Male", random.randint(17, 26), random.choice(["Yes", "No"]), random.choice(["Yes", "No"]), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 
                 random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), "Passion")

Simon =  Student("Simon",  {subject: random.randint(1, 100) for subject in subjects}, "M", "KW", "KuwaIT", "lowerlevel", "G-12", "A", random.choice(subjects), "F", "Mum", 70, 80, 10, 90, random.choice(["Yes", "No"]), random.choice(["Under-7", "Above-7"]), random.choice(["M", "L", "H"]),
                 random.choice(["Yes", "No"]), "Male", random.randint(17, 26), random.choice(["Yes", "No"]), random.choice(["Yes", "No"]), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 
                 random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), "Vision")
students = [Kamran, Andrew, Simon]
current_student = random.choice([Kamran, Andrew, Simon]) # currently logged in student


@app.route("/")
def index():
    # calculating cgpa for current_student
    current_student_marks = current_student.marks
    self_grade = round((sum(current_student_marks.values()) / len(current_student_marks.values())), 3)  # average of all markssi
    predicted_marks = current_student.predicted_marks
    recommended_courses =  list(set([random.choice(subjects) for _ in range(5)]))

    all_grades = {}
    for student in students:
        all_grades[student.name] = student.marks
        all_grades[student.name]["self_grade"] = self_grade
        all_grades[student.name]["prediction"] = predicted_marks

    # return parents_survey_data
    return render_template("index.html", self_grade=self_grade, all_students=students, predicted_grade=predicted_marks, recommended_courses=recommended_courses, 
    all_grades=all_grades, 
    current_student=current_student.name, 
    parents_survey_data=parents_survey_data,
    subjects=subjects
    )


@app.route("/submit_student_checkin_survey", methods=["POST"])
def submit_student_checkin_survey():
    return str(request.form)


@app.route("/submit_teacher_checkin_survey", methods=["POST"])
def submit_teacher_checkin_survey():
    return str(request.form)


@app.route("/submit_parent_checkin_survey", methods=["POST"])
def submit_parent_checkin_survey():
    form_result = request.form
    student_name = request.form.get("student_name")
    if student_name not in grades:
        grades[student_name] = {2018: 3.20,
                                2019: 3.18, 2020: 2.85, "prediction": 3.33}
    if student_name:
        global parents_survey_data
        parents_survey_data[student_name] = {}
        parents_survey_data[student_name]["last_submission"] = form_result.get(
            "submission") if form_result.get("submission") else None
        parents_survey_data[student_name]["wakeup_time"] = form_result.get(
            "wakeup_time") if form_result.get("wakeup_time") else None
        parents_survey_data[student_name]["sleep_time"] = form_result.get(
            "sleep_time") if form_result.get("sleep_time") else None
        parents_survey_data[student_name]["eating_habbits"] = form_result.getlist(
            "eating_habbits") if form_result.getlist("eating_habbits") else None
        parents_survey_data[student_name]["lifestyle_habbits"] = form_result.get(
            "lifestyle_habbits") if form_result.get("lifestyle_habbits") else None
        parents_survey_data[student_name]["family_time"] = form_result.get(
            "family_time") if form_result.get("family_time") else None
        global CURRENT_STUDENT
        CURRENT_STUDENT = student_name

    return str(parents_survey_data) + "<br><br><br><br>" + str(request.form)


app.run(debug=True)
