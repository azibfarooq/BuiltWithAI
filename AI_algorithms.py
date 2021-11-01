
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
    answer = predict_parent_satisfaction(sample_data.tail(), train_model)

    return answer

def get_happy_path(student):
    new_vals = {
        "IndividualProject": student.IndividualProject	, "Age": student.Age, "Gender": student.Gender, "City": student.City, "Influenced": student.Influenced,
        "Perseverance": student.Perseverance, "DesireToTakeInitiative": student.DesireToTakeInitiative, "Competitiveness": student.Competitiveness, "SelfReliance": student.SelfReliance, "StrongNeedToAchieve": student.StrongNeedToAchieve, "SelfConfidence": student.SelfConfidence,
        "GoodPhysicalHealth": student.GoodPhysicalHealth, "KeyTraits": student.KeyTraits
    }   
    sample_data.append(new_vals, ignore_index=True)
    answer = predict_happy_path(sample_data.tail(), train_model)

    return answer


