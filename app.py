import streamlit as st
import numpy as np
from pymongo import MongoClient
from keras.models import load_model

# Load your saved best model
model = load_model('/Users/sreevardhanreddysoma/Desktop/DS_Capstone/best_model_a6_b3.h5')  # Replace with your actual model filename

# MongoDB connection details
MONGO_URI = "mongodb+srv://ssfwk:guest@cluster0.yhab1.mongodb.net/"
DATABASE_NAME = "diabetes_data"
COLLECTION_NAME = "collection1"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Set up the Streamlit app
st.title("Diabetes Predictor")

# Collect user inputs for the features used in the model
high_bp = st.selectbox("Do you have high blood pressure?", options=["Yes", "No"])
high_bp = 1 if high_bp == "Yes" else 0

high_chol = st.selectbox("Do you have high cholesterol?", options=["Yes", "No"])
high_chol = 1 if high_chol == "Yes" else 0

chol_check = st.selectbox("Have you checked your cholesterol in the last year?", options=["Yes", "No"])
chol_check = 1 if chol_check == "Yes" else 0

bmi = st.number_input("Enter your BMI", value=0.0)

smoker = st.selectbox("Do you smoke?", options=["Yes", "No"])
smoker = 1 if smoker == "Yes" else 0

stroke = st.selectbox("Have you had a stroke?", options=["Yes", "No"])
stroke = 1 if stroke == "Yes" else 0

heart_disease = st.selectbox("Have you had a heart disease or attack?", options=["Yes", "No"])
heart_disease = 1 if heart_disease == "Yes" else 0

phys_activity = st.selectbox("Do you engage in physical activity?", options=["Yes", "No"])
phys_activity = 1 if phys_activity == "Yes" else 0

fruits = st.selectbox("Do you eat fruits regularly?", options=["Yes", "No"])
fruits = 1 if fruits == "Yes" else 0

veggies = st.selectbox("Do you eat vegetables regularly?", options=["Yes", "No"])
veggies = 1 if veggies == "Yes" else 0

hvy_alcohol = st.selectbox("Do you consume heavy alcohol?", options=["Yes", "No"])
hvy_alcohol = 1 if hvy_alcohol == "Yes" else 0

any_healthcare = st.selectbox("Do you have access to healthcare?", options=["Yes", "No"])
any_healthcare = 1 if any_healthcare == "Yes" else 0

no_docbc_cost = st.selectbox("Did you avoid medical care due to cost?", options=["Yes", "No"])
no_docbc_cost = 1 if no_docbc_cost == "Yes" else 0

gen_health = st.selectbox("How would you rate your general health?", options=["Excellent", "Very Good", "Good", "Fair", "Poor"])
gen_health_map = {"Excellent": 5, "Very Good": 4, "Good": 3, "Fair": 2, "Poor": 1}
gen_health = gen_health_map[gen_health]

ment_health = st.number_input("How many days in the past month was your mental health not good?", value=0)

phys_health = st.number_input("How many days in the past month was your physical health not good?", value=0)

diff_walk = st.selectbox("Do you have difficulty walking?", options=["Yes", "No"])
diff_walk = 1 if diff_walk == "Yes" else 0

sex = st.selectbox("Select your gender", options=["Male", "Female"])
sex = 1 if sex == "Male" else 0

age = st.number_input("Enter your age", value=0)

education = st.selectbox("Select your education level", options=["No High School", "High School", "Some College", "College Graduate", "Advanced Degree"])
education_map = {"No High School": 0, "High School": 1, "Some College": 2, "College Graduate": 3, "Advanced Degree": 4}
education = education_map[education]

income = st.selectbox("Select your income range", options=["< 25K", "25-50K", "50-75K", "> 75K"])
income_map = {"< 25K": 0, "25-50K": 1, "50-75K": 2, "> 75K": 3}
income = income_map[income]

# Prepare input data for the model (20 features)
input_features = np.array([[high_bp, high_chol, chol_check, bmi, smoker, stroke, heart_disease, 
                            phys_activity, fruits, veggies, hvy_alcohol, any_healthcare, no_docbc_cost, 
                            gen_health, ment_health, phys_health, diff_walk, sex, age, education, income]])

# Ensure input shape matches the model's expectations
if st.button("Predict"):
    prediction = model.predict(input_features)
    result = "Prone to Diabetes" if round(prediction[0][0]) == 1 else "Non-Diabetic"
    st.write(f"Prediction: {result}")

    # Upload the prediction to MongoDB
    collection.insert_one({
        "high_bp": high_bp,
        "high_chol": high_chol,
        "chol_check": chol_check,
        "bmi": bmi,
        "smoker": smoker,
        "stroke": stroke,
        "heart_disease": heart_disease,
        "phys_activity": phys_activity,
        "fruits": fruits,
        "veggies": veggies,
        "hvy_alcohol": hvy_alcohol,
        "any_healthcare": any_healthcare,
        "no_docbc_cost": no_docbc_cost,
        "gen_health": gen_health,
        "ment_health": ment_health,
        "phys_health": phys_health,
        "diff_walk": diff_walk,
        "sex": sex,
        "age": age,
        "education": education,
        "income": income,
        "prediction": round(prediction[0][0])
    })
    st.write("Prediction saved to the database.")