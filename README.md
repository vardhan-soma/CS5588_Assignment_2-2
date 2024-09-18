# CS5588_Assignment_2-2

## Diabetes Predictor Application

This project aims to predict whether an individual is prone to diabetes using a machine learning model based on 21 health and lifestyle-related features. The application is built using Streamlit for the frontend and MongoDB for storing predictions.

## Features

The application predicts the likelihood of diabetes using a deep learning model. The prediction output is a binary result:

1: Prone to diabetes and 0: Non-diabetic

## Key Features:

1. User-friendly Streamlit interface for collecting user health data.
2. Real-time diabetes prediction using a pre-trained deep learning model.
3. MongoDB integration for saving user inputs and prediction results.

## Technology Stack

1. Keras: For building and training the deep learning model.
2. Streamlit: For the web application interface.
3. MongoDB: For storing user data and prediction outcomes.
4. NumPy & Pandas: For data handling and processing.

## Input Features

The model utilizes the following 21 features to predict the risk of diabetes:

1.	HighBP: High blood pressure
2.	HighChol: High cholesterol
3.	CholCheck: Regular cholesterol check
4.	BMI: Body Mass Index
5.	Smoker: Smoking habits
6.	Stroke: History of stroke
7.	HeartDiseaseorAttack: History of heart disease or heart attack
8.	PhysActivity: Physical activity level
9.	Fruits: Frequency of fruit consumption
10.	Veggies: Frequency of vegetable consumption
11.	HvyAlcoholConsump: Heavy alcohol consumption
12.	AnyHealthcare: Access to healthcare
13.	NoDocbcCost: Skipping doctor visits due to cost
14.	GenHlth: General health condition
15.	MentHlth: Mental health days
16.	PhysHlth: Physical health days
17.	DiffWalk: Difficulty in walking
18.	Sex: Gender
19.	Age: Age of the individual
20.	Education: Education level
21.	Income: Income level

## How to Run the Application

1. Install Dependencies:
pip install -r requirements.txt
2. Run the Streamlit App:
streamlit run app.py
3. MongoDB Setup:
Ensure MongoDB is running and connected to store predictions and update the MongoDB connection string in the code if needed.

## Model Integration

The deep learning model (best_model_a6_b3.h5) is loaded in app.py using Keras’ load_model function. This model is designed to predict the likelihood of diabetes based on 21 structured input features. When the user submits new data through the Streamlit interface, the model processes the input and generates a prediction in real-time.

## Prediction Output

1. Prone to diabetes (1): The model predicts that the individual is at risk of developing diabetes based on their input data.
2. Non-diabetic (0): The model predicts that the individual is not at risk of diabetes.

## Project Goals and Future Enhnacement
The Diabetes Predictor Application is a prototype designed to predict an individual’s risk of being prone to diabetes using a deep learning model built with Keras and integrated into a Streamlit interface. The model processes 21 structured input features, including BMI, physical activity, age, and healthcare access, to generate a real-time prediction indicating whether the user is at risk for diabetes (1 for prone, 0 for non-diabetic). The application allows users to input health-related data and instantly receive feedback, with all inputs and predictions stored in a MongoDB database for future analysis. Future enhancements will focus on reducing the number of features to streamline the user experience and improve model efficiency.


