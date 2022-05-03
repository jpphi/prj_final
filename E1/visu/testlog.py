#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé en mars 2022

Projet de fin d'étude Simplon
    Serveur support de l'application d'aide au diagnostique sur les maladies cardio-vasculaires
    fichier lançant l'application. Doit se situer à la racine du site

Ressources:
    https://ichi.pro/fr/comment-configurer-l-authentification-utilisateur-pour-les-applications-
dash-a-l-aide-de-python-et-flask-118945949211473
    https://dash.plotly.com/
    https://dash-bootstrap-components.opensource.faculty.ai/docs/components/

@author: jpphi
"""

from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import warnings
from flask_login import login_user, logout_user, current_user, LoginManager, UserMixin
import configparser

import os

from app import app, server
from apps import home, login, success, failed, data, logout, prediction, home

warnings.filterwarnings("ignore")
engine = create_engine('sqlite:///data.sqlite')
db = SQLAlchemy()
config = configparser.ConfigParser()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable = False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    #clair = db.Column(db.String(80))

Users_tbl = Table('users', Users.metadata)
Type_users_tbl = Table('typeusers', Users.metadata)

#server = app.server
#app.config.suppress_callback_exceptions = True

# config
server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI='sqlite:///data.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db.init_app(server)

# Setup the LoginManager for the server
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'

#User as base
# Create User class with UserMixin
# Sans cette classe, une erreur est généré empechant la connexion à la base
#  de donnée (User n'a pas d'attribut is_active)
class Users(UserMixin, Users):
    pass

#--------------------- Layout de l'application -------------------------------

app.layout= html.Div([
            html.Div(id='page-content', className='content'),
            dcc.Location(id='url', refresh=False),
        ])

#--------------------- Callback -------------------------------

# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.callback(
    Output('page-content', 'children')
    , [Input('url', 'pathname')])
def display_page(pathname):
    if pathname== '/':
        return home.layout

    elif pathname== '/login':
        return login.layout

    elif pathname== '/success':
        if current_user.is_authenticated:
            return success.layout
        else:
            return failed.layout

    elif pathname== '/data':
        if current_user.is_authenticated:
            return data.layout
        else:
            return failed.layout

    elif pathname== '/failed':
        return failed.layout
        # if current_user.is_authenticated:
        #     return success.layout
        # else:
        #     return failed.layout
    elif pathname== '/logout':
        if current_user.is_authenticated:
            logout_user()
            return logout.layout #logout.layout
        else:
            return login.layout #failed.layout

    elif pathname== '/prediction':
        if current_user.is_authenticated:
            return prediction.layout
        else:
            return failed.layout
    else:
        return '404'

@app.callback(Output('url_login', 'pathname')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def successful(n_clicks, input1, input2):
    user = Users.query.filter_by(username=input1).first()
    if user:
        if check_password_hash(user.password, input2):
            login_user(user)
            return '/success'
        else:
            return '/failed'
    else:
        pass

#------------------------------ Main ------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
    #serve(app, host="0.0.0.0", port=8080)
