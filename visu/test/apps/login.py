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


layout =  html.Div([dcc.Location(id='url_login', refresh=True)
            , html.H2('''Please log in to continue:''', id='h1')
            , dcc.Input(placeholder='Enter your username',
                    type='text',
                    id='uname-box')
            , dcc.Input(placeholder='Enter your password',
                    type='password',
                    id='pwd-box')
            , html.Button(children='Login',
                    n_clicks=0,
                    type='submit',
                    id='login-button')
            , html.Div(children='', id='output-state')
        ]) #end div
