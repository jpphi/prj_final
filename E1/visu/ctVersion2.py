# https://ichi.pro/fr/comment-configurer-l-authentification-utilisateur-pour-les-applications-dash-a-l-aide-de-python-et-flask-118945949211473

from turtle import width
import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State

#from sqlalchemy import Table, create_engine, Table
#from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
#import sqlalchemy

from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash #, check_password_hash
import sqlite3
import warnings
import os
from flask_login import login_user, logout_user, current_user, LoginManager, UserMixin
import configparser

from apps import home, createdb, createuser

#warnings.filterwarnings("ignore")

db = SQLAlchemy()
#config = configparser.ConfigParser()

data_base=""

app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh= True),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children')
    , [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/createdb":
        return createdb.layout
    elif pathname == '/createuser':
        return createuser.layout
    else:
        return home.layout

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
                "VALUES ('Propriétaire'), ('Administrateur'), ('Utilisateur'), ('Visiteur')")

            conn.execute(f"INSERT INTO utilisateur (pseudo, mdp, id_fk_type_utilisateur, email) "+\
                f"VALUES ('{creatorname}', '{password_encrypted}', '{1}', '{email}')")

            # Mise à jour de la base de données
            conn.commit()

            conn.close()
            data_base= dbase
      
            return [html.Div([html.H2(f"Création de la base {dbase} réussi ! {creatorname} en est le propriétaire "+\
                "et a les privilèges d'administrateur de cette base."),
                         dcc.Link("Connexion à la base, et création d'utilisateurs.", href="/createuser")])]
        else:
            return [html.Div([html.H2(f"La base {dbase} existe déjà !"),
                        dcc.Link("Connexion à la base, et création d'utilisateurs.", href="/createuser")])]
    else:
        return [html.Div([html.H2("Pour créer la base de données vous devez renseigner tout les champs."),
                        dcc.Link("Cliquez ici pour revenir à la page d'accueil", href="/home")])]


@app.callback( [Output('container-button-basic3', "children")],
    [Input('submit-val', 'n_clicks')],
    [State('username', 'value'), State('password', 'value'), State('email', 'value'), State('type_user', 'value')] )
def insert_users(n_clicks, ps, pwd, em, typus): 
    global data_base
    
    #data_base= "test"

    if ps is not None and pwd is not None and em is not None:
        if data_base!= "":

            try:
                # Connection à la base
                conn= sqlite3.connect(data_base)
                cur= conn.cursor()

                # récupération de la liste des pseudo depuis la base de données
                cur.execute("SELECT pseudo FROM utilisateur")
                liste_pseudos_bdd = cur.fetchall()
                liste_pseudos= [el[0] for el in liste_pseudos_bdd]
 
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
                        dcc.Link("Cliquez ici pour revenir à la page d'accueil", href='/home')])]

                else: # Le pseudo exite déjà
                    conn.close()
                    return [html.Div([html.H2(f"L'utilisateur {ps} existe déjà !"),
                        dcc.Link("Cliquez ici pour revenir à la page d'accueil", href='/home')])]

 
            except:
                return [html.Div([html.H2(f"Erreur d'ouverture de la base {data_base}."), 
                    dcc.Link("Cliquez ici pour revenir à la page d'accueil", href='/home')])]
        
            #conn.close()
        else:
            return [html.Div([html.H2(f"Aucune base n'est ouverte."), 
                dcc.Link("Cliquez ici pour créer une base.", href="/createdb")])]
    else:
        return [html.Div([html.H2(f"Tout les champs doivent être rempli."),
            dcc.Link("Cliquez ici pour revenir à la page d'accueil", href="/home")])]


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
    #serve(app, host="0.0.0.0", port=8080)
