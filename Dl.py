# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:49:42 2018

@author: ali
"""

from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense,Activation
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
import numpy as np 
import pandas as pd  
import os 




path_ = os.getcwd()
print(path_)


seed = 10
_input_dim = 31
kernel_init = "normal"
activation_fun = 'sigmoid'
_loss = 'binary_crossentropy'
_optimizer = 'adam'
_metrics  = 'accuracy' 


np.random.seed(seed)
#reading data
training_X = pd.read_csv("./data/attrition2.csv")
training_X.shape
training_X_ds = training_X.values
training_X


list(training_X.columns)

# training and test set detemination
X =  training_X_ds[:,0:31].astype(float)
Y =  training_X_ds[:,31]

print(Y)

encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

##baseline
##training deep feed forward 
def create_baseline():
     model= Sequential()
     model.add(Dense(36, input_dim = _input_dim, kernel_initializer= kernel_init, activation=activation_fun))     
     model.add(Dense(16,activation='relu'))
     model.add(Dense(1, kernel_initializer= "normal", activation='sigmoid'))
     model.compile(loss = _loss,optimizer = 'adam' ,metrics=['accuracy'])
     model.fit(X,encoded_Y)
     return model

    
   
estimator = KerasClassifier(build_fn =create_baseline, epochs=10,batch_size=5,verbose=2)
    
kfold = StratifiedKFold(n_splits =10, shuffle=True, random_state=seed)
    
results = cross_val_score(estimator, X, encoded_Y, cv=kfold)
    
print("ACC: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

model = create_baseline()
model_json = model.to_json()
with open("att_model.json","w") as json_file:
     json_file.write("att_josn")
     
    
model.save_weights("attr_model_weights.h5")
print("Saved model to disk")
model.save("./models/pre_trained.h5")

