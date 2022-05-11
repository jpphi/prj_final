#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé en mars 2022

Projet de fin d'étude Simplon
    Serveur support de l'application d'aide au diagnostique sur les maladies cardio-vasculaires
    home.py; page home. Ce fichier doit se situer dans le sous-répertoire /apps

@auteur: jpphi
"""

from dash import dcc, html
import dash_bootstrap_components as dbc

from apps import login, glob

layout= html.Div([
       html.H1("Prévention des maladies cardio-vasculaires", id='h1', style= {"text-align":"center"}),
        dbc.Row([ dcc.Markdown('''
Ce programme permet :
- D'utiliser des algorithmes pré-entrainés chargé **d'évaluer le risque 
pour un patient d'avoir un problème cardio vasculaire**.
- D'enregistrer **les nouvelles données** entrées qui pourrait ainsi **enrichir la base de données**.  
- De ** consulter les éléments enregistrés** dans la base de données.  
- D'accéder aux **différentes statistiques** réalisées à partir des données enregistrées.''')]),
        html.P(""),
        html.Div(login.layout),

], style={'background-color': glob.fond_ecran_formulaire,  "display": "flex",
        "flex-direction": "column","justify-content":"space-between", })