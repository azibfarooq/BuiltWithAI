# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# ### 1. Importing Libraries 

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from scipy import stats
from scipy.stats import skew
import warnings
warnings.filterwarnings('ignore')
# get_ipython().run_line_magic('matplotlib', 'inline')

# %% [markdown]
# ### 2. Loading Datasets

# %%
# Load the datasets
file = "xAPI-Edu-Data.csv"
df = pd.read_csv(file)

# %% [markdown]
# ### 3. Explore Datasets

# %%
df.head()


# %%
df.columns


# %%
df.shape


# %%
# Checking missing values
df.isna().sum().sum()

# %% [markdown]
# ### 4. EDA

# %%
# plt.title('Gender of the student', fontsize=22)
# sns.countplot(x=df.gender);



# %%
# bar = df['NationalITy'].value_counts().sort_values(ascending=False)
# ax = bar.plot(kind='barh', figsize=(15,8), color="blue", fontsize=13);
# ax.set_alpha(0.5)
# ax.set_title("Nationality of the students", fontsize=22)
# ax.set_ylabel("Nationality", fontsize=15);
# for i, v in enumerate(bar):
#     ax.text(v + 3, i + .10, str(v))
# plt.show()


# %%
# bar = df['PlaceofBirth'].value_counts().sort_values(ascending=False)
# ax = bar.plot(kind='barh', figsize=(15,8), color="blue", fontsize=13);
# ax.set_alpha(0.5)
# ax.set_title("Place of Birth", fontsize=22)
# ax.set_ylabel("Birt place", fontsize=15);
# for i, v in enumerate(bar):
#     ax.text(v + 3, i + .10, str(v))
# plt.show()


# %%
# df['Discussion'].hist();


# %%
# df['raisedhands'].hist();


# %%
# df['VisITedResources'].hist();


# %%
# df['AnnouncementsView'].hist();


# %%
# df['ParentschoolSatisfaction'].value_counts(normalize=True)


# %%
# df['ParentschoolSatisfaction'].value_counts()


# %%
# label 0 and 1
df['ParentschoolSatisfaction'].replace(['Bad','Good'],[1, 0],inplace=True)

# %% [markdown]
# ### Input and Target Columns

# %%
# Sperate the data, features and label
features_df = df.drop('ParentschoolSatisfaction', axis='columns')
labels_df = df.ParentschoolSatisfaction


# %%
#sample data for our pridict purpose
sample_data = features_df.sample(1)

# %% [markdown]
# ### 5. Encode categorical columns to one-hot vectors

# %%
# Encoder
numeric_cols = features_df.columns[features_df.dtypes != "object"].values
# print(numeric_cols)


# %%
categori_cols = features_df.columns[features_df.dtypes == "object"].values
# print(categori_cols)


# %%
features_df[categori_cols].nunique()


# %%
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoder.fit(features_df[categori_cols])


# %%
encoder.categories_


# %%
encoded_cols = list(encoder.get_feature_names(categori_cols))
# print(encoded_cols)


# %%
features_df[encoded_cols] = encoder.transform(features_df[categori_cols])


# %%
features_df.head()


# %%
features_df.shape

# %% [markdown]
# ### 6. Train Test Split

# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features_df, labels_df, stratify = labels_df, test_size=0.2, random_state=42)


# %%
# print(X_train.shape)
# print(X_test.shape)


# %%
y_train.value_counts(normalize=True)


# %%
y_test.value_counts(normalize=True)


# %%
numeric_cols = X_train.select_dtypes(include=np.number).columns.tolist()
categorical_cols = X_train.select_dtypes('category').columns.tolist()


# %%
X_train = X_train[numeric_cols]
X_test = X_test[numeric_cols]

# %% [markdown]
# ### Model training

# %%
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix


# %%
# Random forrest
model = RandomForestClassifier(random_state = 22, max_depth = 5, class_weight='balanced')
model.fit(X_train, y_train)
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)


# %%
train_acc = accuracy_score(y_train, train_pred)
test_acc = accuracy_score(y_test, test_pred)


# print(f"Train Accuracy = {train_acc} ")
# print(f"Test Accuracy = {test_acc} ")


# %%
# print(classification_report(y_train, train_pred, labels=[0, 1]))


# %%
# print(classification_report(y_test, test_pred, labels=[0, 1]))


# %%
from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test, test_pred)
# print(cm)
# accuracy_score(y_test, test_pred)


# %%
# plot_confusion_matrix(model, X_test, y_test)  
# plt.show()

# %% [markdown]
# ### Model Store

# %%
import pickle
filename = 'parent_satisfiction_model.pkl'
pickle.dump(model, open(filename, 'wb'))

# %% [markdown]
# ### Model load and pridict the value

# %%
# load the model from disk
train_model = pickle.load(open(filename, 'rb'))


# %%
from sklearn.preprocessing import OneHotEncoder

def pridict_the_result(input_data, model_name):
    
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


# %%
sample_data


# %%
pridict_the_result(sample_data, train_model)


