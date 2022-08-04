
import pickle
import json
import config
import numpy as np


class MedicalInsurance():
    def __init__(self, age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_' + region

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.reg_model=pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data=json.load(f)

    def get_predicted_price(self):

        self.load_model()

        print("JSON_Data",self.json_data)

        region_index= self.json_data['columns'].index(self.region)

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.age
        test_array[1] = self.json_data['sex'][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data['smoker'][self.smoker]
        test_array[region_index] = 1

        print("Test_array::",test_array)

        predicted_charges = np.around(self.reg_model.predict([test_array])[0],2)
        return predicted_charges