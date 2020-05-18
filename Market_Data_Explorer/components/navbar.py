import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from fmp.constants import FUNDS
from .utils import *
from .base import BaseBlock
from .callbacks import *

PLOTLY_LOGO = 'https://raw.githubusercontent.com/plotly/dash-sample-apps/master/apps/dash-web-trader/assets/dash-logo-new.png'


class DropDown(BaseBlock):

    dropdown_id = "dropdown-" + random_string()

    def __init__(self, app, options=None):
        """
        options is an array of dicts with key/value pairs for label and value
        options
        """
        super().__init__(app)
        self.options = options

    def layout(self):

        if not self.options:
            self.options = ['']

        layout = dbc.Col(
            dcc.Dropdown(
                id=self.dropdown_id,
                options=self.options,
                value=self.options[0]['value'],
                style={
                    "margin-top": "3px",
                    "width": "170px",
                    "float": "right",
                }
            ),

        )
        return layout

    def callback(self):
        pass


class SearchBar(BaseBlock):
    searchbar_id = "searchbar-" + random_string()
    search_id = "search-" + random_string()
    button_id = "searchbutton-" + random_string()

    def __init__(self, app):
        super().__init__(app)

    def layout(self):
        layout = html.Div(
            id=self.searchbar_id,
            children=dbc.Row(
             [
                 dbc.Col(
                     DropDown(self.app,
                              generate_dropdown_options([key for key in FUNDS.keys()])).layout(),
                     width="auto",
                 ),
                 dbc.Col(
                     dbc.Input(id="input", placeholder="Type something..."),
                     width=6
                 ),
                 dbc.Col(
                     dbc.Button("Search", id=self.button_id, color="primary", className="ml-2"),
                     width="auto",
                 ),

             ],
             no_gutters=True,
             className="sm-auto flex-nowrap mt-3 mt-sm-0",
             align="right",

            )
        )
        return layout

    def callback(self):
        pass


class NavBar(BaseBlock):
    navbar_id = "navbar-" + random_string()

    def __init__(self, app):
        super().__init__(app)

    def layout(self):
        layout = html.Div(
            id=self.navbar_id,
            children=dbc.Navbar(
                [
                    dbc.Col(
                        dbc.Row(
                            [
                                dbc.Col(html.H3("Investig8", style={
                                    "height": "30px",
                                    "margin-left": "-20px",
                                    "color": "#d9e3f2"
                                    })
                                ),
                            ],
                            align="center",
                            no_gutters=True,
                        ),

                    ),
                    dbc.Col([
                        dbc.NavbarToggler(id="navbar-toggler"),
                        dbc.Collapse(
                            [
                                html.Div(
                                    SearchBar(self.app).layout(),
                                ),
                            ],
                            id="navbar-collapse",
                            navbar=True,

                        )],
                        width="auto"
                    )
                ],
                color="dark",
                style={
                    "color": "#142339"
                }
            )
        )
        return layout

    @staticmethod
    def callbacks(app):
        app.callback(
            Output("navbar-collapse", "is_open"),
            [Input("navbar-toggler", "n_clicks")],
            [State("navbar-collapse", "is_open")],
        )(toggle_navbar_collapse())

