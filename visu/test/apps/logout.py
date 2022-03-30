from dash import html
from dash import dcc

from apps import login

layout = html.Div([dcc.Location(id='logout', refresh=True)
        , html.Br()
        , html.Div(html.H2('You have been logged out - Please login'))
        , html.Br()
        , html.Div([login.layout])
        , html.Button(id='back-button', children='Go back', n_clicks=0)
    ])#end div