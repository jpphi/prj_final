from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc

from dash import html
from app import app

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Consultation données", href="/data"),
        dbc.DropdownMenuItem("Prédiction", href="/prediction"),
        dbc.DropdownMenuItem("logout", href="/logout"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

layout = dbc.Navbar(
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

