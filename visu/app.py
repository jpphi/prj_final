#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé le 25 décembre 2021

Projet de fin d'étude Simplon
    Serveur

@author: jpphi
"""

import dash
import dash_bootstrap_components as dbc

# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Wheel of Emotions' 

server = app.server
app.config.suppress_callback_exceptions = True