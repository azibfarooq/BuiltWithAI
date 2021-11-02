
from random import sample
from sklearn.preprocessing import OneHotEncoder
import pickle
import numpy as np

import warnings
warnings.filterwarnings('ignore')
import pandas as pd



# Algo1 work
file1 = "clean_data.csv"
df1 = pd.read_csv(file1)
df1.drop(['Unnamed: 0'], axis=1, inplace=True)
df1['MentalDisorder'].replace(['Yes','No'],[1, 0],inplace=True)
features_df1 = df1.drop('MentalDisorder', axis='columns')
sample_data1 = features_df1.sample(1)
filename1 = 'mental_model.pkl'
train_model1 = pickle.load(open(filename1, 'rb'))



#algo 2 work
file2 = "xAPI-Edu-Data.csv"
df2 = pd.read_csv(file2)
df2['ParentschoolSatisfaction'].replace(['Bad','Good'],[1, 0],inplace=True)
features_df2 = df2.drop('ParentschoolSatisfaction', axis='columns')
sample_data2 = features_df2.sample(1)

### Model load and pridict the value
# load the model from disk
filename2 = 'parent_satisfiction_model.pkl'
train_model2 = pickle.load(open(filename2, 'rb'))



def predict_happy_path(input_data, model_name):
    """ Pridict the result based on the input values"""
    numeric_cols = input_data.columns[input_data.dtypes != "object"].values
    categori_cols = input_data.columns[input_data.dtypes == "object"].values
    
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoder.fit(features_df1[categori_cols])
    
    encoded_cols = list(encoder.get_feature_names(categori_cols))
    input_data[encoded_cols] = encoder.transform(input_data[categori_cols])
    
    numeric_cols = input_data.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = input_data.select_dtypes('category').columns.tolist()
    
    input_data = input_data[numeric_cols]
    
    return model_name.predict(input_data)


def predict_parent_satisfaction(input_data, model_name):
    """ Pridict the result based on the input values"""
    numeric_cols = input_data.columns[input_data.dtypes != "object"].values
    categori_cols = input_data.columns[input_data.dtypes == "object"].values
    
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoder.fit(features_df2[categori_cols])
    
    encoded_cols = list(encoder.get_feature_names(categori_cols))
    input_data[encoded_cols] = encoder.transform(input_data[categori_cols])
    
    numeric_cols = input_data.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = input_data.select_dtypes('category').columns.tolist()
    
    input_data = input_data[numeric_cols]
    
    return model_name.predict(input_data)



def get_happy_path(student):
    new_vals = {
        "IndividualProject": student.IndividualProject	, "Age": student.Age, "Gender": student.Gender, "City": student.City, "Influenced": student.Influenced,
        "Perseverance": student.Perseverance, "DesireToTakeInitiative": student.DesireToTakeInitiative, "Competitiveness": student.Competitiveness, "SelfReliance": student.SelfReliance, "StrongNeedToAchieve": student.StrongNeedToAchieve, "SelfConfidence": student.SelfConfidence,
        "GoodPhysicalHealth": student.GoodPhysicalHealth, "KeyTraits": student.KeyTraits
    }   
    sample_data1.append(new_vals, ignore_index=True)
    answer = predict_happy_path(sample_data1.tail(1), train_model1)
    return answer


def get_parent_satisfaction(student):
    new_vals = {
        "gender": student.gender, "NationalITy": student.NationalITy, "PlaceofBirth": student.PlaceofBirth, "StageID": student.StageID, "GradeID": student.GradeID,
        "SectionID": student.SectionID, "Topic": student.Topic, "Semester": student.Semester, "Relation": student.Relation, "raisedhands": student.raisedhands, "VisITedResources": student.VisITedResources,
        "AnnouncementsView": student.AnnouncementsView, "Discussion": student.Discussion, "ParentAnsweringSurvey": student.ParentAnsweringSurvey, "StudentAbsenceDays": student.StudentAbsenceDays,
        "Class": student.Class
    }   
    sample_data2.append(new_vals, ignore_index=True)
    answer = predict_parent_satisfaction(sample_data2.tail(1), train_model2)

    return answer


