# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:23:02 2022

@author: gouthaman
"""
import warnings  # helps to remove warnings 

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import dabl as db
import numpy as np

import joblib 

from xgboost import XGBRFRegressor

url = "C:\\Users\\gouthaman\\Desktop\\WildBlueberryPollinationSimulationData.csv"

df = pd.read_csv(url)

#print(df.head())

features=['seeds', 'fruitset', 'osmia', 'fruitmass', 'RainingDays']
xgbref =joblib.load("F://TMLC/BlueBerry Prediction//XGBRegressor1.pkl")
print(xgbref.get_booster().feature_names)

def predict_yield(attributes : np.ndarray ):
    pred=xgbref.predict(attributes)
    print("Yield Predict")
    return pred[0]
