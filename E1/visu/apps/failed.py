from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from apps import login, glob, form

#from app import app


layout = html.Div([ dcc.Location(id='url_login_df', refresh=True),
        html.Div([
                html.H1(children= "Reconnection ?", style= {"text-align": "center"}),
                html.P(""),

                html.H4("L'utilisateur n'existe pas, ou le mot de passe n'est pas "+\
                        "correct... ", style= {"text-align": "center"}),
                html.P(""),
                
                html.H4("Même joueur, joue encore !", style= {"text-align": "center"}),
                html.P(""),
                
                html.H3(children= "Login :", style= {"text-align": "center"}),
                
                html.Div([login.layout]),
 
        ]) #end div
], style= {'background-color': glob.fond_ecran_formulaire,  "display": "flex", 
            "flex-direction": "column"}) #end div