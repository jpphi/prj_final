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

layout =  html.Div([dcc.Location(id='url_login', refresh=True),
        html.H1("Prévention des maladies cardio-vasculaires", id='h1', style= {"text-align":"center"}),
 
        dbc.Row([
                dbc.Col([html.P("Nom utilisateur"),
                        dcc.Input(placeholder="Entrez votre nom d'utilisateur:",
                                type='text',
                                id='uname-box'),
                        dcc.Markdown('''
# This is an <h1> tag 
                            
                                petit blabla de présentation 
  
## This is an <h2> tag  
  
                                ###### This is an <h6> tag'''),
                        dcc.Input(placeholder="Entrez votre nom d'utilisateur:",
                                type='text',
                                id='uname-box2'),

                        #html.H2(children= "toto")
                ]),
        ]),
        dbc.Row([
                dbc.Col(html.P("Nom utilisateur")),
                dbc.Col(
                        dcc.Input(placeholder="Entrez votre mot de passe:",
                                type='password',
                                id='pwd-box'),
 
                        ),
        ],
        align="center",
        #no_gutters=True,
        ),

        
        #dcc.Input(placeholder="Entrez votre mot de passe:",
        #            type='password',
        #            id='pwd-box'),

        html.Button(children='Login',
                    n_clicks=0,
                    type='submit',
                    id='login-button'),
        html.Div(children='', id='output-state')
        ], style={'marginBottom': 50, 'background-color': "blue"}) #end div
