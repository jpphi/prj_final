#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé en mars 2022

Projet de fin d'étude Simplon
    Serveur support de l'application d'aide au diagnostique sur les maladies cardio-vasculaires
    logout.py; page logout. Ce fichier doit se situer dans le sous-répertoire /apps

@auteur: jpphi
"""

from dash import html, dcc

from apps import login, glob

layout = html.Div([
        dcc.Location(id='logout', refresh=True),

        html.Div(html.H2('Vous êtes déconnecté', style= {"text-align": "center"})),
        
        html.P(""),
        
        html.Div(login.layout),

], style={'background-color': glob.fond_ecran_formulaire,  "display": "flex",
        "flex-direction": "column","justify-content":"space-between", })