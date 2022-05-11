#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Créé en mars 2022

Projet de fin d'étude Simplon
    Serveur support de l'application d'aide au diagnostique sur les maladies cardio-vasculaires
    glob.py; Fichier contenant les fonctions et variables globales. 
        Ce fichier doit se situer dans le sous-répertoire /apps

@auteur: jpphi
"""

import os
from joblib import load
import sqlite3
import pandas as pd

import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State

from app import app

# Couleurs...
Bleu_de_minuit= "#003366"
Bleu_marine= "#03224C"
Bleu_nuit= "#OF055B"
Bleu_outremer= "#15019B"
Bleu_outremer2= "#2B009A"

fond_ecran_reponse= "#007B94"
fond_ecran_formulaire= Bleu_de_minuit

couleur_ecrit= "#e5e7e9"
# base de données
bdd= "/home/jpphi/Documents/brief/ProjetFinDEtude/E1/datas/base_E1.db"
#bdp="/home/jpphi/Documents/brief/ProjetFinDEtude/E1/datas/base_E1.db"

df_examen= None
df_medecin= None
df_patient= None
df_diagnostique= None

repertoire= "/home/jpphi/Documents/brief/ProjetFinDEtude/E1/modeles/"

message_erreur= ""  #"TEST DE LA FONCTIONNALITE ALERTE"

def alerte(message= None):
        global message_erreur
        #print(message, " - ",message_erreur)

        aff_alerte= dbc.Alert([
                        html.H4(children= "Une erreur est survenu !", 
                                style= {"text-align" : "center"}),
                        html.H5(children= f"Le message envoyé par le code est: {message}"),
                        #html.P(),                       
                        html.H5(children= f"Dans glob.py on a le message: {message_erreur}"),
                        html.Div([
                                html.Button(id='email-button', children= "Envoyer le rapport d'erreur par mail"
                                        , n_clicks=0,style= {"text-align" : "center", "width":"300px"}),
                        ], style={"display":"flex", "justify-content":"center", 
                                "flex-direction": "raw"}),

                        ], color="danger" )
        return aff_alerte

def analyse(donnees_patient= None):
        global message_erreur

        # Analyse
        try:
                dict_algo_fichier = charge_modeles(repertoire= repertoire)
                algos = list(dict_algo_fichier.keys())
                fichiers= list(dict_algo_fichier.values())

                ch= {}
                score=0
                nb=0
                for f in fichiers:
                        nb+= 1
                        mod= load(repertoire+f"{f}")
                        score+= mod.predict([donnees_patient])[0]

                        prediction = mod.predict_proba([donnees_patient])
                        ch[f]= prediction[0]
                ch["score"]= f"{score}/{nb}"
                #print(f"dp: {donnees_patient}, ch: {ch}")
                donnees_patient.append(str(ch))
                #print(f"dp + ch: {donnees_patient}")
                return donnees_patient
        except:
                message_erreur= "Fonction analyse: except"
                return None

def charge_modeles(repertoire= None):
    """
    Retourne un dictionnaire dont la clé est le nom de l'algorithme et la valeur
        associée à la clé le nom du modèle binaire à charger.
    Entrée:
        nom du répertoire contenant les fichiers modeles
    Sortie:
        le dictionnaire{algo:nom_du_fichier}
    """
    assert type(repertoire)== str, "Le paramètre repertoire doit être de "+\
        "type chaine de caractères"
    liste_fichiers= os.listdir(repertoire)
    # On ne récupère que les fichiers d'extensions .h5
    liste_fichiers = [f for f in liste_fichiers if ".h5" in f]
    # Recherche du nom de l'algorithme contenue dans le nom fichier
    # Les fichiers doivent être écrit avec la syntaxe: algo_caractéristique.h5
    algo= [a.split("_")[0] for i,a in enumerate(liste_fichiers)]
    return {cle: valeur for cle, valeur in zip(algo, liste_fichiers)}

def creation_patient(identite_patient= None):
        global message_erreur

        #print(identite_patient)
        try:
        # Connexion à la base de donnée
                conn = sqlite3.connect(bdd)
                cur = conn.cursor()

                sql = "INSERT INTO patient (nom, prenom, naissance) VALUES(?,?,?)"
                #print(f"identite_patient: {identite_patient}")
                cur.execute(sql, (identite_patient[0].upper(), identite_patient[1].lower(), 
                        identite_patient[2]) )
                conn.commit()

                cur.close()
                conn.close()

                # Le patient est créé, on récupère son id
                idpatient= recherche_id(identite_patient= identite_patient)

                return idpatient
        except sqlite3.Error as error:
                message_erreur= f"Erreur dans la fonction creation_patient"
                return None


def enregistrement(retour_analyse= None, idpatient= None, idmedecin= None, cardio= None):

        global message_erreur

        try:
        # Connexion à la base de donnée
                conn = sqlite3.connect(bdd)
                cur = conn.cursor()
                
                sql = "INSERT INTO diagnostique (age, gender, height, weight, ap_hi, ap_lo, "+\
                        "cholesterol, gluc, smoke, alco, active, resultat_diag, idp, idmed, cardio) "+\
                        "VALUES(?,?,?,?,?,?, ?,?,?,?,?,?, ?,?, ?)"
                ligne= tuple(el for el in retour_analyse)

                cur.execute(sql, (ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], 
                        ligne[6], ligne[7], ligne[8], ligne[9], ligne[10], ligne[11],
                        idpatient, idmedecin, cardio) )
                conn.commit()

                cur.close()
                conn.close()
                return 1
        except sqlite3.Error as error:
                message_erreur= f"Erreur dans enregistrement lors de la connexion à SQLite: {error}"
                return None

def ouveture_base_medecin():
        global message_erreur

        try:
                conn = sqlite3.connect(bdd)
                cur = conn.cursor()

                query = conn.execute("SELECT * FROM medecin")
                cols = [column[0] for column in query.description]

                df_medecin= pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
                return 1
        except:
                message_erreur="Fonction ouverture_base_medecin: Impossible de lire la table"
                return None

def patient(identite_patient= None):
        global message_erreur

        #print("patient ", identite_patient)

        # Recherche id patient. S'il n'existe pas, crée le patient
        idp= recherche_id(identite_patient= identite_patient)
        if idp== None:
                message_erreur= "Problème dans la fonction recherche_id"
                return None
        elif idp== 0: # création d'un nouveau patient
                idp= creation_patient(identite_patient= identite_patient)
                if idp== None:
                        message_erreur= "fonction patient, échec création patient."
                        return None
        return idp

def recherche_id(identite_patient= None):
        global message_erreur

        #print(identite_patient)
        try:
        # Connexion à la base de donnée
                conn = sqlite3.connect(bdd)
                cur = conn.cursor()
 
                cur.execute("SELECT idp FROM patient WHERE nom= ? AND prenom= ? AND naissance= ?", 
                        ((identite_patient[0]).upper(),identite_patient[1].lower(),
                        identite_patient[2]))

                idp= cur.fetchall()
                n= len(idp)
                cur.close()
                conn.close()
        except sqlite3.Error as error:
                message_erreur= f"Erreur dans la fonction recherche_id lors de la "+\
                        f"connexion à SQLite: {error}"
                return None

        if n== 0: # le patient n'existe pas
                idp= 0
        elif n > 1: # plusieurs patients avec même nom, prénom et date de naissance
                message_erreur= "Erreur dans la fonction recherche_id. Patient enregistré "+\
                        f"plusieur fois: {idp}"
                return None
        else:
                return int( (idp[0])[0] )

@app.callback(
    Output(component_id= 'container-email', component_property= 'children'),
    Input('email-button', 'n_clicks'),)
def update_output(n_clicks):
    if n_clicks > 0:
        return