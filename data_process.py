import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def convert_to_categorical(df, method = 'manual'):
    """
    Convert categorical variables to numerical value.

    Parameters:
    df (DataFrame): The DataFrame to be transformed.
    method: The method used to convert categorical variables.

    Returns:
    DataFrame: The transformed DataFrame with categorical variables.
    """
    # Make a copy of the DataFrame
    # The DataFrame is passed by reference, not by value.
    df = df.copy()

    if method == 'encoder':
        label_encoder = LabelEncoder()
        categorical_columns = ['Age', 'Accessibility', 'EdLevel', 'Gender', 'MentalHealth', 
                           'MainBranch', 'Country']
        for column in categorical_columns:
            # Encode each categorical column
            df[column] = label_encoder.fit_transform(df[column].astype(str))
        return df
    
    if method == 'manual':
            # map categorical values to numerical
        df["Age"] = df["Age"].replace({"<35": 0, ">35": 1})
        df["Accessibility"] = df["Accessibility"].replace({"No": 0, "Yes": 1})
        df["EdLevel"] = df["EdLevel"].replace({
            "Other": 0,
            "NoHigherEd": 1,
            "Undergraduate": 2,
            "Master": 3,
            "PhD": 4,
        })
        df["Gender"] = df["Gender"].replace({"Man": 1, "Woman": 0,"NonBinary": 2})
        df["Accessibility"] = df["Accessibility"].replace({"No": 0, "Yes": 1})
        df["MentalHealth"] = df["MentalHealth"].replace({"No": 0, "Yes": 1})
        df["MainBranch"] = df["MainBranch"].replace({"NotDev": 0, "Dev": 1})
        return df
    
    if method == 'one-hot':
        categorical_columns = ['Age', 'Accessibility', 'EdLevel', 'Gender', 'MentalHealth', 
                           'MainBranch', 'Country']
        for column in categorical_columns:
            df = pd.get_dummies(df, columns=[column], drop_first=True, dummy_na=True)

        return df
    
def split_and_drop(df, version = 'default'):
    # X = df.drop(["Employed", "Country", "HaveWorkedWith",'ComputerSkills'], axis=1)
    if version == 'dropComputerSkills':
        X = df.drop(["Employed", "Country", "HaveWorkedWith",'ComputerSkills'], axis=1)
        
    if version == 'default':
        X = df.drop(["Employed", "Country", "HaveWorkedWith"], axis=1)
    
    if version == 'drop2':
        X = df.drop(["Employed", "Country", "HaveWorkedWith",'ComputerSkills','PreviousSalary'], axis=1)
    
    y = df["Employed"]
    return X, y

if __name__ == "__main__":
    pass