from flask import Flask, render_template, request, flash, redirect
from student import Student
import random
# from AI_algorithms import get_happy_path, get_parent_satisfaction
app = Flask(__name__)
app.secret_key = "35gbbad932565nnssndg"


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

subjects = ["Math", "Science", "Biology", "Chemistry", "Geology", "History", "IT"]
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

    # Kamran = Student("Kamran",  {subject: random.randint(1, 100) for subject in subjects}, "M", "lebanon", "lebanon", "MiddleSchool", "G-08", "A", random.choice(subjects), "F", "Father", 15, 14, 12, 60, random.choice(["Yes", "No"]), random.choice(["Under-7", "Above-7"]), random.choice(["M", "L", "H"]),
    #              random.choice(["Yes", "No"]), "Male", random.randint(17, 26), random.choice(["Yes", "No"]), random.choice(["Yes", "No"]), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 
    #              random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), "Positivity")

    # Andrew =  Student("Andrew",  {subject: random.randint(1, 100) for subject in subjects}, "M", "Egypt", "Egypt", "MiddleSchool", "G-07", "A", random.choice(subjects), "F", "Father", 8, 10, 20, 90, random.choice(["Yes", "No"]), random.choice(["Under-7", "Above-7"]), random.choice(["M", "L", "H"]),
    #                 random.choice(["Yes", "No"]), "Male", random.randint(17, 26), random.choice(["Yes", "No"]), random.choice(["Yes", "No"]), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 
    #                 random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), "Passion")

    # Simon =  Student("Simon",  {subject: random.randint(1, 100) for subject in subjects}, "M", "KW", "KuwaIT", "lowerlevel", "G-12", "A", random.choice(subjects), "F", "Mum", 70, 80, 10, 90, random.choice(["Yes", "No"]), random.choice(["Under-7", "Above-7"]), random.choice(["M", "L", "H"]),
    #                 random.choice(["Yes", "No"]), "Male", random.randint(17, 26), random.choice(["Yes", "No"]), random.choice(["Yes", "No"]), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 
    #                 random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), "Vision")
    # students = [Kamran, Andrew, Simon]
    # current_student = random.choice([Kamran, Andrew, Simon]) # currently logged in student

    for s in students:
        parent_satisfaction = get_parent_satisfaction(s)[0]
        if parent_satisfaction == 0:
            s.parent_satisfaction = random.randint(1, 5)
        else:
            s.parent_satisfaction = random.randint(6, 10)

        happy_path = get_happy_path(s)[0]
        if happy_path == 0:
            s.happy_path = random.randint(1, 5)
        else:
            s.happy_path = random.randint(6, 10)

    # print(sample_data)
    # return str([(s.name, s.happy_path, s.parent_satisfaction) for s in students]) + "<br><br>" 
    # return f"Happy path score: {happy_path}, parent_satisfaction: {parent_satisfaction} student = {current_student.name}"

    # calculating cgpa for current_student
    current_student_marks = current_student.marks
    self_grade = round((sum(current_student_marks.values()) / len(current_student_marks.values())), 3)  # average of all markssi
    predicted_marks = current_student.predicted_marks
    recommended_courses =  list(set([random.choice(subjects) for _ in range(5)]))

    all_grades = {}
    for student in students:
        marks = student.marks
        all_grades[student.name] = marks
        all_grades[student.name]["self_grade"] = round((sum(marks.values()) / len(marks.values())), 3)
        all_grades[student.name]["prediction"] = student.predicted_marks

    # return parents_survey_data
    return render_template("index.html", self_grade=self_grade, all_students=students, predicted_grade=predicted_marks, recommended_courses=recommended_courses, 
    all_grades=all_grades, 
    current_student=current_student, 
    parents_survey_data=parents_survey_data,
    subjects=subjects,
    )


@app.route("/submit_student_checkin_survey", methods=["POST"])
def submit_student_checkin_survey():
    form = request.form
    student_name = form.get("student_name").strip()
    if not student_name:
        student_name = current_student.name
    
    student = None
    for s in students:
        student = s
        if current_student.name.lower() == student_name.lower():
            break

    student.GoodPhysicalHealth = int(request.form.get("physical_health"))
    
    flash("Student checkin survery successfully submitted!")
    return redirect("/")


@app.route("/submit_teacher_checkin_survey", methods=["POST"])
def submit_teacher_checkin_survey():
    form = request.form
    student_name = form.get("student_name").strip()
    if not student_name:
        student_name = current_student.name
    
    student = None
    for s in students:
        student = s
        if current_student.name.lower() == student_name.lower():
            break

    student.Discussion = int(request.form.get("discussions"))
    student.StudentAbsenceDays = request.form.get("absences")

    flash("Teacher checkin survery successfully submitted!")
    return redirect("/")


@app.route("/submit_parent_checkin_survey", methods=["POST"])
def submit_parent_checkin_survey():
    # global
    form = request.form
    student_name = form.get("student_name").strip()
    if not student_name:
        student_name = current_student.name
    
    student = None
    for s in students:
        student = s
        if current_student.name.lower() == student_name.lower():
            break

    key_trait = form.get("key_trait")

    if not key_trait:
        key_trait = "Passion"

    student.KeyTraits = key_trait
    
    # form_result = request.form
    # student_name = request.form.get("student_name")
    # if student_name not in grades:
    #     grades[student_name] = {2018: 3.20,
    #                             2019: 3.18, 2020: 2.85, "prediction": 3.33}
    # if student_name:
    #     global parents_survey_data
    #     parents_survey_data[student_name] = {}
    #     parents_survey_data[student_name]["last_submission"] = form_result.get(
    #         "submission") if form_result.get("submission") else None
    #     parents_survey_data[student_name]["wakeup_time"] = form_result.get(
    #         "wakeup_time") if form_result.get("wakeup_time") else None
    #     parents_survey_data[student_name]["sleep_time"] = form_result.get(
    #         "sleep_time") if form_result.get("sleep_time") else None
    #     parents_survey_data[student_name]["eating_habbits"] = form_result.getlist(
    #         "eating_habbits") if form_result.getlist("eating_habbits") else None
    #     parents_survey_data[student_name]["lifestyle_habbits"] = form_result.get(
    #         "lifestyle_habbits") if form_result.get("lifestyle_habbits") else None
    #     parents_survey_data[student_name]["family_time"] = form_result.get(
    #         "family_time") if form_result.get("family_time") else None
    #     global CURRENT_STUDENT
    #     CURRENT_STUDENT = student_name

    # return str(parents_survey_data) + "<br><br><br><br>" + str(request.form)

    flash("Parents checkin survey form submitted!")
    return redirect("/")


#### AI ALGOS

from random import sample
from sklearn.preprocessing import OneHotEncoder
import pickle
import numpy as np

import warnings
warnings.filterwarnings('ignore')
import pandas as pd

file = "xAPI-Edu-Data.csv"
df = pd.read_csv(file)
df['ParentschoolSatisfaction'].replace(['Bad','Good'],[1, 0],inplace=True)
features_df = df.drop('ParentschoolSatisfaction', axis='columns')
sample_data = features_df.sample(1)


### Model load and pridict the value
# load the model from disk
filename = 'parent_satisfiction_model.pkl'
train_model = pickle.load(open(filename, 'rb'))


def predict_parent_satisfaction(input_data, model_name):
    """ Pridict the result based on the input values"""
    numeric_cols = input_data.columns[input_data.dtypes != "object"].values
    categori_cols = input_data.columns[input_data.dtypes == "object"].values
    
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoder.fit(features_df[categori_cols])
    
    encoded_cols = list(encoder.get_feature_names(categori_cols))
    input_data[encoded_cols] = encoder.transform(input_data[categori_cols])
    
    numeric_cols = input_data.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = input_data.select_dtypes('category').columns.tolist()
    
    input_data = input_data[numeric_cols]
    
    return model_name.predict(input_data)



def predict_happy_path(input_data, model_name):
    """ Pridict the result based on the input values"""
    numeric_cols = input_data.columns[input_data.dtypes != "object"].values
    categori_cols = input_data.columns[input_data.dtypes == "object"].values
    
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoder.fit(features_df[categori_cols])
    
    encoded_cols = list(encoder.get_feature_names(categori_cols))
    input_data[encoded_cols] = encoder.transform(input_data[categori_cols])
    
    numeric_cols = input_data.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = input_data.select_dtypes('category').columns.tolist()
    
    input_data = input_data[numeric_cols]
    
    return model_name.predict(input_data)


def get_parent_satisfaction(student):
    new_vals = {
        "gender": student.gender, "NationalITy": student.NationalITy, "PlaceofBirth": student.PlaceofBirth, "StageID": student.StageID, "GradeID": student.GradeID,
        "SectionID": student.SectionID, "Topic": student.Topic, "Semester": student.Semester, "Relation": student.Relation, "raisedhands": student.raisedhands, "VisITedResources": student.VisITedResources,
        "AnnouncementsView": student.AnnouncementsView, "Discussion": student.Discussion, "ParentAnsweringSurvey": student.ParentAnsweringSurvey, "StudentAbsenceDays": student.StudentAbsenceDays,
        "Class": student.Class
    }   
    sample_data.append(new_vals, ignore_index=True)
    answer = predict_parent_satisfaction(sample_data.iloc[-1:], train_model)

    return answer

def get_happy_path(student):
    new_vals = {
        "IndividualProject": student.IndividualProject	, "Age": student.Age, "Gender": student.Gender, "City": student.City, "Influenced": student.Influenced,
        "Perseverance": student.Perseverance, "DesireToTakeInitiative": student.DesireToTakeInitiative, "Competitiveness": student.Competitiveness, "SelfReliance": student.SelfReliance, "StrongNeedToAchieve": student.StrongNeedToAchieve, "SelfConfidence": student.SelfConfidence,
        "GoodPhysicalHealth": student.GoodPhysicalHealth, "KeyTraits": student.KeyTraits
    }   
    sample_data.append(new_vals, ignore_index=True)
    answer = predict_happy_path(sample_data.iloc[-1:], train_model)

    return answer



if __name__ == '__main__':
    app.run("0.0.0.0", port=int("8080"), debug=True)
