#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:41:31 2021

@author: jpphi
"""

import dash_html_components as html
import dash_bootstrap_components as dbc


layout = html.Div([
    dbc.Container(children= [
        html.H1(children= ["Bienvenue dans l'utilitaire de création de base de données"], className="text-center"),

        html.P(children= ["Cette application permet de créer la base de données en local. Celle-ci "+\
                "pourra être exportée par la suite sur un serveur distant. Outre la création de la base de données "+\
                "cet utilitaire crée les tables et un super utilisateur permettant d'administrer la base. "+\
                "Enfin, une page permet de créer d'autres utilisateurs avec différents privilèges."],
                className="mb-4"),

        dbc.Button("bdd", href="/createdb"), 
        html.Br(),                             
        dbc.Button("Création d'utilisateurs", href="/createuser"),                              
        
    ], className="mb-5")

])



"""
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Bienvenue dans l'utilitaire de création de base de données", className="text-center"),
                className="mb-5 mt-5")]),

        dbc.Row([
            dbc.Col(html.P(children="Cette application permet de créer la base de données en local. Celle-ci "+\
                "pourra être exportée par la suite sur un serveur distant. Outre la création de la base de données "+\
                "cet utilitaire crée les tables et un super utilisateur permettant d'administrer la base. "+\
                "Enfin, une page permet de créer d'autres utilisateurs avec différents privilèges."),
                className="mb-4")]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children= "Création de la base de données", className="text-center"),
                                       dbc.Button("bdd", href="/createdb", color="primary", className="mt-3"),                              
                                       ], body=True, color="dark", outline=True), width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children="Création d'utilisateurs", className="text-center"),
                                       dbc.Button("user", href="/createuser", color="primary", className="mt-3"),
                                       ], body=True, color="dark", outline=True), width=4, className="mb-4"),
            ], className="mb-5"),

    ], className="mb-5")

])
"""