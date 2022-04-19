from dash import dcc
import pandas as pd
import sqlite3

from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from apps import navbar2, glob

layout = html.Div([dcc.Location(id='url_login_success', refresh=True),
            navbar2.layout,
            html.Div([html.H2('Login successful.'),
                html.Br(),
                html.P('Select a Dataset'),
                ]), #end div
            dcc.Link('Data', href = '/data'),
            dcc.Link('Prédiction', href = '/prediction'),
            html.Div([html.Br(),


            html.Div([           
                html.Button(id='bouton-bdd', children= "Lancer l'analyse", n_clicks=0,
                style={"text-align":"center"}),
                html.Div(id="sortie-bouton-bdd", children= ""),
                ]
                
                ,style={"display": "flex", "align-items":"center", "align-content":"center",
                            "justify-content":"space-around",#"width": "150px",
                            'background-color': glob.fond_ecran_formulaire,
                            "flex-direction": "column"}),




            ])
        ]) #end div




@app.callback(
    Output(component_id= 'sortie-bouton-bdd', component_property= 'children'),
    Input('bouton-bdd', 'n_clicks'),
    #State('ri-genre', 'value'), State("ri-activite", 'value'), State("ri-tabac", "value"),
    )
def chargement_donnee(n_clicks):
    if n_clicks > 0:
        if glob.dfbase== None:
            try:
                conn = sqlite3.connect(glob.bdd)
                glob.dfbase= pd.read_sql_query("SELECT * FROM entrainement", conn)
                conn.close()
                return f"Chargement des données effectué."
            except:
                return f"Echec à l'ouverture de la base {glob.bdd}."
