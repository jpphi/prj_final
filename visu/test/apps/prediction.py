from dash import dcc
#import dash_html_components as html
from dash import html
#import dash
from apps import navbar2



layout = html.Div([html.H2("Prediction"),
            navbar2.layout,
            html.Br(),
            html.Div([dcc.Graph(id='graph')])
            ]) #end div