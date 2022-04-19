from dash import html
from dash import dcc

from apps import login

layout = html.Div([dcc.Location(id='logout', refresh=True),

        html.Div(html.H2('Vous êtes déconnecté', style= {"text-align": "center"})),
        #html.Div(html.H2('Vérifier déconnection base', style= {"text-align": "center"})),
        html.P(""),
        html.Div([login.layout]),

    ])#end div