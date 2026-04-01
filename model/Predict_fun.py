import pandas as pd

def predict_price(model_dict,input_data:dict):
    model = model_dict["model"]
    features = model_dict["features"]
    
    df = pd.DataFrame([input_data])
    df = df[features]
    return model.predict(df)[0]