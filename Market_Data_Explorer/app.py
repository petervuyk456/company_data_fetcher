import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from Market_Data_Explorer.components import navbar
from Market_Data_Explorer.components.layout import apply_layout

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = apply_layout(app)

if __name__ == '__main__':
    app.run_server(debug=True)