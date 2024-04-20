from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Function to load the model from the pickle file
def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

# Load the liver disease prediction model
liver_model = load_model('C:/Users/Dell/OneDrive/Desktop/DM PROJECT/liver_prediction.pkl')

# Route for the home page
@app.route('/')
def home():
    return render_template('liver.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        age = float(request.form['Age'])
        gender = float(request.form['Gender'])
        total_bilirubin = float(request.form['Total_Bilirubin'])
        direct_bilirubin = float(request.form['Direct_Bilirubin'])
        alkaline_phosphotase = float(request.form['Alkaline_Phosphotase'])
        alamine_aminotransferase = float(request.form['Alamine_Aminotransferase'])
        aspartate_aminotransferase = float(request.form['Aspartate_Aminotransferase'])
        total_proteins = float(request.form['Total_Protiens'])
        albumin = float(request.form['Albumin'])
        albumin_and_globulin_ratio = float(request.form['Albumin_and_Globulin_Ratio'])

        # Make predictions
        inputs = [[age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, 
                   alamine_aminotransferase, aspartate_aminotransferase, total_proteins, 
                   albumin, albumin_and_globulin_ratio]]
        
        # Example prediction (replace this with your actual prediction logic)
        prediction = liver_model.predict(inputs)
        
        return render_template('predict.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
