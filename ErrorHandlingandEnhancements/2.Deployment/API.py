import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle,os
import sys

sys.path.append(r"C:\Users\sn27506\Learnings\FSDSession1Assignment1\ErrorHandlingandEnhancements")

from common_util.config import modeloutput
from common_util.utility import *
from common_util.features import *


# Create flask app
flask_app = Flask(__name__,template_folder='templates')
model = pickle.load(open(modeloutput, "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [x for x in request.form.values()]
    float_features = list(filter(None, float_features))
    float_features = [float(x) for x in float_features]
    rawinput = [np.array(float_features)]
    input_feats = [x for x in request.form.keys()]
    input_data = dict(zip(input_feats,float_features))
    # print(input_data)
    #Exception Handling from utility.py
    msg = exceptions(raw_features=input_data)
    if  msg[0] == 1:
        return render_template("index.html", prediction_text = msg[1])
    
    #Feature Enginnering from feature.py
    input_data['log_Peatal_Width'] = process(input_data['Petal_Width'])
    if msg[0] == 0:
        features = [np.array([i for i in input_data.values()])]
        prediction = model.predict(features)
        return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))

    return render_template("index.html", prediction_text = "Incorrect {}".format([k for k, v in check_list.items() if not v]))
if __name__ == "__main__":
    flask_app.run(debug=True)