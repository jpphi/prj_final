# https://ichi.pro/fr/comment-configurer-l-authentification-utilisateur-pour-les-applications-dash-a-l-aide-de-python-et-flask-118945949211473

from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

#import dash

from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
#import sqlite3
import warnings
from flask_login import login_user, logout_user, current_user, LoginManager, UserMixin
import configparser

import os

from app import app, server
from apps import home, login, success, failed, data, logout, prediction, nonloger, glob, home



#glob.bdd= '/home/jpphi/Documents/brief/ProjetFinDEtude/E1/datas/base_E1.db' #os.path.abspath("../datas/base_E1.db")




warnings.filterwarnings("ignore")
#conn = sqlite3.connect('data.sqlite')
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


#app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

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
class Users(UserMixin, Users):
    pass

#--------------------- Ouverture de la base medecin -------------------------------

ret= glob.ouveture_base_medecin()

if ret== None: glob.alerte("Erreur testlog :")

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


"""
#set the callback for the dropdown interactivity
@app.callback(
    [Output('graph', 'figure')]
    , [Input('dropdown', 'value')])
def update_graph(dropdown_value):
    if dropdown_value == 'Day 1':
        return [{'layout': {'title': 'Graph of Day 1'}
                , 'data': [{'x': [1, 2, 3, 4]
                    , 'y': [4, 1, 2, 1]}]}]
    else:
        return [{'layout': {'title': 'Graph of Day 2'}
                ,'data': [{'x': [1, 2, 3, 4]
                    , 'y': [2, 3, 2, 4]}]}]



"""
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

"""
@app.callback(
    Output('output-state', 'children')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        user = Users.query.filter_by(username=input1).first()
        if user:
            if check_password_hash(user.password, input2):
                return ''
            else:
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''
"""

"""
@app.callback(
    Output('url_login_success', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/success'
"""
#from waitress import serve


#------------------------------ Main ------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
    #serve(app, host="0.0.0.0", port=8080)






#------------------ zone code obsolète ----------------

"""
@app.callback(
   [Output('container-button-basic', "children")]
    , [Input('submit-val', 'n_clicks')]
    , [State('username', 'value'), State('password', 'value'), State('email', 'value')])
def insert_users(n_clicks, un, pw, em):
    #hashed_password = generate_password_hash(pw, method='sha256')
    if un is not None and pw is not None and em is not None:
        #---------------------------------------------------------------------
        #
        # IL FAUT CONTROLER L EXISTANCE DE L UTILISATEUR AVANT DE L INSERER
        #
        #---------------------------------------------------------------------
        
        hashed_password = generate_password_hash(pw, method='sha256')
        ins = Users_tbl.insert().values(username=un,  password=hashed_password, email=em)
        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        return [login]
    else:
        return [html.Div([html.H2('Already have a user account?'), dcc.Link('Click here to Log In', href='/login')])]
"""

"""
    elif pathname== '/data':
        if current_user.is_authenticated:
            return data.layout

"""



"""
create = html.Div([ html.H1('Create User Account')
        , dcc.Location(id='create_user', refresh=True)
        , dcc.Input(id="username"
            , type="text"
            , placeholder="user name"
            , maxLength =15)
        , dcc.Input(id="password"
            , type="password"
            , placeholder="password")
        , dcc.Input(id="email"
            , type="email"
            , placeholder="email"
            , maxLength = 50)
        , html.Button('Create User', id='submit-val', n_clicks=0)
        , html.Div(id='container-button-basic')
    ])#end div
"""
"""
login =  html.Div([dcc.Location(id='url_login', refresh=True)
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
"""

"""
success = html.Div([dcc.Location(id='url_login_success', refresh=True)
            , html.Div([html.H2('Login successful.')
                    , html.Br()
                    , html.P('Select a Dataset')
                    , dcc.Link('Data', href = '/data')
                ]) #end div
            , html.Div([html.Br()
                    , html.Button(id='back-button', children='Go back', n_clicks=0)
                ]) #end div
        ]) #end div
"""



"""
data = html.Div([dcc.Dropdown(
                    id='dropdown',
                    options=[{'label': i, 'value': i} for i in ['Day 1', 'Day 2']],
                    value='Day 1')
                , html.Br()
                , html.Div([dcc.Graph(id='graph')])
            ]) #end div
"""




"""
failed = html.Div([ dcc.Location(id='url_login_df', refresh=True)
            , html.Div([html.H2('Log in Failed. Please try again.')
                    , html.Br()
                    , html.Div([login])
                    , html.Br()
                    , html.Button(id='back-button', children='Go back', n_clicks=0)
                ]) #end div
        ]) #end div
"""




"""
logout = html.Div([dcc.Location(id='logout', refresh=True)
        , html.Br()
        , html.Div(html.H2('You have been logged out - Please login'))
        , html.Br()
        , html.Div([login])
        , html.Button(id='back-button', children='Go back', n_clicks=0)
    ])#end div
"""

