#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le 25 décembre 2021

Projet de fin d'étude Simplon
    Serveur

@author: jpphi
"""

import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the Wheel of Emotions Dashboard", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.Img(src="/assets/wheel.png", height="300px")
                    , className="mb-5 text-center")
            ]),
        dbc.Row([
            dbc.Col(html.H5(children='This app is the result of a machine learning study on the wheel of emotions ! '
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='It consists of three main pages:  -  Data, which gives an overview of the data with table and some graph  -  '
                                     'Learning Machine, which give the learning machine study, with stats and analyse  -  '
                                     'APP Predict, where you can predict your emotion')          
                    , className="mb-5")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Explore Graph, Table, Download Data',
                                               className="text-center"),
                                       dbc.Button("DATA", href="/page1",
                                                                   color="primary",
                                                        className="mt-3"),                              
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access to the Machine learning study and Analyse',
                                               className="text-center"),
                                       dbc.Button("MACHINE LEAENING",
                                                  href="/page2",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Use our predict app, to know your emotions ',
                                               className="text-center"),
                                       dbc.Button("PREDICT App",
                                                  href="page3",
                                                  color="primary",
                                                  className="mt-3"),

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),
            
        ], className="mb-5"),
        html.A("Visitez mon github", href="https://github.com/jpphi")

    ], className="mb-5")

])