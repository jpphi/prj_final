#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le 25 décembre 2021

Projet de fin d'étude Simplon
    Serveur

@author: jpphi
"""

import plotly.graph_objects as go
import pandas as pd
import dash_table

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# ---------------------------------------------------
# - Import -

df = pd.read_csv('data/Emotion_final.csv')
df2 = pd.read_csv("data/text_emotion.csv")

# ---------------------------------------------------
# - Figure 1 -
"""
trace = go.Histogram(x=df["Emotion"], xbins=dict(),
                   marker=dict(color='#810303'))
"""
layout = go.Layout(
    title="Frequency Emotions Counts From Kaggle Data"
)

fig = go.Figure(data=go.Histogram(x=df["Emotion"], xbins=dict(),
                   marker=dict(color='#810303')), layout=layout)

# - Figure 2 -
"""
trace = go.Histogram(x=df2["sentiment"], xbins=dict(),
                   marker=dict(color='#11337E'))
"""

layout = go.Layout(
    title="Frequency Emotions Counts From Word Data"
)
fig2 = go.Figure(data=go.Histogram(x=df2["sentiment"], xbins=dict(),
                   marker=dict(color='#11337E')), layout=layout)

# - Figure 3 -

x = np.array(df["Text"])
y = np.array(df["Emotion"])
vec = CountVectorizer(ngram_range=(1,2), min_df=500 )
X = vec.fit_transform(x)
words = vec.get_feature_names()
wsum = np.array(X.sum(0))[0]
ix = wsum.argsort()[::-1]
wrank = wsum[ix] 
labels = [words[i] for i in ix]
def subsample(x, step=150):
    return np.hstack((x[:30], x[10::step]))
freq = subsample(wrank)
r = np.arange(len(freq))
a = [i for i in range(100)]
fig3 = px.bar(x=r, y=freq)
fig3.update_traces(
    marker_color='#810303', 
    marker_line_color='black',
    marker_line_width=1.5
)
fig3.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals=a,
        title_text="Words",
        ticktext = subsample(labels)),
    title="Frequency of word in Kaggel Data",
    yaxis = dict(
        title_text="Frequency",))


# - Figure 4 -

x = np.array(df2["content"])
y = np.array(df2["sentiment"])
vec = CountVectorizer(ngram_range=(1,2), min_df=500 )
X = vec.fit_transform(x)
words = vec.get_feature_names()
wsum = np.array(X.sum(0))[0]
ix = wsum.argsort()[::-1]
wrank = wsum[ix] 
labels = [words[i] for i in ix]
def subsample(x, step=150):
    return np.hstack((x[:30], x[10::step]))
freq = subsample(wrank)
r = np.arange(len(freq))
a = [i for i in range(100)]
fig4 = px.bar(x=r, y=freq)
fig4.update_traces(
    marker_color='#11337E', 
    marker_line_color='black',
    marker_line_width=1.5
)
fig4.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals=a,
        title_text="Words",
        ticktext = subsample(labels)),
    title="Frequency of word in World Data",
    yaxis = dict(
    title_text="Frequency",))

# - Figure 5 -

fig5 = go.Figure(data=[go.Pie(labels=df.Emotion.unique(),
                             values=df.groupby('Emotion').Text.nunique(), 
                             textinfo='label+percent',
                            )],
                layout ={
                   'title':'Proportion Emotion for Kaggle set',
                   'font_color':'grey'
               })

# - Figure 6 -

fig6 = go.Figure(data=[go.Pie(labels=df2.sentiment.unique(),
                             values=df2.groupby('sentiment').content.nunique(), 
                             textinfo='label+percent',
                            )],
                layout ={
                   'title':'Proportion Emotion for World set',
                   'font_color':'grey'
               })

# ---------------------------------------------------
# - Tabs -

tab1_content = dash_table.DataTable(id='container-button-timestamp',
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            export_format='csv',
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
                'padding-left':'5px'
                }
            )

tab2_content = dash_table.DataTable(id='container-button-timestamp',
            data=df2.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df2.columns],
            export_format='csv',
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
             },
            css=[ {'selector': '.row', 'rule': 'margin: 0'}]
            )

# ---------------------------------------------------
# - Layout -
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Data table'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualising the data table from the two file'), className="mb-4")
        ]),
        dbc.Row([dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Data Kaggle",label_style={"color":"#810303"}),
        dbc.Tab(tab2_content, label="Data World", label_style={"color":"#11337E"}),
    ]
),
    ]),
        dbc.Row([
            dbc.Col(html.H1(children='Visualisation'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H4(children='In first lets see the count of emotion'), className="mb-1")
        ]), 
        dbc.Row([
                dbc.Col(dcc.Graph(id='graph-1',figure=fig),),
                dbc.Col(dcc.Graph(id='graph-2',figure=fig2), className="mb-2"),
            ]),
        dbc.Row([
                dbc.Col(html.H6(children='We can observe that the Happy and Sadness emotions are very present in the first dataset, in the second they are rather in the middle, it is neutral and worry which are dominant. Two emotions that do not exist in the first data set. The two datasets are distributed very differently'), className="mb-4")
            ]),
        dbc.Row([
                dbc.Col(html.H4(children='Lets see the proportion'), className="mb-1")
            ]),
        dbc.Row([
                dbc.Col(dcc.Graph(id='graph-5',figure=fig5),),
                dbc.Col(dcc.Graph(id='graph-6',figure=fig6), className="mb-4"),
            ]),
        dbc.Row([
                dbc.Col(html.H4(children='Now watching the word frequency of the two dataset'), className="mb-1")
        ]), 
        dbc.Row([
                dbc.Col(dcc.Graph(id='graph-3',figure=fig3),),
                dbc.Col(dcc.Graph(id='graph-4',figure=fig4), className="mb-2"),
            ]),
        dbc.Row([
                dbc.Col(html.H6(children='By taking the words that appear more than 500 times in the text, we realize that most of the words are linked words which cannot express any emotions, and that in the two sets of data, we must remove them with stopword if we want to make our model relevant.'), className="mb-4")
            ]),
        html.A("Visitez mon github", href="https://github.com/jpphi")
        ], className="mb-5"), 
    ])