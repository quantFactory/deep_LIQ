Title: Attrition prediction

Data:
Employee attrition is one the main contributing factors to business disruption cost increase and performance loss of companies. To be able to predict the employee attrition increases HR ability to make decisions and solve the problem on time. Dataset that is used in this project contains the information of survey from IBM indicating whether there is any attrition. In this project employee attrition probability is predicted using deep learning model and binary classification technique.
Dataset link : https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset.
dataset dimension: 35 *1470 target variable is "Attrition" = 0,1
Model is trained using deep learning and binary classification in Kera’s.
It’s a Sequential model constructed with 3 Dense layers.  
Requirements: 
Python version: Python 3.6.7 |Anaconda, Inc.
Keras : version 2.2.4 using TensorFlow backend.
Flask 1.0.2
Development environment:
OS: Microsoft Windows 10 64-bit
IDE: Anaconda Spyder 3.3.1
GitHub link: 
https://github.com/quantFactory/deep_LIQ.git
 
Project structure: 
Folder PATH listing
Volume serial number is B87E-897C
C:.
| 
|   att_predict.py
|   deep_liq.R
|   hr.doc
|   README.md
|   
+---api
+---data
|       attr.csv
|       
+---employeeDetails
|       emp_1.csv
|       emp_2.csv
|       emp_3.csv
|       emp_4.csv
|       emp_5.csv
|       
+---flask_apps
|   |   dl.png
|   |   predict_app.py
|   |   
|   \---static
|       |   hello.html
|       |   hello2.html
|       |   j.js
|       |   predict.html
|       |   
|       \---predict_file
+---models
|       pre_trained.h5
|       
\---__pycache__
        DL_LIQ_Spyder.cpython-36.pyc
        pickable.cpython-36.pyc

Hierarchy explanation: 
att_predict.py (model training)
contains the Keras deep learning model, you can change different parameter values such as number of epochs, batch size, activation functions and optimizer via the variables that is provided. To train the model run this python file. 
deep_liq.R
contains R commands that are used to pre-process the  attrition dataset. 
Data folder: 
Contains the attrition.csv dataset that is the input to our deep learning model. 
EmployeeDetails folder:
Contains csv files to test the model. Each csv file represents details of a single employee.
flask_apps (web service)
contains the file predict_app.py. It is the web service that is written in flask. To run the webservice , first run the file, then navigate to http://127.0.0.1:5000/predict using the  POSTMAN application.  And in the body section of message choose one of the files in the employeeDetails folder to see the result. 
Static
This folder contains html files to serve the API front-end. 
models folder
Contains pre-trained mode(s). predict_app.py utilizes this file to assess employee’s attrition probability. 
Steps to run the project: 
1-	Model training: 
To train the model run the att_predict.py in the root folder.
2-	Web service 
To run the flask application: 
•	Install POSTMAN to be able to receive post requests. 
•	Navigate  and run : flask_apps > predict_app.py
•	Insert http://127.0.01:500/predict to postman app and choose the method as POST
•	In the body section of Postman insert “input” as key choose a file from EmployeeDetails folder to see the prediction results. 



 





