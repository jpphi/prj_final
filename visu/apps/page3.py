#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le 25 décembre 2021

Projet de fin d'étude Simplon
    Serveur

@author: jpphi
"""

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier

#import nltk
from app import app


# ---------------------------------------------------
# - Code -

#nltk.download('stopwords')

df = pd.read_csv("data/Emotion_final.csv")
#stopwords = nltk.corpus.stopwords.words('english')


targets = list(df["Emotion"])
corpus = list(df["Text"])

X = corpus
y = targets
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=0)

pipe91 = Pipeline([('vect', CountVectorizer()), ('sgd', SGDClassifier()),])
pipe91.fit(X_train, y_train)

# ---------------------------------------------------
# - Layout -

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Predict APP'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='For this APP, we use the first dataset to training our prediction model because it is much more efficient'), className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Try our prediction APP with your input'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(dcc.Input(id="input1", type="text", placeholder="Type your text", debounce=True), className="mb-4 text-center")
        ]),
        dbc.Row([
            dbc.Col(html.H2(id="output"), className="mb-4 text-center")
        ]),
        dbc.Row([
            dbc.Col(html.Img(src="/assets/sentiment-analysis.jpg", height="300px"))
        ]),
    ]),
            html.A("Visitez mon github", href="https://github.com/jpphi")

    ])

@app.callback(
    Output("output", "children"),
    Input("input1", "value"),)
def update_output(input1):  
    
    text = [input1]
    if input1 is None:
        return "Wheel of Emotions"
    else:
        y_pred = pipe91.predict(text)
        return u'Emotion : {}'.format(y_pred)