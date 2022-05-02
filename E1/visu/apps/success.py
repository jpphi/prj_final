from dash import dcc
import pandas as pd
import sqlite3

from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from apps import navbar2, glob


import os


from sqlalchemy import Table, create_engine, sql, text
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy



#with sqlite3.connect(bdd) as conn:
#    df= pd.read_sql("SELECT * from examen",conn)
#engine = create_engine('sqlite:///toto.toto')
#db = SQLAlchemy()

#str_sql = sql.text("SELECT * FROM examen")

#with engine.connect() as connection:
#    records = pd.read_sql('SELECT * from utilisateur', connection)


#records= "cursor.fetchall()"


if glob.df_examen== None or glob.df_medecin== None or glob.df_patient== None \
    or glob.df_diagnostique== None:
    try:
        with sqlite3.connect(glob.bdd) as conn:
            glob.df_examen= pd.read_sql("SELECT * from examen",conn)
        with sqlite3.connect(glob.bdd) as conn:
            glob.df_medecin= pd.read_sql("SELECT * from medecin",conn)
        with sqlite3.connect(glob.bdd) as conn:
            glob.df_patient= pd.read_sql("SELECT * from patient",conn)
        with sqlite3.connect(glob.bdd) as conn:
            glob.df_diagnostique= pd.read_sql("SELECT * from diagnostique",conn)
        cpt_rendu= f"Ouverture des tables examen, medecin et patient depuis {glob.bdd}"
    except:
        cpt_rendu= f"La base {glob.bdd} n'a pu être chargé"

layout = html.Div([
            dcc.Location(id='url_login_success', refresh=True),
            navbar2.layout,
            html.Div([
                html.H2("Bienvenue dans le programme d'aide au dépistage de maladies "+\
                    "cardio-vasculaires.", style={"text-align":"center"}),
                html.P(),
                html.H4('Souhaitez-vous travailler sur les données ou effectuer une prédiction ?',
                    style= {"text-align": "center"}),              
                dcc.Link('Table des examens.', href = '/data'),
                dcc.Link('Effectuer une prédiction sur de nouvelles données.', href = '/prediction'),
            ],style={"display": "flex", 'background-color': glob.fond_ecran_formulaire,
                "flex-direction": "column", "align-items":"center"}),

            html.P(""),

            html.Div([
                html.P(cpt_rendu,style={"text-align": "center"}),
                #html.Div([           
                #    html.Button(id='bouton-bdd', children= "Lancer l'analyse", n_clicks=0,
                #        style={"text-align":"center"}),
                #    html.Div(id="sortie-bouton-bdd", children= ""),
                #] ),
            ])
        ],style={"display": "flex", 'background-color': glob.fond_ecran_formulaire,
            "flex-direction": "column"}) #end div

"""
@app.callback(
    Output(component_id= 'sortie-bouton-bdd', component_property= 'children'),
    Input('bouton-bdd', 'n_clicks'),
    #State('ri-genre', 'value'), State("ri-activite", 'value'), State("ri-tabac", "value"),
    )
def chargement_donnee(n_clicks):
    if n_clicks > 0:



        if glob.dfbase== None:
            try:
                with sqlite3.connect(glob.bdd) as conn:
                    glob.dfbase= pd.read_sql("SELECT * from examen",conn)

                #conn = sqlite3.connect(glob.bdd)

                #dfbase= pd.read_sql_query("SELECT * FROM examen", conn)
                #print(glob.dfbase)

                return f"Chargement de la base de données {glob.bdd} effectué."
            except:
                return f"Problème chargement des données. {glob.bdd}\n"+\
                    f"{os.getcwd()}"
"""