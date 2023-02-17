import numpy as np
import json
import pickle
import config


class Used_car_price_pred ():
    def __init__(self,year,seller_type,km_driven,fuel_type,transmission_type,mileage,engine,max_power,seats):
        self.year = year
        self.seller_type = seller_type
        self.km_driven = km_driven
        self.fuel_type = fuel_type
        self.transmission_type = transmission_type
        self.mileage = mileage
        self.engine = engine
        self.max_power= max_power
        self.seats = seats

    def load_model(self):
        with open (config.model_file_path,"rb") as f:
            self.model = pickle.load(f)
        
        with open (config.json_file_path,"r") as f:
            self.json_data = json.load(f)
    
    def  pred_model(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.year
        test_array[1] = self.json_data["seller_type"][self.seller_type]
        test_array[2] = self.km_driven
        test_array[3] = self.json_data["fuel_type"][self.fuel_type]
        test_array[4] = self.json_data["transmission_type"][self.transmission_type]
        test_array[5] = self.mileage
        test_array[6] = self.engine
        test_array[7] = self.max_power
        test_array[8] = self.json_data["seats"][self.seats]


        print("Test_array",test_array)
        price_prediction = self.model.predict([test_array])
        return price_prediction

