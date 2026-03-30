# 🏠 House Price Prediction App (FastAPI + Streamlit)

This project is a full-stack Machine Learning application that predicts house prices using a trained LightGBM model. It includes a FastAPI backend for prediction and a Streamlit frontend for user interaction and visualization.

---

## 🚀 Live Demo

- 🌐 Frontend (Streamlit): [Your Streamlit URL]
- ⚡ Backend API (FastAPI): [Your Render API URL]

---

## 📊 Features

- 🏠 House price prediction using ML model
- 📈 Interactive Streamlit UI
- 📊 Feature Importance visualization
- 🧠 SHAP Explainability (optional)
- 🔌 FastAPI REST API
- ☁️ Deployed on Render

---

## 🧠 Model Details

- Algorithm: LightGBM Regressor
- Features used:
  - OverallQual
  - GrLivArea
  - GarageCars
  - GarageArea
  - TotalBsmtSF
  - 1stFlrSF
  - FullBath
  - YearBuilt
  - YearRemodAdd
  - LotArea

---

## 🏗️ Project Structure

```
House-Price-API/
│
├── app/
│ └── main.py # FastAPI app
│
├── model/
│ ├── train.py # Training script
│ ├── Predict_fun.py # Prediction logic
│ └── saved_model/
│ └── model.pkl # Trained model
│
├── streamlit_app.py # Streamlit UI
├── requirements.txt
└── README.md
```
---

## ⚙️ Installation

1️⃣ Clone the repository
```
bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
2️⃣ Create virtual environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```
3️⃣ Install dependencies
```
pip install -r requirements.txt
```
▶️ Run Locally
```
Start FastAPI
uvicorn app.main:app --reload
```
👉 Open: http://127.0.0.1:8000/docs

Start Streamlit
streamlit run streamlit_app.py
📡 API Usage
```
POST /predict
Request Body (JSON)
{
  "OverallQual": 7,
  "GrLivArea": 1500,
  "GarageCars": 2,
  "GarageArea": 500,
  "TotalBsmtSF": 800,
  "FirstFlrSF": 900,
  "FullBath": 2,
  "YearBuilt": 2005,
  "YearRemodAdd": 2010,
  "LotArea": 8500
}
Response
{
  "predicted_price": 203925.23,
  "status": "success"
}
```

# 🧠 Explainability
```
📊 Feature Importance (LightGBM)
🧠 SHAP values (optional, enabled in UI)
☁️ Deployment
Backend: FastAPI deployed on Render
Frontend: Streamlit deployed on Render
💡 Future Improvements
📊 Interactive Plotly charts
🤖 Advanced SHAP visualization
📈 Model performance dashboard
🌍 Multi-dataset support
```

# 👨‍💻 Author

Wai Phyo Ko

##⭐ If you like this project

Give it a star ⭐ on GitHub!
