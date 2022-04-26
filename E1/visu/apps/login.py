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
 
        html.P(""),

        #html.Div(children='', id='output-state',style={"display": "flex",
        #                'background-color': glob.fond_ecran_formulaire,}),
        
        html.Div(form.layout),

], style={'background-color': glob.fond_ecran_formulaire,  "display": "flex",
        "flex-direction": "column","justify-content":"space-between", }) #end div
