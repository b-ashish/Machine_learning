!pip install flask
from flask import Flask,render_template,jsonify,request
import numpy as np
from project_app.utils import Used_car_price_pred

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/input", methods = ['get','POST'])
def input():
    prediction = "HERE"
    if request.method == 'POST':
        data = request.form
        a = eval(data ["year"])
        b = data ["seller_type"]
        c = eval(data ["km_driven"])
        d = data ["fuel_type"]
        e = data ["transmission_type"]
        f = eval(data ["mileage"])
        g = eval(data ["engine"])
        h = eval(data ["max_power"])
        i = data ["seats"]

        price_pred = Used_car_price_pred(a,b,c,d,e,f,g,h,i)
        prediction = np.around(price_pred.pred_model(),2)[0]
    return render_template("index.html",result = prediction)
# price = Used_car_price_pred(2000,'Dealer',2000,2,2,20,1500,80,4)
# price.pred_model()

if __name__== "__main__":
    app.run(debug=True)
