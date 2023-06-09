# -*- coding: utf-8 -*-
"""
@author: Rameswar
"""

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from joblib import dump, load
import json


app = FastAPI()

class model_input(BaseModel):
    
    gender : int
    age : float
    hypertension : int
    heart_disease : int
    ever_married : int
    work_type : int
    Residence_type : int
    avg_glucose_level : float
    bmi : float
    smoking_status : int
    
     
        
# loading the saved model
knn = joblib.load('knn.sav')

@app.post('/knn')
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    gender = input_dictionary['gender']
    age = input_dictionary['age']
    hypertension = input_dictionary['hypertension']
    heart_disease = input_dictionary['heart_disease']
    ever_married = input_dictionary['ever_married']
    work_type = input_dictionary['work_type']
    Residence_type = input_dictionary['Residence_type']
    avg_glucose_level = input_dictionary['avg_glucose_level']
    bmi = input_dictionary['bmi']
    smoking_status = input_dictionary['smoking_status']
    
    
    
    input_list = [gender, age, hypertension,heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi,smoking_status]
    
    prediction = knn.predict_proba([input_list])
    
    print(prediction)

#python -m uvicorn KNN:app --reload




