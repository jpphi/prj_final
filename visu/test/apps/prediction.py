from dash import dcc
#import dash_html_components as html
from dash import html
#import dash

from dash.dependencies import Input, Output, State

from apps import navbar2
from app import app


layout = html.Div([navbar2.layout,
            html.H2("Prediction"),
            html.Br(),
            html.Div([dcc.Graph(id='graph')]),
            html.Button(id='back-button', children='Retour', n_clicks=0),

            ]) #end div


#