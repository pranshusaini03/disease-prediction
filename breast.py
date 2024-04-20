from flask import Flask, render_template, request
import pickle

breast = Flask(__name__)

# Function to load the model from the pickle file
def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

# Load the breast cancer prediction model
breast_model = load_model('C:/Users/Dell/OneDrive/Desktop/DM PROJECT/breast_cancer_svm_model.pkl')

# Route for the home page
@breast.route('/')
def home():
    return render_template('breast.html')

# Route for prediction
@breast.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        texture_mean = float(request.form['texture_mean'])
        smoothness_mean = float(request.form['smoothness_mean'])
        compactness_mean = float(request.form['compactness_mean'])
        concave_points_mean = float(request.form['concave points_mean'])
        symmetry_mean = float(request.form['symmetry_mean'])
        fractal_dimension_mean = float(request.form['fractal_dimension_mean'])
        texture_se = float(request.form['texture_se'])
        area_se = float(request.form['area_se'])
        smoothness_se = float(request.form['smoothness_se'])
        compactness_se = float(request.form['compactness_se'])
        concavity_se = float(request.form['concavity_se'])
        concave_points_se = float(request.form['concave points_se'])
        symmetry_se = float(request.form['symmetry_se'])
        fractal_dimension_se = float(request.form['fractal_dimension_se'])
        texture_worst = float(request.form['texture_worst'])
        area_worst = float(request.form['area_worst'])
        smoothness_worst = float(request.form['smoothness_worst'])
        compactness_worst = float(request.form['compactness_worst'])
        concavity_worst = float(request.form['concavity_worst'])
        concave_points_worst = float(request.form['concave points_worst'])
        symmetry_worst = float(request.form['symmetry_worst'])
        fractal_dimension_worst = float(request.form['fractal_dimension_worst'])
        
        # Make predictions
        inputs = [[texture_mean, smoothness_mean, compactness_mean, concave_points_mean, symmetry_mean, 
                   fractal_dimension_mean, texture_se, area_se, 
                   smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                   texture_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst,
                   symmetry_worst, fractal_dimension_worst]]
        
        # Example prediction (replace this with your actual prediction logic)
        prediction = breast_model.predict(inputs)
        
        return render_template('predict.html', prediction=prediction[0])

if __name__ == '__main__':
    breast.run(debug=True)
