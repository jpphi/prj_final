from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from apps import login

#from app import app


layout = html.Div([ dcc.Location(id='url_login_df', refresh=True),
        html.Div([
                html.H2("L'utilisateur n'existe pas, ou le mot de passe n'est pas "+\
                        "correct... ", style= {"text-align": "center"}),
                html.H3("Même joueur, joue encore !", style= {"text-align": "center"}),
                html.P(""),
                html.Div([login.layout]),
        ]) #end div
]) #end div