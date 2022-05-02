from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc

from apps import navbar2, glob

largeur= '1200px'

dfex= glob.df_examen[0:1000]
dfpat= glob.df_patient[0:1000]

tab_examen= dash_table.DataTable(id='container-button-timestamp',
    data= dfex.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in glob.df_examen.columns],
    export_format='csv',
    style_header={'backgroundColor': 'rgb(30, 30, 30)', "color" : glob.couleur_ecrit},
    style_table={'overflowX': 'auto',
                    'width' : largeur,
                    'height': '400px'},
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white',
        'textAlign':'left',
        'padding-left':'5px'
        }
)

tab_medecin= dash_table.DataTable(id='container-button-timestamp',
    data= glob.df_medecin.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in glob.df_medecin.columns],
    export_format='csv',
    style_header={'backgroundColor': 'rgb(30, 30, 30)', "color" : glob.couleur_ecrit},
    style_table={'overflowX': 'auto',
                    'width' : largeur,
                    'height': '400px'},
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white',
        'textAlign':'left',
        'padding-left':'5px'
        }
)

tab_patient= dash_table.DataTable(id='container-button-timestamp',
    data= dfpat.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in glob.df_patient.columns],
    export_format='csv',
    page_size= 10,
    style_header={'backgroundColor': 'rgb(30, 30, 30)', "color" : glob.couleur_ecrit},
    style_table={'overflowX': 'auto',
                    'width' : largeur,
                    'height': '400px'},
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white',
        'textAlign':'left',
        'padding-left':'5px'
        }
)
tab_diag= dash_table.DataTable(id='container-button-timestamp',
    data= glob.df_diagnostique.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in glob.df_diagnostique.columns],
    export_format='csv',
    page_size= 10,
    style_header={'backgroundColor': 'rgb(30, 30, 30)', "color" : glob.couleur_ecrit},
    style_table={'overflowX': 'auto',
                    'width' : largeur,
                    'height': '400px'},
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white',
        'textAlign':'left',
        'padding-left':'5px'
        }
)

layout = html.Div([
    navbar2.layout,
    html.Div([
        html.H2(children= "Base de donnée - données brutes", style= {"text-align": "center"}),
        html.P(""),
        dcc.Markdown(children= """Cette base comporte plusieurs tables.   
- La table examen: Comporte l'ensembles des données cliniques ainsi que l'identifiant
du patient ainsi que l'identifiant du medecin.
- La table médecin: Le nom des médecins prescripteurs.
- La table patient: Le nom des patients ayant participant à l'étude.
- La table diagnostique: Les différents diagnostiques réalisés
"""),
        html.P(""),

        html.Div([
            dbc.Tabs([
                dbc.Tab(tab_examen, label="Examen",label_style={"color":"#e5e7e9"}),
                dbc.Tab(tab_medecin, label="Medecins", label_style={"color":"#fefefe"}),
                dbc.Tab(tab_patient, label="Patients", label_style={"color":"#dbdbdb"}),
                dbc.Tab(tab_diag, label="Diagnostiques", label_style={"color":"#b9b9b9"}),
            ], style={"display": "flex", "align-items":"center", "align-content":"center"}),
        ], style={"display": "flex", "flex-direction": "column", "justify-content":"center",
            "align-items":"center", "align-content":"center"}),
        
        html.P(""),
        dcc.Link("Page d'acceuil", href = '/success'),

    ],),                    

], style={'background-color': glob.fond_ecran_formulaire,  "display": "flex", 
            "flex-direction": "column"}) #end div


"""
tab1_content2 = dbc.Row([html.H4(children='Logistic Regression', className="mt-4"),

            dash_table.DataTable(id='container-button-timestamp',
            data=res1.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in res1.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'margin-bot': '100px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
                'padding-left':'5px'
                },
            css=[ {'selector': '.row', 'rule': 'margin: 0'}]
            ),
            html.H6(children='On these different optimizations of the Logistic Regression model, we see that it is the vectorization with stopworld and ngramm which obtains the best result with an F1 at 0.892, despite the longer execution speed,', className="mt-4"),
            ])
"""

"""
# ------


###################

tab1_content = dash_table.DataTable(id='container-button-timestamp',
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            export_format='csv',
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
                'padding-left':'5px'
                }
            )

tab2_content = dash_table.DataTable(id='container-button-timestamp',
            data=df2.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df2.columns],
            export_format='csv',
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
             },
            css=[ {'selector': '.row', 'rule': 'margin: 0'}]
            )
dbc.Row([
    dbc.Tabs([
        dbc.Tab(tab1_content, label="Data Kaggle",label_style={"color":"#810303"}),
        dbc.Tab(tab2_content, label="Data World", label_style={"color":"#11337E"}),
    ]),
])




"""