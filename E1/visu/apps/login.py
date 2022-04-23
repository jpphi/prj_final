from dash import dcc
#import dash_html_components as html
from dash import html
#import dash
#from dash.dependencies import Input, Output, State
#from sqlalchemy import Table, create_engine
#from sqlalchemy.sql import select
#from flask_sqlalchemy import SQLAlchemy
#from werkzeug.security import generate_password_hash, check_password_hash
#import sqlite3
#import warnings
#import os
#from flask_login import login_user, logout_user, current_user, LoginManager, UserMixin

import dash_bootstrap_components as dbc


from app import app
from apps import glob, form
"""
border: 10px ridge #f00;
    background-color: #ff0;
    padding: .5rem;
    display: flex;
    flex-direction: column;
"""
layout = html.Div([
        dcc.Location(id='url_login', refresh=True),
        html.H1("Prévention des maladies cardio-vasculaires", id='h1', style= {"text-align":"center"}),
        dbc.Row([ dcc.Markdown('''
Ce programme permet d'utiliser des algorithmes pré-entrainés chargé **d'évaluer le risque 
pour un patient d'avoir un problème cardio vasculaire**.  
D'autre part, **les nouvelles données** entrées pourrait aussi **enrichir la base de données**.  
Le programme permet aussi de **consulter les éléments enregistrés** dans la base de données.  
Enfin ce programme permet **d'accéder aux différentes statistiques** réalisées à partir 
des données enregistrées.''')]),

        html.P(""),

        html.Div(children='', id='output-state',style={"display": "flex",
                        'background-color': glob.fond_ecran_formulaire,}),
        
        #html.Div(glob.form),
        html.Div(form.layout),

        ], style={'background-color': glob.fond_ecran_formulaire,  "display": "flex",
        "flex-direction": "column","justify-content":"space-between", }) #end div

       #dbc.Row([
        #        dbc.Col([
        #                html.P("Nom utilisateur"),
        #        ],style={"display": "flex"})
        #],align="center"),

        
        #dcc.Input(placeholder="Entrez votre mot de passe:",
        #            type='password',
        #            id='pwd-box'),
