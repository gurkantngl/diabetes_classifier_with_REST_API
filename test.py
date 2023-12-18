from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_diabetic():
    data = {
        "Pregnancies": 2,
        "Glucose": 130,
        "BloodPressure": 75,
        "SkinThickness": 30,
        "Insulin": 100,
        "BMI": 25,
        "DiabetesPedigreeFunction": 0.6,
        "Age": 35,
        "New_Glucose_Class_Prediabetes": False,
        "New_BMI_Range_Healty": True,
        "New_BMI_Range_Overweight": False,
        "New_BMI_Range_Obese": False,
        "New_BloodPressure_HS1": False,
        "New_BloodPressure_HS2": False,
        "New_SkinThickness_1": True,
    }

    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json()["predicted_outcome"] == 1
    assert response.json()["label"] == "Diabetic"

def test_predict_non_diabetic():
    data = {
        "Pregnancies": 1,
        "Glucose": 90,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 80,
        "BMI": 22,
        "DiabetesPedigreeFunction": 0.4,
        "Age": 25,
        "New_Glucose_Class_Prediabetes": False,
        "New_BMI_Range_Healty": True,
        "New_BMI_Range_Overweight": False,
        "New_BMI_Range_Obese": False,
        "New_BloodPressure_HS1": False,
        "New_BloodPressure_HS2": False,
        "New_SkinThickness_1": False,
    }

    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json()["predicted_outcome"] == 1
    assert response.json()["label"] == "Diabetic"

def test_invalid_input():
    data = {
        "Glucose": 100,
        "BloodPressure": 70,
        "SkinThickness": 25,
        "Insulin": 75,
        "BMI": 23,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 30,
        "New_Glucose_Class_Prediabetes": False,
        "New_BMI_Range_Healty": True,
        "New_BMI_Range_Overweight": False,
        "New_BMI_Range_Obese": False,
        "New_BloodPressure_HS1": False,
        "New_BloodPressure_HS2": False,
        "New_SkinThickness_1": False,
    }

    response = client.post("/predict", json=data)
    assert response.status_code == 422


def test_edge_cases():
    data_min = {
        "Pregnancies": 0,
        "Glucose": 50,
        "BloodPressure": 30,
        "SkinThickness": 0,
        "Insulin": 0,
        "BMI": 10,
        "DiabetesPedigreeFunction": 0,
        "Age": 1,
        "New_Glucose_Class_Prediabetes": False,
        "New_BMI_Range_Healty": False,
        "New_BMI_Range_Overweight": False,
        "New_BMI_Range_Obese": False,
        "New_BloodPressure_HS1": False,
        "New_BloodPressure_HS2": False,
        "New_SkinThickness_1": False,
    }

    response_min = client.post("/predict", json=data_min)
    assert response_min.status_code == 200
    assert response_min.json()["predicted_outcome"] == 0 

    data_max = {
        "Pregnancies": 99,
        "Glucose": 300,
        "BloodPressure": 200,
        "SkinThickness": 99,
        "Insulin": 900,
        "BMI": 50,
        "DiabetesPedigreeFunction": 2.5,
        "Age": 100,
        "New_Glucose_Class_Prediabetes": True,
        "New_BMI_Range_Healty": True,
        "New_BMI_Range_Overweight": True,
        "New_BMI_Range_Obese": True,
        "New_BloodPressure_HS1": True,
        "New_BloodPressure_HS2": True,
        "New_SkinThickness_1": True,
    }

    response_max = client.post("/predict", json=data_max)
    assert response_max.status_code == 200
    assert response_max.json()["predicted_outcome"] == 1 
