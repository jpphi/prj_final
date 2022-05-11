#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé en mars 2022

Projet de fin d'étude Simplon
    Serveur support de l'application d'aide au diagnostique sur les maladies cardio-vasculaires
    page success; ce fichier doit se situer dans le sous-répertoire /apps

@auteur: jpphi
"""

import pandas as pd
import sqlite3

from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from apps import navbar2, glob

#--------------------- Ouverture des tables -------------------------------

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
        cpt_rendu= f"Une des table de la base {glob.bdd} n'a pu être chargé"

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
            ])
        ],style={"display": "flex", 'background-color': glob.fond_ecran_formulaire,
            "flex-direction": "column"}) #end div
