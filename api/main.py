from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
from model.Predict_fun import predict_price

app = FastAPI(title="House Price Prediction API")

class HouseFeatures(BaseModel):
    OverallQual: int = Field(..., example=7, description="Overall material and finish QUALITY (1 = Poor, 10 = Excellent)")
    GrLivArea: float = Field(..., example=1500, description="Above Ground living area in square feet")
    GarageCars: int = Field(..., example=2, description="Size of garage in car capacity")
    GarageArea: float = Field(..., example=500, description="Size of garage in square feet")
    TotalBsmtSF: float = Field(..., example=800, description="Total Basement area in square feet")
    FirstFlrSF: float = Field(..., example=900, description="First Floor living area in square feet")
    FullBath: int = Field(..., example=2, description="Number of full bathrooms")
    YearBuilt: int = Field(..., example=2005, description="Original Construction Year")
    YearRemodAdd: int = Field(..., example=2010, description="Remodelling Year (if any)")
    LotArea: float = Field(..., example=8500, description="Lot size in square feet")

#Load model once
model_dict = joblib.load("saved_model/model.pkl")

@app.get('/')
def home():
    return {"message":"House Price Prediction API is running"}

@app.post("/predict")
def predict(data:HouseFeatures):
    try:
        #convert to dict
        input_data = data.dict()
        input_data["1stFlrSF"] = input_data.pop('FirstFlrSF')
        price = predict_price(model_dict,input_data)
        return{
            "predicted_price":price,
            "status":"Success!"
        }
    except Exception as e:
        return{
            "error":str(e),
            "status": "Failed!"
        }