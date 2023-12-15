from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Eğitilmiş modelinizi buraya yükleyin
model = pickle.load(open("diabetes.pkl", "rb"))

app = FastAPI(title="Diyabet Teşhis API'si")


class PatientData(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    


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
