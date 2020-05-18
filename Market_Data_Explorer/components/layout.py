import dash_html_components as html
import dash_bootstrap_components as dbc
from Market_Data_Explorer.components.navbar import NavBar


def apply_layout(app):
    app.layout = html.Div([
        html.Div(
            NavBar(app).layout(),
        ),
        html.Div(
            dbc.Card(
                id="test",
                className="container-flex",
                style={
                    "position": "fixed",
                    "top": "80px",
                    "left": "1%",
                    "bottom": "2%",
                    "width": "20rem",
                    "padding": "2rem 1rem",
                    "background-color": "#2A4B7C",
                }
            )
        )
    ])
    return app
