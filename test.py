



# from student import Student
# import random


# subjects = ["Math", "Science", "IT", "Arabic", "Quran", "English", "French"]
# x = set(
#     [random.choice(subjects) for _ in range(5)]
#     )

# print(x)



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

print(sample_data1)