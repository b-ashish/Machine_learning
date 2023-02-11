import numpy as np
import pickle
import json
import config

class MedInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
    
    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model= pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)
    
    def get_predicted_charges(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.age
        test_array[1] = self.json_data["sex"][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data["smoker"][self.smoker]
        test_array[5] = self.json_data["region"][self.region]

        print("Test array",test_array)
        predicted_charges = self.model.predict([test_array])
        return predicted_charges