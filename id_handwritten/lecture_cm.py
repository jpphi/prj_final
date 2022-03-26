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

import time

from PIL import Image, ImageOps

import tensorflow as tf

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
    return {cle: valeur for cle, valeur in zip(algo, liste_fichiers)}

def sauvegarde(nom):
    imgpil= Image.open("./images/tmp.png")
    imgpil.save(nom)
    

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
epaisseur = st.sidebar.slider("Epaisseur du trait: ", 1, 25, 15)
nom_algo = st.sidebar.selectbox("Choix du modèle d'algorithme:", algos,
                          key="recon_model_select")
fichier_modele= dict_algo_fichier[nom_algo]
sav= st.sidebar.button("Sauvegarde")

with st.form("Prédiction"):
    c1, c2= st.columns(2)
    with c1:
        recon_canvas = st_canvas(
            #epaisseur = st.slider("Epaisseur du trait: ", 1, 25, 15)
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
    with c2:
        irma_dit = st.form_submit_button("Prédiction")


    if irma_dit:
        # on charge l'image et on l'a converti
        img= recon_canvas.image_data
        image= Image.fromarray(img)
        image= image.resize((28,28))
        image= ImageOps.grayscale(image)
        image.save("./images/tmp.png")

        
        chiffre= np.array(image)/255.0
        
        # On charge le modèle
        id_algo= nom_algo[0:3]
        if id_algo== "Reg" or id_algo== "KNN":
            modele= load(f'./modeles/{fichier_modele}') 
            tab= list(modele.predict_proba([chiffre.ravel()])[0])
        #elif id_algo== "KNN":
            #modele= load(f'./modeles/{fichier_modele}') 
            #tab= list(modele.predict_proba([chiffre.ravel()])[0])
        elif id_algo== "CNN":
            modele = tf.keras.models.load_model(f'./modeles/{fichier_modele}')
            tab= list(modele.predict(chiffre.reshape(1,28,28)).reshape(10))
        
        # Convertion de l'image au format rgba en tableau numpy 2d
        
        prediction= tab.index(max(tab))
        #
if irma_dit:
    ch= ""
    for i in range(len(tab)):ch+= f"p({i})= {100*tab[i]:.2f} %, "
    col1, col2= st.columns(2)
    with col1:
        st.image(image)
    with col2:
        st.write(f"Chiffre lu: {prediction}")
        
    st.write(f"Tableau des probabilités:\n{ch[:-2]}")
    st.write(f"fichier modèle: {fichier_modele}")


with st.sidebar.container():
    st.markdown(
        "Pour effectuer une sauvegarde de l'image appuyez sur le boutton "
        "correspondant à la vérité terrain. L'image sera enregistrée sous "
        "la forme 'chiffre_numero_unique.png'."
    )
    c21, c22, c23, c24, c25= st.columns(5)
    with c21:
        chif0= st.button(("0"), key="b0")
        chif5= st.button(("5"), key="b5")
    with c22:
        chif1= st.button(("1"), key="b1")
        chif6= st.button(("6"), key="b6")
    with c23:
        chif2= st.button(("2"), key="b2")
        chif7= st.button(("7"), key="b7")
    with c24:
        chif3= st.button(("3"), key="b3")
        chif8= st.button(("8"), key="b8")
    with c25:
        chif4= st.button(("4"), key="b4")
        chif9= st.button(("9"), key="b9")
   
    if chif0:
        sauvegarde(f"0_{int(time.time())}.png")
    if chif5:
        sauvegarde(f"5_{int(time.time())}.png")
        
    if chif1:
        sauvegarde(f"1_{int(time.time())}.png")
        
    if chif6:
        sauvegarde(f"6_{int(time.time())}.png")
    
    if chif2:
        sauvegarde(f"2_{int(time.time())}.png")
        
    if chif7:
        sauvegarde(f"7_{int(time.time())}.png")
    
    if chif3:
        sauvegarde(f"3_{int(time.time())}.png")
    
    if chif8:
        sauvegarde(f"8_{int(time.time())}.png")
        
    if chif4:
        sauvegarde(f"4_{int(time.time())}.png")
    
    if chif9:
        sauvegarde(f"9_{int(time.time())}.png")
    
  
st.markdown(
    "Pour retrouver ce projet, ainsi que les projets réalisés lors de la "
    "formation 'Développeur Data IA' effectué à simplon: "
    " [jpphi - github](https://github.com/jpphi)")
