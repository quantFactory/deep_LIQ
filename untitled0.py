# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:24:36 2018

@author: ali
"""

from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
import numpy
from pandas import read_csv
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
from keras import backend as K
K.tensorflow_backend._get_available_gpus()

_seed = 777
_input_dim = 35
kernel_init = "normal"
activation_fun = 'relu'
_loss = 'binray_crossentropy'
_optimizer = 'adam'
_metrics  = 'accuracy' 





numpy.random.seed(seed)

training_X = read_csv("F://deepLearning/DL_Proj_dataset/attrition.csv")
training_X.shape
training_X_ds = training_X.values
training_X

X =  training_X_ds[:,0:35].astype(float)
Y =  training_X_ds[:,35]

encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

def create_baseline():
     model= Sequential()
     model.add(Dense(35, input_dim = 35, kernel_initializer="normal", activation='relu'))
     model.add(Dense(35,activation='sigmoid'))
     model.add(Dense(1, kernel_initializer= "normal", activation='sigmoid'))
     model.compile(loss = 'binary_crossentropy',optimizer = 'adam',metrics=['accuracy'])
     return model

##estiamtor      

estimator = KerasClassifier(build_fn =create_baseline, epochs=30,batch_size=5,verbose=1)

kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)

results = cross_val_score(estimator, X, encoded_Y, cv=kfold)

print("baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))


