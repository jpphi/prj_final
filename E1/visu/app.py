#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé le 25 décembre 2021

Projet de fin d'étude Simplon
    Serveur support de l'application d'aide au diagnostique sur les maladies cardio-vasculaires
    fichier devant se situer à la racine du site.

@author: jpphi
"""

import dash
import dash_bootstrap_components as dbc

# bootstrap theme
external_stylesheets = [dbc.themes.DARKLY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Prévention des maladies cardio-vasculaire' 

app._favicon = "favicon.ico"

server = app.server
app.config.suppress_callback_exceptions = True