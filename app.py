"""
Script to instantiate web application
"""
import os
import dash
import dash_bootstrap_components as dbc


# bootstrap theme
external_stylesheets = [dbc.themes.LUX]

# Instantiate dash application
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])

server = app.server

# Application Title
app.title = 'Omdena Egypt Local Chapter'
app.config.suppress_callback_exceptions=True