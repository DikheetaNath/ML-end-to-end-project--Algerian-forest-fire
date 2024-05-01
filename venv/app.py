import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

#import ridge regressor model and standard scaler pickle
ridge_model = pickle.load(open(r'C:\Users\dikhe\OneDrive\Desktop\end_project\venv\models\ridge.pkl','rb'))
standard_scaler_model = pickle.load(open(r'C:\Users\dikhe\OneDrive\Desktop\end_project\venv\models\scaler.pkl','rb'))

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET',"POST"])
def predict_datapoint():
    if request.method=='POST':
        pass
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")





