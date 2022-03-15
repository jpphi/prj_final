# https://ichi.pro/fr/comment-configurer-l-authentification-utilisateur-pour-les-applications-dash-a-l-aide-de-python-et-flask-118945949211473

from turtle import width
import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State

#from sqlalchemy import Table, create_engine, Table
#from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash #, check_password_hash
import sqlite3
import warnings
import os
from flask_login import login_user, logout_user, current_user, LoginManager, UserMixin
import configparser

#warnings.filterwarnings("ignore")

db = SQLAlchemy()
config = configparser.ConfigParser()

data_base=""

db = SQLAlchemy()
config = configparser.ConfigParser()
"""
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
"""


app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

"""
# config
server.config.update(
    #SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI='sqlite:///data2.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
"""

#db.init_app(server)

create_db = html.Div(id='container-button-basic2', children= [
    html.H1("Création de la base de donnée, des tables et du login du créateur de la base."),
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
    html.Div(id='container-button-basic', children= [html.P(children="Ici et maintenant")])
    ])#end div


create_user = html.Div(children= [ html.H1("La base est créé ? Ajout d'utilisateur."),
    dcc.Location(id='create_user', refresh=True),
    dcc.Input(id="username", type="text", placeholder="user name", maxLength =15,
        style= {'display': 'inline-block'}),
    dcc.Input(id="password", type="password", placeholder="password",
        style= {'display': 'inline-block'}),
    dcc.Input(id="email", type="email", placeholder="email", maxLength = 50,
        style= {'display': 'inline-block'}),
    dcc.Dropdown(id='type_user',
        options=[{'label': "Administrateur", 'value': 2}, {'label': "Utilisateur", 'value': 3},
            {'label': "Visiteur", 'value': 4}], value= 2, style= {'display': 'inline-block'}),
    html.Br(),
    html.Button('Create User', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic3'),
    ])#end div



"""
app.layout= html.Div([
            html.Div(id='page-content', className='content')
            ,  dcc.Location(id='url', refresh=True)
        ])
"""

app.layout= html.Div(id='page-content', className='content', children= [dcc.Location(id='url', refresh=True)])


@app.callback(
    Output('page-content', 'children')
    , [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return create_db
    elif pathname == '/create_user':
        return create_user
    else:
        return '404'

@app.callback( [Output('container-button-basic', "children")],
    [Input('submit-val', 'n_clicks')],
    [State('dbname', 'value'), State('creatorname', 'value'), State('password', 'value'), State('email', 'value')])
def create_database(n_clicks, dbase, creatorname, password, email):
    global data_base

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

            conn.execute(f"INSERT INTO utilisateur (pseudo, mdp, id_fk_type_utilisateur, email) "+\
                f"VALUES ('{creatorname}', '{password_encrypted}', '{1}', '{email}')")

            # Mise à jour de la base de données
            conn.commit()

            conn.close()
            data_base= dbase
      
            return [html.Div([html.H2(f"Création de la base {dbase} réussi ! {creatorname} à les privilèges d'administrateur de cette base."),
                         dcc.Link("Connexion à la base, et création d'utilisateurs.", href="/create_user")])]
        else:
            return [html.Div([html.H2(f"La base {dbase} existe déjà !"),
                        dcc.Link("Connexion à la base, et création d'utilisateurs.", href="/")])]
    else:
        return [html.Div([html.H2("Pour créer la base de données vous devez renseigner tout les champs."),
                        dcc.Link("Connexion à la base, et création d'utilisateurs.", href="/create_user")])]


@app.callback( [Output('container-button-basic3', "children")],
    [Input('submit-val', 'n_clicks')],
    [State('username', 'value'), State('password', 'value'), State('email', 'value'), State('type_user', 'value')] )
def insert_users(n_clicks, ps, pwd, em, typus): 
    global data_base
    
    data_base= "toto.toto" #"Existe.pas"

    if ps is not None and pwd is not None and em is not None:
        if data_base!= "":

            try:
                # Connection à la base
                conn= sqlite3.connect(data_base)
                cur= conn.cursor()

                # récupération de la liste des pseudo depuis la base de données
                cur.execute("SELECT pseudo FROM utilisateur")
                liste_pseudos_bdd = cur.fetchall()
                liste_pseudos= []
                for el in liste_pseudos_bdd: 
                    #print(el[0])
                    liste_pseudos.append(el[0])

                #print(liste_pseudos,"\n",l)
                # garantir l'unicité du pseudo
                if ps not in liste_pseudos: 
                    print(liste_pseudos)
                    password_encrypted = generate_password_hash(pwd, method='sha256')

                    cur.execute(f"INSERT INTO utilisateur (pseudo, mdp, id_fk_type_utilisateur, email) "+\
                        f"VALUES ('{ps}', '{password_encrypted}', '{typus}', '{em}')")

                    # Mise à jour de la base de données
                    conn.commit()

                    conn.close()

                    return [html.Div([html.H2(f"Utilisateur {ps} créé."), 
                        dcc.Link('Click here to Log In', href='/create_user')])]
                else: # Le psodo exite déjà
                    conn.close()

                    return [html.Div([html.H2(f"L'utilisateur {ps} existe déjà !")])]
                    #, dcc.Link('Click here to Log In', href='/create_user')

                #print(pseudo)
                #conn.execute(f"SELECT utilisateur (pseudo, mdp, id_fk_type_utilisateur, email) "+\
                #    f"VALUES ('{pseudo}', '{password_encrypted}', '{type_user}', '{email}')")
                #return [html.Div([html.H2(f"list_pseudo {list_pseudos} \n. mise nen liste: {mise_en_list_pseudo}"), 
                #    dcc.Link('Click here to Log In', href='/create_user')])]

            except:
                return [html.Div([html.H2(f"Erreur d'ouverture de la base {data_base}."), 
                    dcc.Link('Click here to Log In', href='/create_user')])]
        
            #conn.close()
        else:
            return [html.Div([html.H2(f"La base {data_base} n'est pas ouverte."), dcc.Link('Click here to Log In', href='/create_user')])]
    else:
        return [html.Div([html.H2(f"Tout les champs doivent être rempli: bdd {data_base}"), dcc.Link('Else insert user', href='/create_user')])]


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
    #serve(app, host="0.0.0.0", port=8080)
