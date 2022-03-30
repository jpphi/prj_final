from dash import dcc
#import dash_html_components as html
from dash import html
#import dash

from apps import login



layout = html.Div([ dcc.Location(id='url_login_df', refresh=True)
            , html.Div([html.H2('Log in Failed. Please try again.')
                    , html.Br()
                    , html.Div([login.layout])
                    , html.Br()
                    , html.Button(id='back-button', children='Go back', n_clicks=0)
                ]) #end div
        ]) #end div