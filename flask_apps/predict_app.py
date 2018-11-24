# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:48:03 2018

@author: ali
"""

from keras.models import load_model
from keras.models import print_function
from flask import Flask, request
import tensorflow as tf
import flask
import numpy as np 
from numpy import array
import pandas as pd 
from flask import jsonify
import json


#loading model 
model_ = load_model("./atr_subset.h5")
graph = tf.get_default_graph()     
model_.summary()

x=1
Age = 30 
MartialStatus = 1 
Gender =2 

#testing model prediction 
Xnew = array([[48,1,1]])
Attrition_predict = model_.predict(Xnew)
Attrition_predict

input_ = pd.read_csv("../input.csv")
pr = model_.predict_proba(input_)
pr
type(pr)
pr_list = pr.tolist()
type(pr_list)
json_result = json.dumps(pr_list)
json_result
type(json_result)

    
#running flask app 
app = flask.Flask(__name__)
@app.route("/", methods=['GET','POST'])
def index():
    global graph
    with graph.as_default():
        csv_file = request.get_json(force = True)
                 
        csv = pd.read_csv(request.files.get("input"))
        proba = model_.predict_proba(csv)
        proba_as_list = proba.tolist()
        json_proba = json.dumps(proba_as_list) 
        return (json_proba)
  

@app.route("/predict", methods=['GET','POST'])    
def predict():
    global graph
    with graph.as_default():        
        csv = pd.read_csv(request.files.get("input"))
        proba = model_.predict_proba(csv)
        proba_as_list = proba.tolist()
        json_proba = json.dumps(proba_as_list) 
        return (json_proba)
    
@app.route("/hello", methods=['GET','POST'])
def hellos():
        global graph
        with graph.as_default():
                req_message = request.get.json(force =True)
                name = req_message['name']
                response = {
                        "greeting" : "hello, " + name + "!"                        
                }
                return jsonify(response)

     
if __name__  ==  "__main__":
    app.run()