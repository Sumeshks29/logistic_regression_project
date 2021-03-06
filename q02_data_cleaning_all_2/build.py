# %load q02_data_cleaning_all_2/build.py
# Default Imports
import pandas as pd
import numpy as np
from greyatomlib.logistic_regression_project.q02_data_cleaning_all.build import data_cleaning
from greyatomlib.logistic_regression_project.q01_outlier_removal.build import outlier_removal

loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
loan_data = loan_data.drop('Loan_ID', 1)
loan_data = outlier_removal(loan_data)
X, y, X_train, X_test, y_train, y_test = data_cleaning(loan_data)


# Write your solution here :
def data_cleaning_2(X_train, X_test, y_train, y_test):
    cols = X_train.columns
    num_cols = X_train._get_numeric_data().columns
    cat_cols = list(set(cols) - set(num_cols))
    X_train=pd.get_dummies(X_train,columns=cat_cols, drop_first=True)
    X_test=pd.get_dummies(X_test,columns=cat_cols, drop_first=True)
    
    for i in num_cols:
        X_train[i] = np.sqrt(X_train[i])
        X_test[i] = np.sqrt(X_test[i])
    return X_train, X_test, y_train, y_test


