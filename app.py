# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:11:12 2020
@author: pattn
"""


# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from flask import Flask, request, render_template
import pickle

app = Flask("__name__")



q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/predict", methods=['POST'])
def predict():
    
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8= request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']

    model = pickle.load(open("model.sav", "rb"))
    
    
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5,inputQuery6, inputQuery7, inputQuery8, inputQuery9, inputQuery10]]
    new_df = pd.DataFrame(x, columns = ['profession','régime', 'situation_pros', 'Age', 'Enfant', 'tarif','garantie','région','Ancienneté','compagnie précédente'])
    
    single = model.predict(new_df)
    probablity = model.predict_proba(new_df)[:,1]
    
    if single==1:
        o1 = "The contract will not be cancelled"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "The contract will be cancelled"
        o2 = "Confidence: {}".format(probablity*100)
        
    return render_template('home.html', output1=o1, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7= request.form['query7'],query8 = request.form['query8'],query9 = request.form['query9'],query10 = request.form['query10'])
    
if __name__ == "__main__":
    app.run()
