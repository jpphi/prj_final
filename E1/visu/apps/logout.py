from dash import html
from dash import dcc

from apps import login, glob

layout = html.Div([dcc.Location(id='logout', refresh=True),

        html.Div(html.H2('Vous êtes déconnecté', style= {"text-align": "center"})),
        #html.Div(html.H2('Vérifier déconnection base', style= {"text-align": "center"})),
        html.P(""),
        html.Div(login.layout),

], style={'background-color': glob.fond_ecran_formulaire,  "display": "flex",
        "flex-direction": "column","justify-content":"space-between", })#end div