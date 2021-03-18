#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Important Modules
from flask import Flask,render_template, url_for ,flash , redirect
import pickle
from flask import request
import numpy as np




import os
from flask import send_from_directory


#from this import SQLAlchemy
app=Flask(__name__,template_folder='template')




@app.route("/")

@app.route("/home")
def home():
    return render_template("home.html")
 


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cancer")
def cancer():
    return render_template("cancer.html")


@app.route("/diabetes")
def diabetes():
    #if form.validate_on_submit():
    return render_template("diabetes.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")


@app.route("/liver")
def liver():
    #if form.validate_on_submit():
    return render_template("liver.html")

@app.route("/kidney")
def kidney():
    #if form.validate_on_submit():
    return render_template("kidney.html")



def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==8):#Diabetes
        loaded_model = pickle.load(open("Diabetes_model.pkl","rb"))
        result = loaded_model.predict(to_predict)
    elif(size==30):#Cancer
        loaded_model = pickle.load(open("Cancer_model.pkl","rb"))
        result = loaded_model.predict(to_predict)
    elif(size==18):#Kidney
        loaded_model = pickle.load(open("kidney_model.pkl","rb"))
        result = loaded_model.predict(to_predict)
    elif(size==10):#Liver
        loaded_model = pickle.load(open("Liver_model.pkl","rb"))
        result = loaded_model.predict(to_predict)
    elif(size==13):#Heart
        loaded_model = pickle.load(open("Heart_model.pkl","rb"))
        result =loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ["POST"])
def result():
    global recommendations
    global contact
    global prediction
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        
        if(len(to_predict_list)==30):#Cancer
            result = ValuePredictor(to_predict_list,30)
            if(int(result)==1):
                prediction='Benign tumor has been detected in the patient.'
                contact = " "
                recommendations = " "
            else:
                prediction='Malignant tumor has been detected in the patient.'
                contact='Helplines: \n022-24139445 \n1800-2700-703 \n+1800-180-1104'
                recommendations='You must immediately visit an oncologist. \nTreatment options: \nSurgery and radiation are used to treat cancer in a specific part of the body (such as the breast). They do not affect the rest of the body. \nChemotherapy, hormone treatment, targeted therapy, and immunotherapy drugs go through the whole body. They can reach cancer cells almost anywhere in the body. \nDoctors often use more than one treatment for breast cancer. The treatment plan that’s best for you will depend on the cancer stage and grade, age, pre lying health conditions, and other factors.'
                
        elif(len(to_predict_list)==8):#Diabetes
            result = ValuePredictor(to_predict_list,8)
            if(int(result)==1):
                prediction='The patient is Diabetic.'
                contact ='Helplines: \n+1800-300-22935 \n+1800-121-2096 \n+1800-180-1104'
                recommendations ='It is advised to seek help from a physician. \nAdditional tips include: \nChoose healthier carbohydrates. \nEat less salt. \nEat less red and processed meat. \nCut down on added sugar. \nDo not forget to get in regular physical exercise.'
            else:
                prediction='The patient is Non-Diabetic.'
                contact = " "
                recommendations = " "
                
        elif(len(to_predict_list)==18):#kidney
            result = ValuePredictor(to_predict_list,18)
            if(int(result)==1):
                prediction='Chronic kidney disease has been detected in the patient.'
                contact='Helplines: \n022-2281-4892 \n022-2880-9118 \n+1800-180-1104'
                recommendations='It is advised to immediately seek help from a nephrologist. \nAdditionsal tips include: \nControl your blood pressure \nMeet your blood glucose goal if you have diabetes \nWork with your health care team to monitor your kidney health \nTake medicines as prescribed \nWork with a dietitian to develop a meal plan \nMake physical activity part of your routine \nAim for a healthy weight \nGet enough sleep \nStop smoking \nFind healthy ways to cope with stress and depression '
            else:
                prediction='No chronic kidney disease has been detected in the patient.'
                contact = " "
                recommendations = " "
                
        elif(len(to_predict_list)==13):#heart
            result = ValuePredictor(to_predict_list,13)
            if(int(result)==1):
                prediction="No heart condition has been detected in the patient."
                contact = " "
                recommendations = " "
            
            else:
                prediction="A heart condition has been detected in the patient."
                contact='Helplines: \n+112 \n1800-103-3691 \n+1800-180-1104'
                recommendations='It is advised to immediately seek help from a cardiologist. \nAdditional tips include: \nEat a balanced diet. \nMaintain a reasonable body weight. \nStay at least moderately physically active, within any limits your cardiologist gives you. \nCheck your cholesterol level regularly, especially if your family has a history of heart disease. \nAvoid smoking tobacco. \nGet regular medical care from your primary care physician. '
                
        elif(len(to_predict_list)==10):#liver
            result = ValuePredictor(to_predict_list,10)
            if(int(result)==1):
                prediction="No liver condition has been detected in the patient."
                contact = " "
                recommendations = " "
            else:
                prediction="A liver condition has been detected in the patient."
                contact='Helplines: \n+9600953999 \n+01146300000 \n+1800-180-1104'
                recommendations='It is advised to immediately seek help from a gastroenterologists. \nAdditional tips include: \nCut down the amount of animal protein you eat. \nIncrease your intake of carbohydrates to be in proportion with the amount of protein you eat.\nEat fruits and vegetables and lean protein such as legumes, poultry, and fish. \nTake vitamins and medicines prescribed by your health care provider for low blood count, nerve problems, or nutritional problems from liver disease. \nLimit your salt intake. '



    return(render_template("result.html", prediction=prediction,recommendations=recommendations,contact=contact))

if __name__ == "__main__":
    app.run(debug=True)

