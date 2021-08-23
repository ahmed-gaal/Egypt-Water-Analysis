"""
Data exploration script
"""
import os
import cufflinks
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime, timezone
from app import app

# Load data to a pandas DataFrame
df = pd.read_parquet('data/rain-wapor.parquet')

cols = df.columns
months = df['Month'].unique()
years = df['Year'].unique()
now = datetime.now(timezone.utc)
current_month = now.strftime('%B')

# Set custom color scale
color_scale = ['#E22126', '#669278', '#16161A', '#C74D4F', '#161729',
               '#B42D52', '#9B5A9C', '#B4C756', '#A9595C', '#3AA484',
               '#3580A0', '#CE3A74', '#7EAFED', '#6192BA', '#2D2F89',
               '#465DAB', '#1E1F2E']


fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = df[df['Year'] == 2020].Transpiration_sum.mean(),
    title = {
        "text": "Plants<br><span style='font-size\
                :0.8em;color:gray'>in</span><br><span style='font-size\
                :0.8em;color:gray'>mm/day</span>"
    },
    delta = {
        'reference': df[df['Year'] == 2019].Transpiration_sum.mean(),\
            'relative': True
    },
    domain = {'x': [0, 0.5], 'y': [0.5, 0]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = df[df['Year'] == 2020].Rainfall.mean(),
    title = {
        "text": "Rainfall<br><span style='font-size:0.8em;\
                color:gray'>in</span><br><span style='font-size\
                :0.8em;color:gray'>mm/day</span>"
    },
    delta = {
        'reference': df[df['Year'] == 2019].Rainfall.mean(),\
            'relative': True
    },
    domain = {'x': [0.5, 1], 'y': [0, 1]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = df[df['Year'] == 2020].Evaporation_sum.mean(),
    title = {
        "text": "Soil<br><span \
                style='font-size:0.8em ;color:gray'>in</span><br><span\
                style='font-size:0.8em ;color:gray'>mm/day</span>"
    },
    delta = {
        'reference': df[df['Year'] == 2019].Evaporation_sum.mean(),\
            'relative': True
    },
    domain = {'x': [0.5, 0], 'y': [1, 0.5]}))

# Load in our mapbox token
px.set_mapbox_access_token(os.environ.get('TOKEN'))

# Set custom color scale
color_scale = ['#E22126', '#669278', '#16161A', '#C74D4F', '#161729',
               '#B42D52', '#9B5A9C', '#B4C756', '#A9595C', '#3AA484',
               '#3580A0', '#CE3A74', '#7EAFED', '#6192BA', '#2D2F89',
               '#465DAB', '#1E1F2E']

layout = html.Div([
    html.Hr(),
    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H1(
                    'Average Water Consumption as at 2020',
                    className='text-center'
                ), className='mb-4 mt-5'
            ))
            #dbc.Col(
            #    html.P('Average Water Consumption as at 2020', style={
            #        'font-family': 'Overpass, sans-serif', 'font-weight': 'bold',
            #        'font-variant': 'small-caps', 'font-size': '150%'
            #    }), width={'size': 6, 'offset': 4}), className='row'),
    ]),
    html.Hr(),
    dbc.Row(
        dbc.Col(
            html.Div(
                dcc.Graph(
                    id='Indicator',
                    figure=fig,
                    animate=True,
                    responsive=True,
                    config={
                        'showTips': True,
                        'displaylogo': False
                    }
                )
            ), style={'font-variant': 'small-caps', 'font-weight': 'bold'}, width=12, xs=12, sm=12, md=12
        ), className='row'
    ),
    html.Hr(),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column',
                        options=[{
                            'label': i, 'value': i
                        } for i in cols],
                        value='Transpiration_sum'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                html.Div([
                    dcc.Dropdown(
                        id='yaxis-column',
                        options=[{
                            'label': i, 'value': i
                        } for i in cols],
                        value='Evaporation_sum'
                    ),
                    dcc.RadioItems(
                        id='yaxis-type',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
            dcc.Graph(
                id='sunburst',
                responsive=True,
                config={
                    'showTips': True,
                    'displaylogo': False
                }
            )
            ], style={
                'font-variant': 'small-caps', 'font-weight': 'bold'
            }), width=6, xs=12, sm=12, md=6
        ),
        dbc.Col(
            html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column1',
                        options=[{
                            'label': i, 'value': i
                        } for i in years],
                        value=2009
                    ),
                    dcc.RadioItems(
                        id='xaxis-type1',
                        labelStyle={
                            'display': 'inline-block'
                        }
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                html.Div([
                    dcc.Dropdown(
                        id='yaxis-column1',
                        options=[{
                            'label': i, 'value': i
                        } for i in cols],
                        value='Evaporation_sum'
                    ),
                    dcc.RadioItems(
                        id='yaxis-type1',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                
            dcc.Graph(
                id='pie-chart',
                responsive=True,
                config={
                    'showTips': True,
                    'displaylogo': False
                }
            )
            ], style={
                'font-variant': 'small-caps', 'font-weight': 'bold'
            }), width=6, xs=12, sm=12, md=6
        )
    ], className='row'),
    html.Hr()

])
@app.callback(
    Output('sunburst', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value')
)
def sunburst_graph(xaxis_column, yaxis_column, xaxis_type):
    fig = px.sunburst(df, path=['Month', 'Year'], values=xaxis_column, 
                      color=yaxis_column, template='seaborn',
                      color_continuous_scale=color_scale,
                      title='Explore  ' + str(xaxis_column) + ' &  ' \
                          + str(yaxis_column) + '  from 2009-2020')
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})

    return fig


@app.callback(
    Output('pie-chart', 'figure'),
    Input('xaxis-column1', 'value'),
    Input('yaxis-column1', 'value'),
    Input('xaxis-type1', 'value')
)
def pie_chart(xaxis_column, yaxis_column, xaxis_type):
    dff = df[df['Year'] == xaxis_column]
    fig = dff.iplot(
        asFigure=True, kind='pie', labels='Month', values=yaxis_column,
        hole=.65, theme='white',colors=color_scale, textposition='inside',
        linecolor='black', textinfo='percent',
        title='Total  ' + str(yaxis_column) + '  per month for  '\
            + str(xaxis_column)
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})

    return fig

