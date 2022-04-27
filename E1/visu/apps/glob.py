import os
from joblib import load

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

df_examen= None
df_medecin= None
df_patient= None

repertoire= "/home/jpphi/Documents/brief/ProjetFinDEtude/E1/modeles/"

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
    # On ne récupère que les fichiers d'extensions .modele
    liste_fichiers = [f for f in liste_fichiers if ".h5" in f]
    # Recherche du nom de l'algorithme contenue dans le nom fichier
    # Les fichiers doivent être écrit avec la syntaxe: algo_caractéristique.modele
    algo= [a.split("_")[0] for i,a in enumerate(liste_fichiers)]
    return {cle: valeur for cle, valeur in zip(algo, liste_fichiers)}

def analyse(dp= None):

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
                        score+= mod.predict([dp])[0]

                        prediction = mod.predict_proba([dp])
                        ch[f]= prediction[0]
                ch["score"]= f"{score}/{nb}"
                return str(ch)
        except:
                return None

def alerte(message= None):
        pass
def enregistrement(dp= None, ra= None):
        pass
"""
form=        html.Div([
                html.Div([
                        html.P(children= "Utilisateur :"),
                        dcc.Input(placeholder="Nom", type='text', id='uname-box',
                                style= {"text-align": "center", "height": "30px"}, ), #value= "toto"
                ], style= {"display":"flex", "text-align": "center", "flex-direction":"raw",
                        "align-content":"center", "gap":"20px", "justify-content":"space-around"},),

                html.Div([
                        html.P(children= "Mot de passe :"),
                        dcc.Input(placeholder="Mot de passe", type='password', id='pwd-box',
                                style= {"text-align": "center", "height": "30px"}), #, value="toto"
                ], style= {"display":"flex", "text-align": "center", "flex-direction":"raw",
                        "align-content":"center", "gap":"20px", "justify-content":"space-around"}),

                html.Button(children='Connexion', n_clicks=0, type='submit',
                                id='login-button', style= {"text-align": "center",
                                "height": "30px"}),

                ],style={"display": "flex","flex-direction": "raw", 
                "background-color": fond_ecran_formulaire, "justify-content":"space-around",
                "align-items":"baseline"
                }),

"""
