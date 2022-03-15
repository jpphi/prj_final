#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:43:44 2021

@author: jpphi
"""

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

# L'utilisateur "Propriétaire" est crée au moment de la création de la table. Il n'y a
#   qu'un seul propriétaire, il ne peut donc pas être crée ici !
tab= ["Administrateur", "Utilisateur", "Visiteur"]

#-----------------------------------------
# - Layout -

layout = html.Div(children= [
    html.Div(children= [ html.H1("La base est créé ? Ajout d'utilisateur."),
        dcc.Location(id='create_user', refresh= True),

        dbc.Container([

            dcc.Input(id="username", type="text", placeholder="user name", maxLength =15,
                style= {'display': 'inline-block'}),
            dcc.Input(id="password", type="password", placeholder="password",
                style= {'display': 'inline-block'}),
            dcc.Input(id="email", type="email", placeholder="email", maxLength = 50,
                style= {'display': 'inline-block'}),
            dcc.Dropdown(id='type_user', options=[ {"label": tab[i], "value": i+2} for i in range(len(tab)) ],
                value= 2, style= {'display': 'block'}),
        ]),
        
        html.Br(),
        html.Button('Create User', id='submit-val', n_clicks=0),
        html.Div(id='container-button-basic3', style= {'display': 'block'}),
    ])
  
])

