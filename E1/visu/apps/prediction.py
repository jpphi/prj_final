from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State

import datetime

from apps import navbar2, glob
from app import app


layout = html.Div([navbar2.layout,

            html.H2("Prédiction du risque cardio-vasculaire.", style={"text-align":"center"}),

            html.P(children= ""),

            html.H4("Fiche patient.", style={"text-align":"center"}),

            # Boutons radios. 1er goupe de 4 entrées
            html.Div([ 
                html.Div([
                    html.P(children= "Genre :"),
                    dcc.RadioItems(id="ri-genre", options=[{'label': ' Homme', 'value': 'h'},
                        {'label': ' Femme', 'value': 'f'}], value= "h",
                        labelStyle={'display': 'flex', "gap": "5px"},),
                    ], style={"display": "flex", "align-items":"flex-start", "gap": "10px",
                            "justify-content":"space-between",}),

                html.Div([           
                    html.P(children= "Activité physique :"),
                    dcc.RadioItems(id="ri-activite", options=[{'label': ' Actif', 'value': 'act'},
                        {'label': ' Inactif', 'value': 'inact'},], value= "act",
                        labelStyle={'display': 'flex',"gap":"5px"}),
                ], style={"display": "flex", "align-items":"flex-start", "gap": "10px",
                            "justify-content":"space-around",}),

                html.Div([           
                    html.P(children= "Tabagisme :"),
                    dcc.RadioItems(id= "ri-tabac", options=[{'label': ' Fumeur', 'value': 'fum'},
                        {'label': ' Non fumeur', 'value': 'nfum'}, ],  value= "nfum",
                        labelStyle={'display': 'flex', "gap":"5px"}),
                ], style={"display": "flex", "align-items":"flex-start",
                            "justify-content":"space-around", "gap": "10px"}),

                html.Div([           
                    html.P(children= "Alcool :"),
                    html.P("   "),
                    dcc.RadioItems(id= "ri-alcool", options=[{'label': ' Oui', 'value': 'alc'},
                        {'label': " Non", 'value': 'nalc'}, ],  value= "alc",
                        labelStyle={'display': 'flex', "gap":"5px"}),
                ], style={"display": "flex", "align-items":"flex-start",
                            "justify-content":"space-around", "gap": "10px"}),
            ], style={'background-color': glob.fond_ecran_formulaire,  "display": "flex", "align-items":"baseline",
            "justify-content":"space-around",}),

            html.P(children= ""),

            # 2 dropdown 2 input. 2ème goupe de 4 entrées
            html.Div([

                html.Div([           
                    html.P(children= "Glucose :"),
                    dcc.Dropdown(id='dd-glucose', options= [1,2,3], placeholder= '1, 2 ou 3',
                        style= {"width":"100px", "color": glob.fond_ecran_formulaire,},
                        value= 1, ),
                ], style={"display": "flex", "align-items":"baseline",
                            "justify-content":"space-around", "gap": "10px"}),              

                html.Div([           
                    html.P(children= "Cholesterol :"),
                    dcc.Dropdown(id='dd-cholesterol', options= [1,2,3], placeholder= '1, 2 ou 3',
                        style= {"width":"100px", "color": glob.fond_ecran_formulaire},
                        value= 1,), 
                ], style={"display": "flex", "align-items":"baseline",
                            "justify-content":"space-around", "gap": "10px", "width":"50 %"}),

                html.Div([           
                    html.P(children= "Taille (en cm):"),
                    dcc.Input(placeholder="[50;280]", type='text', id='i-taille',
                        min= 50, max= 280, style= {"text-align": "center", "width":"100px"},
                        value= 185,),
                ], style={"display": "flex", "align-items":"baseline", "gap": "10px",
                            "justify-content":"space-around",}),
                
                html.Div([           
                    html.P(children= "Poids (en kg):"),
                    dcc.Input(placeholder="[10;650]", type='text', id='i-poids',
                        min= 10, max= 650, style= {"text-align": "center", "width":"100px"},
                        value= 90,),
                ], style={"display": "flex", "align-items":"baseline", "gap": "10px",
                            "justify-content":"space-around", }),
            
            ], style={'background-color': glob.fond_ecran_formulaire,  "display": "flex",
            "justify-content":"space-around", "align-items":"center"}),
            #"flex-direction": "raw", 
            #"flex-wrap": "wrap", }

            html.P(children= ""),

            # 2 date 2 input. 3ème goupe de 4 entrées
            html.Div([
                html.Div([           
                    html.P(children= "PA systolique"),
                    dcc.Input(placeholder="[10;300]", type='text', id='i-pasys',
                        min= 10, max= 300, style= {"text-align": "center", "width":"100px"},
                        value= 150,),
                ], style={"display": "flex", "align-items":"baseline",
                            "justify-content":"space-around", "gap": "10px"}),
                
                html.Div([           
                    html.P(children= "PA diastolique"),
                    dcc.Input(placeholder="[10;300]", type='text', id='i-padia',
                        min= 10, max= 300, style= {"text-align": "center", "width":"100px"},
                        value= 90),
                ], style={"display": "flex", "align-items":"baseline",
                            "justify-content":"space-around", "gap": "10px"}),

                html.Div([           
                    html.P(children= "Date de naissance :"),
                    dcc.DatePickerSingle(
                        id='dt-naissance',
                        min_date_allowed= datetime.date(1900, 1, 1),
                        max_date_allowed= datetime.date.today(), #(2017, 9, 19)
                        initial_visible_month= datetime.date(1965, 11, 5),
                        date= datetime.date(1965, 11, 5),
                        display_format= "DD-MM-Y"
                    ),
                ], style={"display": "flex", "align-items":"baseline",
                            "justify-content":"space-around", "gap": "10px"}),
            
                html.Div([           
                    html.P(children= "Date de la consultation :"),
                    dcc.DatePickerSingle(
                        id='dt-consultation',
                        min_date_allowed= datetime.date(1900, 1, 1),
                        max_date_allowed= datetime.date.today(), #(2017, 9, 19)
                        #initial_visible_month= datetime.date.today(),
                        date= datetime.date.today(),
                        display_format= "DD-MM-Y"
                    ),
                ], style={"display": "flex", "align-items":"baseline",
                            "justify-content":"space-around", "gap": "10px"}),

            ], style={'background-color': glob.fond_ecran_formulaire,  "display": "flex",
            "justify-content":"space-around", "align-items":"baseline"}),
            #"flex-direction": "raw", 
            #"flex-wrap": "wrap", }

            html.P(children= ""),

            html.Div([           
                html.Button(id='analyse-button', children= "Lancer l'analyse", n_clicks=0,
                style={"text-align":"center"}),
                ],style={"display": "flex", "align-items":"center", "align-content":"center",
                            "justify-content":"space-around",#"width": "150px",
                            'background-color': glob.fond_ecran_formulaire,
                            "flex-direction": "column"}),

            html.P(children= ""),

            html.H4("Liste des algorithmes.", style={"text-align":"center"}),

            html.P(children= ""),
            #html.Div(id='output-container-date-picker-single'),

            # Zone d'analyse
            html.Div([
                html.H2(children= "Veuillez remplir tout les champs du formulaire "+\
                    "avant de lancer une analyse.", style= {"text-align" : "center"}),

                html.Div(id='container-button-basic', children= ""),
            ], style={'background-color': glob.fond_ecran_reponse, "display": "flex",
            "flex-direction": "column", "justify-content":"space-between"})   

        ], style={'background-color': glob.fond_ecran_formulaire, "display": "flex",
            "flex-direction": "column", "justify-content":"space-between"}) #end div






@app.callback(
    Output(component_id= 'container-button-basic', component_property= 'children'),
    Input('analyse-button', 'n_clicks'),
    State('ri-genre', 'value'), State("ri-activite", 'value'), State("ri-tabac", "value"),
    State("ri-alcool", "value"), State("dd-glucose", "value"), State("dd-cholesterol", "value"),
    State("i-taille", "value"), State("i-poids", "value"), State("i-pasys", "value"),
    State("i-padia", "value"), State("dt-consultation", "date"), State("dt-naissance", "date"),
    )
def update_output(n_clicks, rigenre, riactivite, ritabac, rialcool, ddglucose,
    ddcholesterol, itaille, ipoids, ipasys, ipadia, dtconsultation, dtnaissance):
    if n_clicks > 0:
        if rigenre== None:
            return "Erreur: Veuillez renseigner le genre."
        else:
            rigenre = 0 if rigenre== 'h' else 1

        if riactivite== None:
            return "Erreur: Veuillez renseigner l'activité."
        else:
            riactivite = 1 if riactivite== 'act' else 0

        if ritabac== None:
            return "Erreur: Veuillez renseigner tabagisme."
        else:
            ritabac = 1 if ritabac== 'fum' else 0

        if rialcool== None:
            return "Erreur: Veuillez renseigner la consommation d'alcool."
        else:
            rialcool = 1 if rialcool== 'alc' else 0

        if ddglucose== None:
            return "Erreur: Veuillez renseigner le niveau de glucose."
        if ddcholesterol== None:
            return "Erreur: Veuillez renseigner le taux de cholesterol."

        if itaille== None or itaille== "":
            return "Erreur: Veuillez renseigner la taille."
        if ipoids== None or ipoids== "":
            return "Erreur: Veuillez renseigner le poids."
        if ipasys== None or ipasys== "":
            return "Erreur: Veuillez renseigner PA systolique."
        if ipadia== None or ipadia== "":
            return "Erreur: Veuillez renseigner PA diastolique."

        if dtnaissance== None:
            return "Erreur: Veuillez renseigner la date de naissance."
        if dtconsultation== None:
            return "Erreur: Veuillez renseigner la date de consultation."

        else:
            d1= datetime.datetime.strptime(dtnaissance,'%Y-%m-%d')
            d2= datetime.datetime.strptime(dtconsultation,'%Y-%m-%d')
            donnees_patient= [(d2-d1).days, rigenre, itaille, ipoids, ipasys, ipadia,
                ddcholesterol, ddglucose, ritabac, rialcool, riactivite]
            
            retour_analyse= glob.analyse(donnees_patient)

            if retour_analyse== None:
                glob.alerte("Erreur: Analyse impossible")
            else: #Enregistrement en base
                glob.enregistrement(ra= retour_analyse, dp= donnees_patient)

            return f"{retour_analyse} {n_clicks}, {rigenre}, {riactivite}, {ritabac}, {rialcool}, {ddglucose},"+\
                f"{ddcholesterol}, {itaille}, {ipoids}, {ipasys}, {ipadia}, {dtconsultation},"+\
                f"{dtnaissance} - {(d2-d1).days}"
    



######################




@app.callback(
    Output('output-container-date-picker-single', 'children'),
    Input('my-date-picker-single', 'date'))
def update_output(date_value):
    string_prefix = 'You have selected: '
    if date_value is not None:
        date_object = datetime.date.fromisoformat(date_value)
        date_string = date_object.strftime('%B %d, %Y')
        return string_prefix + date_string


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'


