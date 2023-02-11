
from flask import Flask,render_template,jsonify,request
from Project_app.utils import IrisPred

import config

app = Flask(__name__)

@app.route("/test")
def base():
    sepalLengthCm  =  4.0
    SepalWidthCm   =  2
    PetalLengthCm  =  1
    PetalWidthCm   =  0.1
    iris_data = IrisPred(sepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    species = iris_data.get_pred()
    return jsonify({"Result":f"Predicted species is {species}"})

@app.route("/")
def predict():
    return render_template("home.html")

@app.route("/predict",methods=['get',"POST"])
def input():
    species = "here"
    if request.method == 'POST':

        data = request.form
        a = eval(data["sepalLengthCm"])
        b = eval(data["SepalWidthCm"])
        c = eval(data["PetalLengthCm"])
        d = eval(data["PetalWidthCm"])
        l = [a,b,c,d]
        for i in l:
            print(i)
            print(type(i))

        iris_data = IrisPred(a,b,c,d)
        species = iris_data.get_pred()

    return render_template("index.html",result=species)




if __name__ =="__main__":
    app.run(debug=True)

