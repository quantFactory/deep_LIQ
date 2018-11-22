# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:48:03 2018

@author: ali
"""
import keras
from keras.models import load_model
import h5py
from keras.models import print_function
from flask import Flask, request
import tensorflow as tf
import flask
import numpy as np 
from numpy import array
from keras.backend import clear_session

#loading model 
model_ = load_model("./models/pre_trained_subset.h5")
graph = tf.get_default_graph()     
model_.summary()

x=1
Age = 30 
MartialStatus = 1 
Gender =2 
'''
  xx = np.array([[Age,MartialStatus,Gender]])
  pre = model_.predict(xx)
  pre
  '''
  
  
  
  
#testing model prediction 
Xnew = array([[48,1,1]])
Attrition_predict = model_.predict(Xnew)
Attrition_predict


#running flask app 
app = flask.Flask(__name__)
@app.route("/", methods=['GET','POST'])    
def indexx():
    global graph
    with graph.as_default():        
        Age =  request.args.get("Age")
        MartialStatus=  request.args.get("MartialStatus")
        Gender =  request.args.get("Gender")
        #prediction = model_.predict_classes(np.array([[Age,MartialStatus,Gender]]))                  
        predict_probability = prediction = model_.predict_proba(np.array([[Age,MartialStatus,Gender]]))                  
        return str(prediction)
    
if __name__  ==  "__main__":
    app.run()