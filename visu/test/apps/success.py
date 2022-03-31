from dash import dcc
#import dash_html_components as html
from dash import html
#import dash

from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc

from app import app

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("data", href="/data"),
        dbc.DropdownMenuItem("success", href="/success"),
        dbc.DropdownMenuItem("logout", href="/logout"),
        dbc.DropdownMenuItem("login", href="/login")
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="./images/image_test.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Emotions Wheel DASH", className="ml-2")),
                    ],
                    align="center",
                    #no_gutters=True,
                ),
                href="/",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)




layout = html.Div([dcc.Location(id='url_login_success', refresh=True),
            navbar,
            html.Div([html.H2('Login successful.'),
            html.Br(),
            html.P('Select a Dataset'),
            dcc.Link('Data', href = '/data'),
            ]), #end div
            html.Div([html.Br(),
            html.Button(id='back-button', children='Go back', n_clicks=0),
                ]) #end div
        ]) #end div