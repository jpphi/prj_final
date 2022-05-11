#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé en mars 2022

Projet de fin d'étude Simplon
    Serveur support de l'application d'aide au diagnostique sur les maladies cardio-vasculaires
    login.py; page login. Ce fichier doit se situer dans le sous-répertoire /apps

@auteur: jpphi
"""

from dash import dcc, html
#import dash_bootstrap_components as dbc

from app import app
from apps import glob

layout= html.Div([
        dcc.Location(id='url_login', refresh=True),

        html.H2("Login :",style={"text-align":"center"}),

        html.P(""),
        
        html.Div([

                html.Div([
                        html.P(children= "Utilisateur :"),
                        dcc.Input(placeholder="Nom", type='text', id='uname-box',
                                style= {"text-align": "center", "height": "30px"}, ),

                ], style= {"display":"flex", "text-align": "center", 
                        "align-content":"center", "gap":"20px", "justify-content":"space-around"},),

                html.Div([
                        html.P(children= "Mot de passe :"),
                        dcc.Input(placeholder="Mot de passe", type='password', id='pwd-box',
                                style= {"text-align": "center", "height": "30px"}), #, value="toto"
                ], style= {"display":"flex", "text-align": "center",
                        "align-content":"center", "gap":"20px", "justify-content":"space-around"}),

                #html.Div([
                html.Button(children='Connexion', n_clicks=0, type='submit',
                                id='login-button', style= {"text-align": "center",
                                "height": "30px"}),
                #], style= {"display":"flex", "text-align": "center",
                #        "align-content":"center", "gap":"20px", "justify-content":"space-around"}),

                html.Div(children='', id='output-state',
                        style={"display": "flex",'background-color': glob.fond_ecran_formulaire,}),

        ],style={"display": "flex", "background-color": glob.fond_ecran_formulaire, 
        "justify-content":"space-around", "align-items":"baseline"})

],style={"background-color": glob.fond_ecran_formulaire, })
