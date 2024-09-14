from django.shortcuts import render
import pickle
import os
def load_model(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The model file at {file_path} does not exist.")
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model
def homepage(request):
        return render(request,"main.html")
def breast(request):
     return render(request,"breast.html")
def faq(request):
        return render(request,"faqs.html")

def heart(request):
        return render(request,"heart.html")

    
def liver(request):
        return render(request,"liver.html")

    
def diabetes(request):
        return render(request,"diabetes.html")
def predictb(request):
    if request.method == 'POST':
        try:
            model_path = 'C:/Users/Pranshu Saini/Desktop/FINAL DOCPAT/DM PROJECT/docpat/breast_cancer_svm_model.pkl'
            breast_model = load_model(model_path)

            texture_mean = float(request.POST.get('texture_mean'))
            smoothness_mean = float(request.POST.get('smoothness_mean'))
            compactness_mean = float(request.POST.get('compactness_mean'))
            concave_points_mean = float(request.POST.get('concave_points_mean'))
            symmetry_mean = float(request.POST.get('symmetry_mean'))
            fractal_dimension_mean = float(request.POST.get('fractal_dimension_mean'))
            texture_se = float(request.POST.get('texture_se'))
            area_se = float(request.POST.get('area_se'))
            smoothness_se = float(request.POST.get('smoothness_se'))
            compactness_se = float(request.POST.get('compactness_se'))
            concavity_se = float(request.POST.get('concavity_se'))
            concave_points_se = float(request.POST.get('concave_points_se'))
            symmetry_se = float(request.POST.get('symmetry_se'))
            fractal_dimension_se =float(request.POST.get('fractal_dimension_se'))
            texture_worst = float(request.POST.get('texture_worst'))
            area_worst = float(request.POST.get('area_worst'))
            smoothness_worst = float(request.POST.get('smoothness_worst'))
            compactness_worst = float(request.POST.get('compactness_worst'))
            concavity_worst = float(request.POST.get('concavity_worst'))
            concave_points_worst = float(request.POST.get('concave_points_worst'))
            symmetry_worst = float(request.POST.get('symmetry_worst'))
            fractal_dimension_worst = float(request.POST.get('fractal_dimension_worst'))
            data = [ texture_mean, smoothness_mean, compactness_mean,
                     concave_points_mean, symmetry_mean, fractal_dimension_mean,  texture_se,
                     area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se,
                    fractal_dimension_se,  texture_worst,  area_worst, smoothness_worst,
                    compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]
            prediction_result = breast_model.predict([data])
            context = {
                'prediction_result': prediction_result[0]  
            }
            return render(request, 'predict.html', context)

        except Exception as e:
            return render(request, 'error.html', {'error': str(e)}) 
        
def predictd(request):
    if request.method == 'POST':
        try:
            model_path = 'C:/Users/Pranshu Saini/Desktop/FINAL DOCPAT/DM PROJECT/docpat/diabetes_model.pkl'
            diabetes_model = load_model(model_path)

            Pregnancies = float(request.POST.get('Pregnancies'))
            Glucose =float(request.POST.get('Glucose'))
            BloodPressure = float(request.POST.get('BloodPressure'))
            SkinThickness = float(request.POST.get('SkinThickness'))
            Insulin = float(request.POST.get('Insulin'))
            BMI = float(request.POST.get('BMI'))
            DiabetesPedigreeFunction = float(request.POST.get('DiabetesPedigreeFunction'))
            Age = float(request.POST.get('Age'))
            inputs = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, 
                   BMI, DiabetesPedigreeFunction, Age 
                   ]]
            prediction_result = diabetes_model.predict(inputs)


            context = {
                'prediction_result': prediction_result[0]  
            }
            return render(request, 'predict.html', context)

        except Exception as e:
            return render(request, 'error.html', {'error': str(e)}) 
def predictl(request):
    if request.method == 'POST':
        try:
            model_path = 'C:/Users/Pranshu Saini/Desktop/FINAL DOCPAT/DM PROJECT/docpat/liver_prediction.pkl'
            liver_model = load_model(model_path)
            age = float(request.POST.get('Age'))
            gender = float(request.POST.get('Gender'))
            total_bilirubin = float(request.POST.get('Total_Bilirubin'))
            direct_bilirubin = float(request.POST.get('Direct_Bilirubin'))
            alkaline_phosphotase = float(request.POST.get('Alkaline_Phosphotase'))
            alamine_aminotransferase = float(request.POST.get('Alamine_Aminotransferase'))
            aspartate_aminotransferase = float(request.POST.get('Aspartate_Aminotransferase'))
            total_proteins = float(request.POST.get('Total_Protiens'))
            albumin = float(request.POST.get('Albumin'))
            albumin_and_globulin_ratio = float(request.POST.get('Albumin_and_Globulin_Ratio'))

            inputs = [[age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, 
                   alamine_aminotransferase, aspartate_aminotransferase, total_proteins, 
                   albumin, albumin_and_globulin_ratio]]
        
            
            prediction_result =liver_model.predict(inputs)


            context = {
                'prediction_result': prediction_result[0]  
            }
            return render(request, 'predict.html', context)

        except Exception as e:
            return render(request, 'error.html', {'error': str(e)}) 
def predicth(request):
    if request.method == 'POST':
        try:
            model_path = 'C:/Users/Pranshu Saini/Desktop/FINAL DOCPAT/DM PROJECT/docpat/heart_disease_model.pkl'
            heart_model = float(load_model(model_path))
            age = float(request.POST.get('age'))
            sex = float(request.POST.get('sex'))
            cp = float(request.POST.get('cp'))
            trestbps = float(request.POST.get('trestbps'))
            chol = float(request.POST.get('chol'))
            fbs = float(request.POST.get('fbs'))
            restecg = float(request.POST.get('restecg'))
            thalach = float(request.POST.get('thalach'))
            exang = float(request.POST.get('exang'))
            oldpeak = float(request.POST.get('oldpeak'))
            slope = float(request.POST.get('slope'))
            ca = float(request.POST.get('ca'))
            thal = float(request.POST.get('thal'))
            inputs = [[age, sex,cp,trestbps, chol, fbs, restecg, 
                   thalach, exang, oldpeak, 
                   slope, ca,thal]]
            
            prediction_result = heart_model.predict(inputs)


            context = {
                'prediction_result': prediction_result[0] 
            }
            return render(request, 'predict.html', context)

        except Exception as e:
            return render(request, 'error.html', {'error': str(e)}) 

def diabetes_info(request):
    return render(request,"diabetes_info.html")
def breast_cancer_info(request):
    return render(request,'breast_cancer_info.html')
def heart_disease_info(request):
    return render(request,'heart_disease_info.html')
def liver_disease_info(request):
    return render(request,'liver_disease_info.html')