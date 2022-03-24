#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codé en mars 2022

Projet fin détude Simplon

@author: Jean-Pierre Maffre
"""

#-------------- Import, variables globales et fonctions  ----------------------

import streamlit as st
from streamlit_drawable_canvas import st_canvas
import os

from PIL import Image, ImageOps

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

from joblib import load

import numpy as np

def charge_modeles(repertoire= None):
    """
    Retourne un dictionnaire dont la clé est le nom de l'algorithme et la valeur
        associée à la clé le nom du modèle binaire à charger.
    Entrée:
        nom du répertoire contenant les fichiers modele
    Sortie:
        le dictionnaire{algo:nom_du_fichier}
    """
    assert type(repertoire)== str, "Le paramètre repertoire doit être de type chaine de caractère"
    
    liste_fichiers= os.listdir(repertoire)
    # On ne récupère que les fichiers d'extensions .modele
    liste_fichiers = [f for f in liste_fichiers if ".modele" in f]
    # Recherche du nom de l'algorithme contenue dans le nom fichier
    # Les fichiers doivent être écrit avec la syntaxe: algo_caractéristique.modele
    algo= [a.split("_")[0] for i,a in enumerate(liste_fichiers)]
    #print(liste_fichiers)
    #print(algo)
    return {cle: valeur for cle, valeur in zip(algo, liste_fichiers)}

#-------------------------- Programme principal -------------------------------

dict_algo_fichier = charge_modeles(repertoire= "./modeles/")
algos = list(dict_algo_fichier.keys())
fichiers= list(dict_algo_fichier.values())

#------------------------ Construction de la page -----------------------------
st.set_page_config("Lecture caractères manuscrits")
st.title("🍀 Lecture caractères manuscrits")
Image_illustration = Image.open("./images/image_titre.png")
 
st.image(Image_illustration)
st.markdown(
    "Aprés la théorie et l'étude sur les différents algorithmes "
    "sur des données provenant du même dataset, il est temps de "
    "passer à la pratique !\n \n"
    "Comme on peut le voir sur l'image illustrant cette page il y "
    "une trés grande diversité dans les écritures. Nos modèles ne "
    "devrait donc pas avoir de difficultés majeures pour s'adapter "
    "à un style d'écriture qu'il n'a jamais rencontré...\n\n"
)

st.subheader("De la théorie, à la pratique:")

# Epaisseur du tracé
epaisseur = st.slider("Epaisseur du trait: ", 1, 25, 15)

with st.form("Prédiction"):
    nom_algo = st.selectbox("Choix du modèle d'algorithme':", algos,
                              key="recon_model_select")
    fichier_modele= dict_algo_fichier[nom_algo]
    #modele = tf.keras.models.load_model(f'./modeles/{fichier_modele}')
    #modele = tf.keras.models.load_model('CNN_1.modele')
    
    recon_canvas = st_canvas(
        # Fixed fill color with some opacity
        fill_color="rgba(0, 165, 0, 0.3)", #"rgba(255, 165, 0, 0.3)"
        stroke_width= epaisseur,
        stroke_color="#FFFFFF",
        background_color="#000000",
        update_streamlit=True,
        height=280,
        width=280,
        drawing_mode= "freedraw",
        key="recon_canvas",
    )
    submit = st.form_submit_button("Prédiction")
    if submit:
        # on charge l'image et on l'a converti
        img= recon_canvas.image_data
        image= Image.fromarray(img)
        image= image.resize((28,28))
        image = ImageOps.grayscale(image)
        chiffre= np.array(image)/255.0
        
        # On charge le modèle
        id_algo= nom_algo[0:3]
        if id_algo== "Reg":
            modele= load(f'./modeles/{fichier_modele}') 
            tab= list(modele.predict_proba([chiffre.ravel()])[0])
        elif id_algo== "KNN":
            modele= load(f'./modeles/{fichier_modele}') 
            tab= list(modele.predict_proba([chiffre.ravel()])[0])
        elif id_algo== "CNN":
            modele = tf.keras.models.load_model(f'./modeles/{fichier_modele}')
            tab= list(modele.predict(chiffre.reshape(1,28,28)).reshape(10))
        
        # Convertion de l'image au format rgba en tableau numpy 2d
        
        prediction= tab.index(max(tab))
        #
if submit:
    ch= ""
    for i in range(len(tab)):ch+= f"p({i})= {100*np.round(tab[i],4)}, "
    st.image(image)
    st.write(f"Chiffre lu: {prediction}")
    st.write(f"Tableau des probabilités:\n{ch[:-2]}")
    st.write(f"fichier modèle: {fichier_modele}")

st.markdown(
    "Pour retrouver ce projet, ainsi que les projets réalisés lors de la "
    "formation 'Développeur Data IA' effectué à simplon: "
    " [jpphi - github](https://github.com/jpphi)")
