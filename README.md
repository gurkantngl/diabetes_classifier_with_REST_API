# Diabetes Classifier API

This API predicts the likelihood of diabetes using input data with a classification model.

## Getting Started

First, install the required libraries:

```bash
pip install -r requirements.txt

Run the API:

uvicorn main:app --reload


Test the API:

curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d
'{"Pregnancies": 1,
  "Glucose": 106,
  "BloodPressure": 70,
  "SkinThickness": 26,
  "Insulin": 135,
  "BMI": 34.2,
  "DiabetesPedigreeFunction": 0.142,
  "Age": 22,
  "New_Glucose_Class_Prediabetes": false,
  "New_BMI_Range_Healty": true,
  "New_BMI_Range_Overweight": false,
  "New_BMI_Range_Obese": false,
  "New_BloodPressure_HS1": false,
  "New_BloodPressure_HS2": false,
  "New_SkinThickness_1": false}'



Review the Results:
{
  "predicted_outcome": 0,
  "label": "Non-diabetic"
}
