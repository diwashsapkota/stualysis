#.venv\scripts\activate
#python -m flask run


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


application = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predict', methods=['POST'])
def predict():

    int_features = [ x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    

    if output == 5:
        return render_template('index.html', prediction_text=format("Above 90%"))
    elif output== 4:
        return render_template('index.html', prediction_text=format("Between 80-90%"))
    elif output== 3:
        return render_template('index.html', prediction_text=format("Between 70-80%"))
    elif output== 2:
        return render_template('index.html', prediction_text=format("Between 50-60%"))
    elif output== 1:
        return render_template('index.html', prediction_text=format("Between 50-60%"))
    elif output== 0:
        return render_template('index.html', prediction_text=format("Below 50%"))
    else:
        return render_template('index.html', prediction_text=format("Sorry, the parameters you entered were not correct."))


if __name__ == "__main__":
    application.debug=True
    application.run()

