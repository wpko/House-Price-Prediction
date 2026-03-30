import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

import lightgbm as lgb

os.makedirs("saved_model",exist_ok=True)
#1. Load data
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
#2.Select important feature
features = [
    "OverallQual",
    "GrLivArea",
    "GarageCars",
    "GarageArea",
    "TotalBsmtSF",
    "1stFlrSF",
    "FullBath",
    "YearBuilt",
    "YearRemodAdd",
    "LotArea"
]
target = "SalePrice"

#3. Prepare Data
X = train[features]
y = train[target]

X_test_final = test[features]

#4. Handle Missing values
X = X.fillna(0)
X_test_final = X_test_final.fillna(0)

#5. Train/Test Split (for evaluate only)
X_train,X_val,y_train,y_val = train_test_split(X,y,test_size=0.2,random_state=42)

#6. Pipeline
pipeline = Pipeline([
    ("scaler",StandardScaler()),
    ("model",lgb.LGBMRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=6
    ))
])

#7. Train
pipeline.fit(X_train,y_train)

#8.Evaluate
preds = pipeline.predict(X_val)
mae = mean_absolute_error(y_val,preds)
print(f"MAE: {mae:.2f}")

#9. Train on Full data
pipeline.fit(X,y)
#10. Predict on test.csv
test_preds = pipeline.predict(X_test_final)

joblib.dump({
    "model":pipeline,
    "features":features
},"saved_model/model.pkl")
print('Model Saved')