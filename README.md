# 🏗️ Bridge Load Predictor

This project uses a trained Artificial Neural Network (ANN) built with TensorFlow to predict the **maximum load capacity (in tons)** of a bridge based on key design and condition features.

It includes:
- A Jupyter notebook for data preprocessing, model training, and evaluation.
- A saved model and preprocessing pipeline.
- A deployed **Streamlit web app** for user interaction and real-time predictions.

---

## 🚀 Try the Live App

👉 [Click here to use the Streamlit App](https://<your-streamlit-deployment-link>)

---

## 📊 Features

- Predicts **Max Load (Tons)** based on:
  - Span (ft)
  - Deck Width (ft)
  - Age (Years)
  - Number of Lanes
  - Material (Steel, Concrete, Composite)
  - Condition Rating (1–5)

- Uses a fully trained TensorFlow model with:
  - L2 Regularization
  - Dropout
  - Early Stopping

---

## 📂 Files

- `app.py`: The Streamlit web app
- `tf_bridge_model.h5`: The trained ANN model
- `preprocessing_pipeline.pkl`: Scikit-learn pipeline for preprocessing new inputs
- `requirements.txt`: Python dependencies
- `README.md`: You're reading it!

---

## 🧠 Model Training

You can retrain the model using the `lab_11_bridge_data.csv` dataset and the included Jupyter Notebook steps. The model is trained with:

- One-hot encoding for materials
- Standard scaling for numeric features
- EarlyStopping and dropout layers
- Final regression layer with linear activation

---

## 🛠️ Setup Instructions

### 🔧 Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/bridge-load-predictor.git
   cd bridge-load-predictor
