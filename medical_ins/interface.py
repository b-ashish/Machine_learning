
from flask import Flask,render_template,jsonify,request
import numpy as np


import config

from Project_app.utils import MedInsurance

app = Flask(__name__)


@app.route("/", methods=['get','POST'])
def pred():
    prediction ="HERE"
    if request.method == 'POST':
        
        data = request.form
        a = data["age"]
        b = data["sex"]
        c = data["bmi"]
        d = data["children"]
        e = data["smoker"]
        f = data["region"]
        med_ins = MedInsurance(a,b,c,d,e,f)
        prediction= np.around(med_ins.get_predicted_charges()[0],2)
    return render_template("index.html",result = prediction)


# @app.route("/predict")
# def get_ins_char():
#     age = 30
#     sex = 'male'
#     bmi = 26
#     children = 1
#     smoker = 'no'
#     region = 'northeast'

#     med_ins = MedInsurance(age,sex,bmi,children,smoker,region)
#     charges = med_ins.get_predicted_charges()

#     return jsonify({"Result":f"Predicted medical insurance charges are : {charges}"})

if __name__ =="__main__":
    app.run(debug=True)