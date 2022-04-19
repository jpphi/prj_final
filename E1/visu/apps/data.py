from dash import dcc
#import dash_html_components as html
from dash import html
#import dash


from apps import navbar2



layout = html.Div([ navbar2.layout,
                    dcc.Dropdown(
                        id='dropdown',
                        options=[{'label': i, 'value': i} for i in ['Day 1', 'Day 2']],
                        value='Day 1'),
                    html.Br(),
                    html.Div([dcc.Graph(id='graph')]),
                    dcc.Link("Page d'acceuil", href = '/success'),
            ]) #end div