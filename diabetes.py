from flask import Flask, render_template, request
import pickle

diabetes= Flask(__name__)

# Function to load the model from the pickle file
def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

# Load the liver disease prediction model
liver_model = load_model('C:/Users/Dell/OneDrive/Desktop/DM PROJECT/diabetes_model.pkl')

# Route for the home page
@diabetes.route('/')
def home():
    return render_template('templates/diabetes.html')

# Route for prediction
@diabetes.route('templates/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        Pregnancies = float(request.form['Pregnancies'])
        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = float(request.form['Age'])
        # Make predictions
        inputs = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, 
                   BMI, DiabetesPedigreeFunction, Age 
                   ]]
        
        # Example prediction (replace this with your actual prediction logic)
        prediction = liver_model.predict(inputs)
        
        return render_template('predict.html', prediction=prediction[0])

if __name__ == '__main__':
    diabetes.run(debug=True)
