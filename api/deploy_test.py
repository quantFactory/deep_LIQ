# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:57:31 2018

@author: ali
"""
import pickle
from flask import Flask, request
import numpy as np
import pandas as pd

##create an app from that Flask
app = Flask(__name__)

@app.route('/')

def deepApi():
    return "Insert variables amounts!"

app.run(port=4999)


