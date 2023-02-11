import config
import numpy as np
import pickle
import json
from sklearn.preprocessing import MinMaxScaler

class IrisPred():
    def __init__(self,SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
        self.SepalLengthCm = (SepalLengthCm)
        self.SepalWidthCm = (SepalWidthCm)
        self.PetalLengthCm = (PetalLengthCm)
        self.PetalWidthCm = (PetalWidthCm)

    def load_model(self):
        with open (config.Model_os_path,"rb") as f:
            self.model = pickle.load(f)
            
        with open (config.Json_os_path,'r') as f:
            self.json_data = json.load(f)

    def get_pred(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data["columns"]))


        test_array[0] = self.SepalLengthCm
        test_array[1] = self.SepalWidthCm
        test_array[2] = self.PetalLengthCm
        test_array[3] = self.PetalWidthCm

        print("Test array",test_array)
        predict_species = self.model.predict([test_array])[0]
        return predict_species
