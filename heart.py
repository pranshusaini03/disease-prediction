from flask import Flask, render_template, request
import pickle

heart= Flask(__name__)

# Function to load the model from the pickle file
def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

# Load the liver disease prediction model
liver_model = load_model('C:/Users/Dell/OneDrive/Desktop/DM PROJECT/heart_disease_model.pkl')

# Route for the home page
@heart.route('/')
def home():
    return render_template('heart.html')

# Route for prediction
@heart.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = float(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])

        # Make predictions
        inputs = [[age, sex,cp,trestbps, chol, fbs, restecg, 
                   thalach, exang, oldpeak, 
                   slope, ca,thal]]
        
        # Example prediction (replace this with your actual prediction logic)
        prediction = liver_model.predict(inputs)
        
        return render_template('predict.html', prediction=prediction[0])

if __name__ == '__main__':
    heart.run(debug=True)
