from flask import Flask,render_template,jsonify,request,redirect,url_for
import config

from project_app.utils import MedicalInsurance

app = Flask(__name__)

@app.route('/')
def flask():

    print("Hello")
    return jsonify({'Message':"Successful"})

@app.route('/test')
def test():

    print("Hello")
    return jsonify({'Message':"My name is shyam kokare"})

@app.route('/predict_charges')

def get_insurance_charges():
    data= request.form
    age = eval(data['age'])
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    med_ins=MedicalInsurance(age, sex, bmi, children, smoker, region)
    charges=med_ins.get_predicted_price()

    return jsonify({"Result": f"Predicted Medical Charges are : {charges}"})
        

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=False)