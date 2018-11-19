# deep_LIQ
Attrition analytics _ deep learning project

This repo contains 3 files 

1- deep_liq.R 
R have been used a a programming language of choice for data manipulation and dataset porep processing. 

2- DL_LIQ_Spyder.py

Deep learning model written in Keras using TensorFlow as backend and has been configured to use GPU cores. 
currently the number of epochs is set to 20 because the system that processes the model uses a single GTX 960 Nvidia card
Better accuracy results will achieve if epoches = 200. which demands more time to process on current hardware.
** Confusion matrix will be added to model 
Prediction method : binary classification


3- dataset 
dataset called attrition.csv which resides in data folder
Data source: https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset.)

dataset dimension:  35 *1470 
target variable is "Attrition" = 0,1


It is a HR analytics dataset that predicts employee attrition. 
