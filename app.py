import dash
import dash_bootstrap_components as dbc

from layouts.main_layout import layout
import callbacks.dashboard_callbacks  # só para registrar callbacks

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG]
)

app.title = "Dashboard BI"
app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)
