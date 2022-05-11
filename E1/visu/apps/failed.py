#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé en mars 2022

Projet de fin d'étude Simplon
    Serveur support de l'application d'aide au diagnostique sur les maladies cardio-vasculaires
    failed.py; page failed. Ce fichier doit se situer dans le sous-répertoire /apps

@auteur: jpphi
"""

from dash import dcc, html
import dash_bootstrap_components as dbc

from apps import login, glob

layout = html.Div([ dcc.Location(id='url_login_df', refresh=True),
        html.Div([
                html.H1(children= "Reconnection ?", style= {"text-align": "center"}),
                html.P(""),

                html.H4("L'utilisateur n'existe pas, ou le mot de passe n'est pas "+\
                        "correct... ", style= {"text-align": "center"}),
                html.P(""),
                
                html.H4("Même joueur, joue encore !", style= {"text-align": "center"}),
                html.P(""),
                
                html.Div([login.layout]),
 
        ]) #end div
], style= {'background-color': glob.fond_ecran_formulaire,  "display": "flex", 
            "flex-direction": "column"}) #end div