from keras.models import load_model
from keras.models import print_function
from flask import Flask, request, render_template,jsonify
import tensorflow as tf
import flask
import numpy as np 
from numpy import array
import pandas as pd 
import json



app = flask.Flask(__name__)
@app.route("/hello2", methods=['GET','POST'])
def show():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


if __name__  ==  "__main__":
    app.run()