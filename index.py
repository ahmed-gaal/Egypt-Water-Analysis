
"""
Script for the landing page of the project
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import server
from app import app
from apps import home, explore
from dash.dependencies import Input, Output, State

# building the navigation bar
nav_item = dbc.NavItem(
    dbc.NavLink('Explore', href='/explore')
)
navitem = dbc.NavItem(
    dbc.NavLink(
        "Home", style={
            'font-variant': 'small-caps', 'font-weight': 'bold'
        }, href='/home'
    )
)
# make a dropdown for the different pages
drop_down = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(
            'Project Code', href='https://github.com/ahmed-gaal/Egypt-Water-Analysis', target='_blank'
        ),
    ],
    nav=True,
    in_navbar=True,
    label="Useful Links",
)

# Navbar Layout
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src='/assets/log.png', height="100px"),
                            width=4
                        ),
                        dbc.Col(
                            dbc.NavbarBrand(
                                'Egypt Water Statistics', className="ml-2"
                            ), width=8
                        ),
                    ],
                    align="center",
                    no_gutters=True,
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [navitem, nav_item, drop_down], className="ml-auto",
                    navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
                style=None
            ),
        ]
    ),
    id='nav-bar',
    color="auto",
    className="mb-5"
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
# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/explore':
        return explore.layout
    else:
        return home.layout

if __name__ == "__main__":
    app.run_server(port=6060, debug=True)