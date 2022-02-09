!pip install pyngrok
!pip install flask_ngrok
from pyngrok import ngrok

ngrok.set_auth_token('23FQOPv2TJNiuaPmmm7MUuzSwd6_5BMazik7iC6AZr855sC4N')


import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
from flask_ngrok import run_with_ngrok
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
run_with_ngrok(app)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

@app.route('/', methods=['GET', "POST"])
def predict():
  input_values = [float(x) for x in request.form.values()]
  inp_features = [input_values]
  prediction = model.predict(inp_features)
  if prediction== '5':
    return render_template('index.html', prediction_text='5')
  elif prediction== '4':
    return render_template('index.html', prediction_text='4')
  elif prediction== '3':
    return render_template('index.html', prediction_text='3')
  elif prediction== '2':
    return render_template('index.html', prediction_text='2')
  elif prediction== '1':
    return render_template('index.html', prediction_text='1')
  elif prediction== '0':
    return render_template('index.html', prediction_text='0')
  else:
    return render_template('index.html', prediction_text='Projected Score: Between 80-90%')

if __name__ == '__main__':
    app.use_reloader=False
    app.run()