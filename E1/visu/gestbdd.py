#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le 26 décembre 2021

Projet de fin d'étude Simplon
    Gestionnaire de base de données

@author: jpphi
"""

from tkinter import *
from tkinter import ttk

def connexion():
    pass

root = Tk()
Entete = ttk.Frame(root, padding=10)
Entete.grid()
ligne= 0

ttk.Label(Entete, text="Utilitaire de gestion de base de données.").grid(column=0, row=ligne)
ligne+= 1

ttk.Label(Entete, text="Nom de la base: ").grid(column=0, row=ligne)
#ligne+= 1
nom_base= StringVar()
ttk.Entry(feuille, textvariable= nom_base).grid(column=0, row=ligne)
ligne+= 1
ttk.Label(feuille, text=nom_base.get()).grid(column=0, row=ligne)
ligne+= 1


ttk.Button(feuille, text="Connexion", command=connexion).grid(column=1, row=ligne)
ligne+= 1

ttk.Button(feuille, text="Bye !", command=root.destroy).grid(column=2, row=ligne)
root.mainloop()