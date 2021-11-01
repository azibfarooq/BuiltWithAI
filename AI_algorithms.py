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