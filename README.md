### Attrition prediction

### How to train the model and run the webserver

#### 1-Model training: 
Run att_predict.py file by typing command below in Windows commandline applikcation  or Mac/Linux Terminal application:
           
           computerName:~ Username$ python att_perdict.py
          
     
#### 2- How to test the API(Flask application)
        
*	Install [POSTMAN](https://www.getpostman.com/download?platform=win64) to be able to receive post requests. 
*	Navigate  and run : flask_apps > predict_app.py.
*	Insert http://127.0.01:500/predict to postman app and choose the method as POST
*	In the body section of Postman insert “input” as key choose a file from EmployeeDetails folder to see the prediction results. 


#### 3- Run the web servire (Flask application)
Run prdcit.py file (locate it in flask_app folder) by typing commands below in Windows Commandline application or Mac/Linux Terminal application :

           computerName:~ Username$ python perdict.py
                     
 command above will runs the Flaks webserver.
                  
                    

#### Data:
Employee attrition is one the main contributing factors to business disruption cost increase and performance loss of companies. To be able to predict the employee attrition increases HR ability to make decisions and solve the problem on time. Dataset that is used in this project contains the information of survey from IBM indicating whether there is any attrition. In this project employee attrition probability is predicted using deep learning model and binary classification technique.

Dataset link : https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset.

dataset dimension: 35 *1470 target variable is "Attrition" = 0,1
Model is trained using deep learning and binary classification in Kera’s.
It’s a Sequential model constructed with 3 Dense layers.  

#### Requirements:  
Python version: Python 3.6.7 |Anaconda, Inc.  
Keras : version 2.2.4 using TensorFlow backend.  
Flask 1.0.2  
Development environment:  
OS: Microsoft Windows 10 64-bit  
IDE: Anaconda Spyder 3.3.1  
GitHub link:  
https://github.com/quantFactory/deep_LIQ.git  

#### Project structure: 
Folder PATH listing

```bash
\
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
```

 





