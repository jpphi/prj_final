# https://ichi.pro/fr/comment-configurer-l-authentification-utilisateur-pour-les-applications-dash-a-l-aide-de-python-et-flask-118945949211473

import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State

from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import warnings
import os
from flask_login import login_user, logout_user, current_user, LoginManager, UserMixin
import configparser

warnings.filterwarnings("ignore")

data_base=""

db = SQLAlchemy()
config = configparser.ConfigParser()

class TypeUtilisateur(db.Model):
    id_type_utilisateur = db.Column(db.Integer, primary_key=True)
    type= db.Column(db.String(15), unique=True, nullable = False)

class Utilisateurs(db.Model):
    id_utilisateur = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(15), unique=True, nullable = False)
    password = db.Column(db.String(80))
    id_fk_type_utilisateur= db.Column(db.Integer, foreign_key= True)
    #clair = db.Column(db.String(80))

Utilisateurs_table = Table('utilisateurs', Utilisateurs.metadata)
Type_utilisateurs__table = Table('type_utilisateurs', TypeUtilisateur.metadata)





app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True


# config
server.config.update(
    #SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI='sqlite:///data2.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db.init_app(server)

# Setup the LoginManager for the server
#login_manager = LoginManager()
#login_manager.init_app(server)
#login_manager.login_view = '/login'

#User as base
# Create User class with UserMixin
#class Users(UserMixin, Users):
#    pass

create_db = html.Div([ html.H1("Création de la base de donnée, des tables et du login du créateur de la base."),
        dcc.Location(id='create_db', refresh=True),
        dcc.Input(id= "dbname",
            type= "text",
            placeholder= "Nom de la base de données",
            maxLength= 30),
        dcc.Input(id= "creatorname",
            type= "text",
            placeholder= "Pseudo du créateur de la base",
            maxLength= 30),
        dcc.Input(id= "password",
            type= "password",
            placeholder= "mot de passe",
            maxLength= 50),
        dcc.Input(id= "email",
            type= "text",
            placeholder= "e-mail",
            maxLength= 50),
        html.Button('Crée !', id='submit-val', n_clicks=0),
        html.Div(id='container-button-basic2')
    ])#end div




"""
create_user = html.Div([ html.H1("La base est créée ? Ajout d'utilisateur.")
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


app.layout= html.Div([
            html.Div(id='page-content', className='content')
            ,  dcc.Location(id='url', refresh=False)
        ])


@app.callback(
    Output('page-content', 'children')
    , [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return create_db
    #elif pathname == '/create_user':
    #    return create_user
    else:
        return '404'

@app.callback( [Output('container-button-basic2', "children")],
    [Input('submit-val', 'n_clicks')],
    [State('dbname', 'value'), State('creatorname', 'value'), State('password', 'value'), State('email', 'value')])
def create_database(n_clicks, dbase, creatorname, password, email):
    if dbase is not None and creatorname is not None and password is not None and email is not None:
        
        password_encrypted = generate_password_hash(password, method= 'sha256')

        if os.path.isfile(dbase)== False:
            conn = sqlite3.connect(dbase)
            conn.execute("CREATE TABLE type_utilisateur ("+\
            "id_type_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,"+\
            "type TEXT NOT NULL )")

            conn.execute("CREATE TABLE utilisateur ("+\
            "id_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,"+\
            "pseudo TEXT NOT NULL ," + \
            "mdp TEXT NOT NULL,"+\
            "email TEXT NOT NULL,"+\
            "id_fk_type_utilisateur INTEGER NO NULL,"+\
            "FOREIGN KEY(id_fk_type_utilisateur) REFERENCES type_utilisateur(id_type_utilisateur) )")

            conn.execute("INSERT INTO type_utilisateur (type) "+\
                "VALUES ('Créateur'), ('Super utilisateur'), ('Utilisateur'), ('Visiteur')")
            #conn.commit()

            conn.execute(f"INSERT INTO utilisateur (pseudo, mdp, id_fk_type_utilisateur, email) "+\
                f"VALUES ('{creatorname}', '{password_encrypted}', '{1}', '{email}')")
            conn.commit()

            data_base= dbase

       
        #pass
        #ins = Utilisateurs_table.insert().values(username=un,  password=hashed_password, email=em)
        #conn = engine.connect()
        #conn.execute(ins)
        #conn.close()
        return [html.Div([html.H2('Création réussi !'),
                    dcc.Link("Connexion à la base, et création d'utilisateurs.", href="/create_user")])]
    else:
        return [html.Div([html.H2("Si la base existe déjà, de nouveaux utilisateurs peuvent être crées."), 
                    dcc.Link("Connexion à la base, et création d'utilisateurs.", href="/login")])]







"""
@app.callback( [Output('container-button-basic', "children")],
    [Input('submit-val', 'n_clicks')],
    [State('username', 'value'), State('password', 'value'), State('email', 'value')] )
def insert_users(n_clicks, user, password, email):

    #---------------------------------------------------------------------
    #
    # OUVRIR LA BASE, si bdd= "" alors demander le nom de la base ? Le faire au login
    #
    #---------------------------------------------------------------------

    if user is not None and password is not None and email is not None:
        #---------------------------------------------------------------------
        #
        # IL FAUT CONTROLER L EXISTANCE DE L UTILISATEUR AVANT DE L INSERER
        #
        #---------------------------------------------------------------------
        
        password_encrypted = generate_password_hash(password, method='sha256')
        ins = Utilisateurs_table.insert().values(username= user,  password= password_encrypted, email= email)
        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        return [login]
    else:
        return [html.Div([html.H2('Already have a user account?'), dcc.Link('Click here to Log In', href='/login')])]

"""

if __name__ == '__main__':
    app.run_server(debug=True)
    #serve(app, host="0.0.0.0", port=8080)
