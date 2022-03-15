#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:42:11 2021

@author: jpphi
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# ---------------------------------------------------
# - Layout -

layout = html.Div(children= [
    html.Div(children= [
        html.H1("Création de la base de donnée, des tables et du login du créateur de la base."),
        dcc.Location(id='create_db', refresh=True),
        dcc.Input(id= "dbname",
            type= "text",
            placeholder= "Nom de la base de données",
            maxLength= 30),
        dcc.Input(id= "creatorname",
            type= "text",
            placeholder= "Pseudo du créateur de la base",
            maxLength= 30),
        dcc.Input(id= "password",
            type= "password",
            placeholder= "mot de passe",
            maxLength= 50),
        dcc.Input(id= "email",
            type= "text",
            placeholder= "e-mail",
            maxLength= 50),
        html.Button('Crée !', id='submit-val', n_clicks=0),
        html.Div(id='container-button-basic')
    ])
])


"""
layout = dbc.Container([
    html.Div(id='container-button-basic2', children= [
        html.H1("Création de la base de donnée, des tables et du login du créateur de la base."),
        dcc.Location(id='create_db', refresh=True),
        dcc.Input(id= "dbname",
            type= "text",
            placeholder= "Nom de la base de données",
            maxLength= 30),
        dcc.Input(id= "creatorname",
            type= "text",
            placeholder= "Pseudo du créateur de la base",
            maxLength= 30),
        dcc.Input(id= "password",
            type= "password",
            placeholder= "mot de passe",
            maxLength= 50),
        dcc.Input(id= "email",
            type= "text",
            placeholder= "e-mail",
            maxLength= 50),
        html.Button('Crée !', id='submit-val', n_clicks=0),
        html.Div(id='container-button-basic', children= [html.P(children="Ici et maintenant")])
        ])
])

"""
