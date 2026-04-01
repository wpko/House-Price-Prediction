import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import shap

API_URL = "https://house-price-prediction-fastapi-7kxt.onrender.com/predict"

st.set_page_config(page_title = "House Price Predictor",page_icon="🏠",layout="wide")
st.title("🏠 House Price Prediction")
st.write("Enter house details below to predict price")

with st.form("prediction_form"):
    col1,col2 = st.columns(2)
    with col1:
        OverallQual = st.slider("Overall Quality(1-10)",1,10,7)
        GrLivArea = st.number_input("Living Area (square feet)",500,5000,1500)
        GarageCars = st.number_input("Garage Cars",0,5,2)
        GarageArea = st.number_input("Garage Area (square feet)",0,2000,500)
        TotalBsmtSF = st.number_input("Basement Area (square feet)",0,3000,800)
        
    with col2:
        FirstFlrSF = st.number_input("First Floor Area",0,3000,900)
        FullBath = st.number_input("Full Bathrooms",0,5,2)
        YearBuilt = st.number_input("Year Built",1900,2026,2005)
        YearRemodAdd = st.number_input("Remodeled Year",1900,2026,2010)
        LotArea = st.number_input("Lot Area",1000,20000,8500)
        
    submit = st.form_submit_button("Predict Price")
    
if submit:
    input_data = {
        "OverallQual":OverallQual,
        "GrLivArea":GrLivArea,
        "GarageCars":GarageCars,
        "GarageArea":GarageArea,
        "TotalBsmtSF":TotalBsmtSF,
        "FirstFlrSF":FirstFlrSF,
        "FullBath":FullBath,
        "YearBuilt":YearBuilt,
        "YearRemodAdd":YearRemodAdd,
        "LotArea":LotArea
    }
    try:
        response = requests.post(API_URL,json=input_data)
        if response.status_code == 200:
            result = response.json()
            if result['status'] == "Success!":
                price = result["predicted_price"]
                st.success("Prediction Successful!")
                st.markdown("### 💰 Estimated House Price")
                st.metric(label="Predicted Price",value=f"${price:,.2f}")
                
                st.markdown("### 📊 Your House Features")
                input_df = pd.DataFrame([input_data])
                st.bar_chart(input_df.T)
                
                st.markdown("### 📈 Price Comparison")
                avg_price = 180000
                chart_data = pd.DataFrame({
                    "Type":["Your House","Average House"],
                    "Price":[price,avg_price]
                })
                st.bar_chart(chart_data.set_index("Type"))
                
                st.markdown("### 🔍 Feature Importance")
                try:
                    model_dict = joblib.load("saved_model/model.pkl")
                    model = model_dict['model']
                    st.write(type(model_dict))   # should be dict
                    st.write(model_dict.keys())  # should show: model, features

                    model = model_dict["model"]
                    st.write(model)

                    lgb_model = model.named_steps["model"]
                    st.write(lgb_model)
                    importances = lgb_model.feature_importances_
                    features = model_dict['features']
                    df = pd.DataFrame({
                        "Feature":features,
                        "Importance":importances
                    }).sort_values(by="Importance",ascending=False)
                    fig,ax = plt.subplots()
                    ax.barh(df['Feature'],df['Importance'])
                    ax.invert_yaxis()
                    st.pyplot(fig)
                except:
                    st.warning("Feature importance not available")
                
            else:
                st.error(result["error"])
                
        else:
            st.error("API Error")
    except Exception as e:
        st.error(f"Connection Error: {e}")
