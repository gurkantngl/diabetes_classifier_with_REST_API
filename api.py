from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Modelinizi yükleyin
model = joblib.load("diabetes.pkl")

class Item(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.post("/predict")
async def predict_diabetes(item: Item):
    # Gelen verileri modele uygun formata getirin
    input_data = [
        item.Pregnancies,
        item.Glucose,
        item.BloodPressure,
        item.SkinThickness,
        item.Insulin,
        item.BMI,
        item.DiabetesPedigreeFunction,
        item.Age
    ]
    
    # Numpy array'e çevirin
    input_array = np.array([input_data])

    # Modeli kullanarak tahmin yapın
    prediction = model.predict(input_array)

    # Tahmin sonucunu döndürün
    return {"prediction": int(prediction[0])}

# Hızlı bir şekilde çalıştırmak için
# uvicorn dosyanizin_adi:app --reload
# komutunu kullanabilirsiniz.
