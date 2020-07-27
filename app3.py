from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model= load('randfor.save')
trans=load('scalar')

@app.route('/')
def home():
    return render_template('index3.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[x for x in request.form.values()]]
    test=trans.transform(x_test)
    test=test[:,0:]
    prediction = model.predict(test)
    output=prediction[0]
    if(output>294):
        return render_template('index3.html', prediction_text='The CO2 Emisssion rate of your vehicle is {} g/km CO2 Emisssion Limit crossed,Seize the vehicle'.format(output))
    else:
        return render_template('index3.html', prediction_text='The CO2 Emisssion rate of your vehicle is {} g/km \n CO2 Emission is in Limit'.format(output))



if __name__ == "__main__":
    app.run(debug=True)
