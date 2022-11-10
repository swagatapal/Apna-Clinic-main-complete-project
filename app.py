from flask import Flask, render_template, jsonify, request, flash, redirect
#render_template helps to redirect to return the home page.
import pickle
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model


app = Flask(__name__)
#default page of our web-app

# prediction function for diabetes, breast cancer, heart, kidney, liver disease
def predict(values, dic):
    if len(dic) == 8:
        model = pickle.load(open('models\diabetes (1).pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 26:
        model = pickle.load(open('models/breast_cancer.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 13:
        model = pickle.load(open('models/heart.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 18:
        model = pickle.load(open('models/kidney.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 10:
        model = pickle.load(open('models/liver.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]

#it is the default page whenever the page load for first time
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact us')
def contact():
    return render_template('contact us.html')

#moving from home page to cancer introduction page
@app.route("/cancer introduction", methods=['GET', 'POST'])
def cancerintroPage():
    return render_template('breast cancer.html')

#moving from cancer intro page to cancer predict page where we have to fill all the details
@app.route("/cancer", methods=['GET', 'POST'])
def cancerPage():
    return render_template('breast cancer2.html')

#moving from home page to diabetes introduction page
@app.route("/diabetes introduction", methods=['GET', 'POST'])
def diabetesIntroPage():
    return render_template('diabetes.html')

#moving from diabetes intro  page to diabetes prediction page where we have to fill all the details
@app.route("/diabetes", methods=['GET', 'POST'])
def diabetesPage():
    return render_template('diabetes2.html')

@app.route("/heart introduction", methods=['GET', 'POST'])
def heartDiseaseIntroPage():
    return render_template('heart disease.html')

@app.route("/heart", methods=['GET', 'POST'])
def heartDiseasePage():
    return render_template('heart disease2.html')

@app.route("/kidney introduction", methods=['GET', 'POST'])
def kidneyDiseaseIntroPage():
    return render_template('kidney diseases.html')

@app.route("/kidney", methods=['GET', 'POST'])
def kidneyDiseasePage():
    return render_template('kidney diseases2.html')

@app.route("/liver introduction", methods=['GET', 'POST'])
def liverDiseaseIntroPage():
    return render_template('liver diseases.html')

@app.route("/liver", methods=['GET', 'POST'])
def liverDiseasePage():
    return render_template('liver diseases2.html')

#main logic and after prediction page it moves to the result (health condition) page
@app.route("/predict", methods = ['POST'])
def predictPage():
    # int_features = [float(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # return render_template('diabetes2.html',prediction_text='swagata '+"\nint features: "+str(to_predict_dict)+"\nfinal features: "+str(to_predict_list))
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = predict(to_predict_list, to_predict_dict)
    except:
        message = "Please enter valid Data"
        return render_template('diabetes2.html', prediction_text='Exception occur') 
    
    # return render_template('heart disease2.html',prediction_text='swagata '+"\npredict dict: "+str(to_predict_dict)+"\npredict list: "+str(to_predict_list)+"\nprediction value: "+str(pred))

    if(pred==0):
        return render_template('positive.html') # health condition is good
    else:
        return render_template('negative.html') # health condition is bad

#moving from home page to malaria introduction page
@app.route("/malaria introduction", methods=['GET', 'POST'])
def malariaDiseaseIntroPage():
    return render_template('malaria.html')
    
#moving from malaria intro page to malaria predict page
@app.route("/malaria", methods=['GET', 'POST'])
def malariaDiseasePage():
    return render_template('malaria2.html')

#main logic and after prediction page it moves to the result (health condition) page
@app.route("/malariapredict", methods = ['POST', 'GET'])
def malariapredictPage():
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image'])
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,3))
                img = img.astype(np.float64)
                model = load_model("models/malaria.h5")
                pred1 = np.argmax(model.predict(img)[0])
        except:
            message = "Please upload an correct Image"
            return render_template('malaria2.html', message = message)
    # return render_template('malaria2.html', prediction_text = pred1)

    if(pred1==0):
        return render_template('positive.html') # health condition is good
    else:
        return render_template('negative.html') # health condition is bad

#moving from home page to pneumonia introduction page
@app.route("/pneumonia introduction", methods=['GET', 'POST'])
def pneumoniaDiseaseIntroPage():
    return render_template('pneumonia.html')

#moving from pneumonia intro page to pneumonia predict page
@app.route("/pneumonia", methods=['GET', 'POST'])
def pneumoniaDiseasePage():
    return render_template('pneumonia2.html')

#main logic and after prediction page it moves to the result (health condition) page
@app.route("/pneumoniapredict", methods = ['POST', 'GET'])
def pneumoniapredictPage():
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image']).convert('L')
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,1))
                img = img / 255.0
                model = load_model("models/pneumonia.h5")
                pred2 = np.argmax(model.predict(img)[0])
        except:
            message = "Please upload an Image"
            return render_template('pneumonia2.html', message = message)
    # return render_template('pneumonia2.html', prediction_text = pred2)

    if(pred2==0):
        return render_template('positive.html') #health condion is good
    else:
        return render_template('negative.html') # health condition is bad

if __name__ == "__main__":
    app.run(debug=True)