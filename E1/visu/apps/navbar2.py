#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé en mars 2022

Projet de fin d'étude Simplon
    Serveur support de l'application d'aide au diagnostique sur les maladies cardio-vasculaires
    navbar2.py; layout de la barre de navigation. 
        Ce fichier doit se situer dans le sous-répertoire /apps

@auteur: jpphi
"""

from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import html

from app import app   

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Consultation données", href="/data"),
        dbc.DropdownMenuItem("Prédiction", href="/prediction"),
        dbc.DropdownMenuItem("logout", href="/logout"),
    ],
    nav = True,
    in_navbar = True,
    label = "Menu",
)

layout = dbc.Navbar(
    dbc.Container(
        [
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="../assets/stethoscope-coeur2.png", height="30px")),
                        dbc.Col(
                            dbc.NavbarBrand("Prévention des maladies cardio-vasculaires.",)
                        ),
                    ],
                    
                    #no_gutters=True,
                ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ], style={"display": "flex", "justify-content":"space-around"}
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

