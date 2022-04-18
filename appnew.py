import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from flask import *

app = Flask(__name__,static_folder='')

@app.route('/',methods=['GET','POST'])

def processing():
    humidity=''
    temp=''
    soilmoisture=''
    ph=''
    waterlevel=''
    space=''
    crop_test=''

    if request.method == 'POST':
        humidity = int(request.form['humidity'])
        temp = float(request.form['temp'])
        soilmoisture = int(request.form['soilmoisture'])
        ph = float(request.form['ph'])
        waterlevel = int(request.form['waterlevel'])
        space = float(request.form['space'])

        testdata = [[humidity,temp,soilmoisture,ph,waterlevel,space]]
        from Model import classifier
        Y_test1 =  classifier.predict(testdata)[0]


        return jsonify({

            "suitable crop is": str(Y_test1)

        })






