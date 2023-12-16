from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Eğitilmiş modelinizi buraya yükleyin
model = pickle.load(open("LGBM_model.pkl", "rb"))

app = FastAPI(title="Diyabet Teşhis API'si")


class PatientData(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float
    New_Glucose_Class_Prediabetes : bool
    New_BMI_Range_Healty : bool   
    New_BMI_Range_Overweight : bool   
    New_BMI_Range_Obese : bool   
    New_BloodPressure_HS1 : bool   
    New_BloodPressure_HS2 : bool   
    New_SkinThickness_1 : bool
    


@app.post("/predict")
async def predict(data: PatientData):
    features = [
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age,
        data.New_Glucose_Class_Prediabetes,
        data.New_BMI_Range_Healty,   
        data.New_BMI_Range_Overweight,   
        data.New_BMI_Range_Obese,   
        data.New_BloodPressure_HS1,   
        data.New_BloodPressure_HS2,   
        data.New_SkinThickness_1,
    ]

    prediction = model.predict([features])[0]

    if prediction == 1:
        label = "Diabetic"
    else:
        label = "Non-diabetic"

    return {
        "predicted_outcome": int(prediction),
        "label": label,
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000)
