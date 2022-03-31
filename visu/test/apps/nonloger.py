from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from apps import login

#from app import app


layout = html.Div([ dcc.Location(id='url_login_df', refresh=True)
            , html.Div([html.H2("Non loger !")
                    , html.Br()
                    , html.Div([login.layout])
                    , html.Br()
                    , html.Button(id='back-button', children='Go back', n_clicks=0)
                ]) #end div
        ]) #end div