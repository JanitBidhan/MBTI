from flask_ngrok import run_with_ngrok
from flask import Flask, render_template , request 
import os
import pandas as pd 
import numpy as np 
import flask
import pickle
from flask import Flask, render_template, request

import pickle
from nltk.stem import WordNetLemmatizer

from predict import predictMBTI

PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__, template_folder='webapp/website')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/')
def signUp():
    return render_template('question.html')


@app.route('/predict',methods = ['POST'])
def result():
 if request.method == 'POST':
  to_predict_list = request.form.to_dict()
  if to_predict_list['userChoice'] == 'Twitter':
    textType = 'twitter'
  else:
    textType = 'text'

  result = predictMBTI(to_predict_list[textType], textType)
  prediction = str(result)
 return render_template("prediction.html",prediction=prediction, link='#' + prediction.upper())

@app.route('/feedback',methods = ['POST'])
def feedback():
 if request.method == 'POST':
  to_predict_list = request.form.to_dict()
  to_predict_list=list(to_predict_list.values())
  result = ValuePredictor(to_predict_list)
  prediction = str(result)
 return render_template("prediction.html",prediction=prediction)

if __name__ == '__main__':

    class Lemmatizer(object):
        def __init__(self):
            self.lemmatizer = WordNetLemmatizer()
        def __call__(self, sentence):
            return [self.lemmatizer.lemmatize(word) for word in sentence.split() if len(word)>2]

    with open('models/vectorizer.pk', 'rb') as f:
        vectorizer = pickle.load(f)

    with open('models/model_linear_svc-Links.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('models/target-encoder.pk', 'rb') as f:
        labelEncoder = pickle.load(f)

    app.run()