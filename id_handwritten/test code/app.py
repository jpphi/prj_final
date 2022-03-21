#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:36:09 2022

@author: jpphi
"""

import streamlit as st
from streamlit_drawable_canvas import st_canvas
import os
#import app_utils as utils
from PIL import Image, ImageOps

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D


import numpy as np

st.set_page_config("Lecture caractères manuscrits")
st.title("🍀 VAE Playground")
title_img = Image.open("title_img.png")

st.image(title_img)
st.markdown(
    "This is a simple streamlit app to showcase how different VAEs "
    "function and how the differences in architecture and "
    "hyperparameters will show up in the generated images. \n \n"
    "In this playground there will be two scenarios that you can use to "
    "interact with the models:"
)
st.markdown(
    """
    1. **Image Reconstruction:** <br>
    Observe quality of image reconstruction
    2. **Image Interpolation:** <br>
    Sample images equally spaced between 2 drawn images. Observe tradeoff
    between image reconstruction and latents space regularity
    """, unsafe_allow_html=True
)

#  the first is a reconstruction one which is "
# "used to look at the quality of image reconstruction. The second one is "
# "interpolation where you can generate intermediary data points between "
# "two images. From here this you can analyze the regularity of the latent "
# "distribution."

st.markdown(
    "There are also two different architectures. The first one is the vanilla "
    "VAE and the other is the convolutional VAE which uses convolutional layers"
    " for the encoder and decoder. "
    "To find out more check this accompanying"
    " [blogpost](https://towardsdatascience.com/beginner-guide-to-variational-autoencoders-vae-with-pytorch-lightning-13dbc559ba4b)"
)
st.subheader("Hyperparameters:")
st.markdown(
    "- **alpha**: Weight for reconstruction loss, higher values will lead to better"
    "image reconstruction but possibly poorer generation \n"
    "- **dim**: Hidden Dimension of the model."
)





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


dict_algo_fichier = charge_modeles(repertoire= "./modeles/")
algo = list(dict_algo_fichier.keys())
fichier= list(dict_algo_fichier.values())

##file_name_map = load_model_files("./modeles/")
##files = list(file_name_map.keys())
#"""
st.header("🖼️ Image Reconstruction", "recon")

st.write(f"{dict_algo_fichier}")

with st.form("reconstruction"):
    nom_algo = st.selectbox("Choose Model:", algo,
                              key="recon_model_select")
    fichier_modele= dict_algo_fichier[nom_algo]
    #modele = tf.keras.models.load_model(f'./modeles/{fichier_modele}')
    #modele = tf.keras.models.load_model('CNN_1.modele')
    

    recon_canvas = st_canvas(
        # Fixed fill color with some opacity
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=8,
        stroke_color="#FFFFFF",
        background_color="#000000",
        update_streamlit=True,
        height=150,
        width=150,
        drawing_mode="freedraw",
        key="recon_canvas",
    )
    submit = st.form_submit_button("Perform Reconstruction")
    if submit:
        modele = tf.keras.models.load_model(f'./modeles/{fichier_modele}')
        img= recon_canvas.image_data
        
        # Convertion de l'image au format rgba en tableau numpy 2d
        image= Image.fromarray(img)
        image= image.resize((28,28))
        image = ImageOps.grayscale(image)
        chiffre= np.array(image)/255.0
        
        tab= list(modele.predict(chiffre.reshape(1,28,28)).reshape(10))
        prediction= tab.index(max(tab))
        #
if submit:
    st.image(image)
    st.write(f"Chiffre lu: {prediction}")

"""


st.header("🔍 Image Interpolation", "interpolate")
with st.form("interpolation"):
    model_name = st.selectbox("Choose Model:", files)
    inter_model_name = file_name_map[model_name]
    stroke_width = 8
    cols = st.beta_columns([1, 3, 2, 3, 1])

    with cols[1]:
        canvas_result_1 = st_canvas(
            # Fixed fill color with some opacity
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=stroke_width,
            stroke_color="#FFFFFF",
            background_color="#000000",
            update_streamlit=True,
            height=150,
            width=150,
            drawing_mode="freedraw",
            key="canvas1",
        )

    with cols[3]:
        canvas_result_2 = st_canvas(
            # Fixed fill color with some opacity
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=stroke_width,
            stroke_color="#FFFFFF",
            background_color="#000000",
            update_streamlit=True,
            height=150,
            width=150,
            drawing_mode="freedraw",
            key="canvas2",
        )
    submit = st.form_submit_button("Perform Interpolation")
    if submit:
        inter_model = utils.load_model(inter_model_name)
        inter_tens1 = utils.canvas_to_tensor(canvas_result_1)
        inter_tens2 = utils.canvas_to_tensor(canvas_result_2)
        inter_output = utils.perform_interpolation(
            inter_model, inter_tens1, inter_tens2
        )
if submit:
    st.image(inter_output)

"""
st.write(
    """
    ## 💡 Interesting Note:
    At low values of alpha, we can see the phenomenon known as the **posterior
    collapse**. This is when the loss function does not weight reconstruction 
    quality sufficiently and the reconstructed images look like digits but 
    nothing like the input.
    Essentially what happens is that the encoder encodes data points to a 
    random gaussian distribution (to minimize KL Loss) but this does not give 
    sufficient information to the decoder. In this case our decoder behaves 
    very similarly to a Generative Adversarial Network (GAN) which generates 
    images from random noise. 
    """
)
    
