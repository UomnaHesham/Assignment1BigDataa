import pandas as pd
import numpy as np
from load import load_dataset  # Ensure `load_dataset` is defined in load.py

def data_transformation(df):
    """Perform data transformation tasks."""
    df['FamilySize'] = df['SibSp'] + df['Parch']
    return df

def data_cleaning(df):
    """Perform data cleaning tasks."""
    df['Age'].fillna(df['Age'].mean(), inplace=True)

    # Fill missing Survived values based on the distribution of existing values
    survived_counts = df['Survived'].value_counts()
    distribution = survived_counts / survived_counts.sum()
    null_count = df['Survived'].isnull().sum()
    null_indices = df[df['Survived'].isnull()].index
    missing_survived = np.random.choice(distribution.index, null_count, p=distribution)
    df.loc[null_indices, 'Survived'] = missing_survived

    # Fill missing Fare values with mean
    df['Fare'].fillna(df['Fare'].mean(), inplace=True)

    # Fill missing Embarked values with the first non-null value
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].values[0])

    return df

def data_reduction(df):
    """Perform data reduction tasks."""
    columns_to_drop = ['PassengerId', 'Name', 'AgeGroup', 'FareGroup', 
                        'Sex', 'Embarked', 'Cabin', 'Ticket']
    df.drop(columns=columns_to_drop, inplace=True, errors='ignore')
    return df

def data_discretization(df):
    """Perform data discretization tasks."""
    # Age Binning
    bins = [df['Age'].min() - 1, 10, 20, 30, 40, 50, 60, df['Age'].max() + 1]
    labels = ['0-10 years', '11-20 years', '21-30 years', '31-40 years', 
              '41-50 years', '51-60 years', '61+ years']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

    # Fare Binning
    fare_bins = [df['Fare'].min() - 1, 20, 40, 60, 80, 100, df['Fare'].max() - 1]
    fare_labels = ['0-20', '21-40', '41-60', '61-80', '81-100', '100+']
    df['FareGroup'] = pd.cut(df['Fare'], bins=fare_bins, labels=fare_labels)

    # Factorize categorical columns
    df['IntAgeGroup'] = pd.factorize(df['AgeGroup'])[0]
    df['IntFareGroup'] = pd.factorize(df['FareGroup'])[0]
    df['IntSex'] = pd.factorize(df['Sex'])[0]
    df['IntEmbarked'] = pd.factorize(df['Embarked'])[0]
    df['IntTicket'] = pd.factorize(df['Ticket'])[0]

    return df

def dpre(df):
    """Main function to preprocess the dataset."""
    print("Starting data preprocessing...")
    df = data_transformation(df)
    print("Data transformation completed.")

    df = data_cleaning(df)
    print("Data cleaning completed.")

    df = data_discretization(df)
    print("Data discretization completed.")

    df = data_reduction(df)
    print("Data reduction completed.")

    df.to_csv("res_dpre.csv", index=False)
    print("Preprocessed data saved as res_dpre.csv.")
    return df

if __name__ == "__main__":
    # Load dataset and process it
    df = load_dataset("dataset.csv")  
    df = dpre(df)
