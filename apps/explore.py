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
df_irr = pd.read_parquet('data/irrigation.parquet')

cols = df.columns
irr_cols = df_irr.columns
irr_area = ['Total Area', 'Groundwater Area', 'Surface Water Area', 'Percent area']
cities = df_irr['Governorate'].unique()
months = df['Month'].unique()
years = df['Year'].unique()
now = datetime.now(timezone.utc)
current_month = now.strftime('%B')

# Set custom color scale
color_scale = ['#E22126', '#669278', '#16161A', '#C74D4F', '#161729',
               '#B42D52', '#9B5A9C', '#B4C756', '#A9595C', '#3AA484',
               '#3580A0', '#CE3A74', '#7EAFED', '#6192BA', '#2D2F89',
               '#465DAB', '#1E1F2E']


fig_1 = go.Figure()
fig_1.add_trace(go.Indicator(
    mode = "number+delta",
    value = df[df['Year'] == 2020].Transpiration_sum.mean(),
    title = {
        "text": "Transpiration<br><span style='font-size\
                :0.8em;color:gray'>in</span><br><span style='font-size\
                :0.8em;color:gray'>mm/day</span>"
    },
    delta = {
        'reference': df[df['Year'] == 2019].Transpiration_sum.mean(),\
            'relative': True
    },
   domain = {'x': [0.5, 0], 'y': [1, 0.5]}))

fig_2 = go.Figure()
fig_2.add_trace(go.Indicator(
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
    domain = {'x': [0.5, 0], 'y': [1, 0.5]}))

fig_3 = go.Figure()
fig_3.add_trace(go.Indicator(
    mode = "number+delta",
    value = df[df['Year'] == 2020].Evaporation_sum.mean(),
    title = {
        "text": "Evaporation<br><span \
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
    ]),
    html.Hr(),
    dbc.Row([

        dbc.Col(
            html.Div(
                dcc.Graph(
                    id='Indicator',
                    figure=fig_1,
                    animate=True,
                    responsive=True,
                    config={
                        'showTips': True,
                        'displaylogo': False
                    }
                )
            ), style={'font-variant': 'small-caps', 'font-weight': 'bold'}, width=4, xs=12, sm=12, md=4
        ),
        dbc.Col(
            html.Div(
                dcc.Graph(
                    id='Indicator1',
                    figure=fig_2,
                    animate=True,
                    responsive=True,
                    config={
                        'showTips': True,
                        'displaylogo': False
                    }
                )
            ), style={'font-variant': 'small-caps', 'font-weight': 'bold'}, width=4, xs=12, sm=12, md=4
        ),
        dbc.Col(
            html.Div(
                dcc.Graph(
                    id='Indicator2',
                    figure=fig_3,
                    animate=True,
                    responsive=True,
                    config={
                        'showTips': True,
                        'displaylogo': False
                    }
                )
            ), style={'font-variant': 'small-caps', 'font-weight': 'bold'}, width=4, xs=12, sm=12, md=4
        )
    ], className='row'),
    html.Hr(),
    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H1(
                    'Average Water Consumption as at 2020',
                    className='text-center'
                ), className='mb-4 mt-5'
            ))
    ]),
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
                        value='Temperature(C)'
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
                        value='Temperature(C)'
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
    html.Hr(),
    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H1(
                    'Average Water Consumption as at 2020',
                    className='text-center'
                ), className='mb-4 mt-5'
            ))
    ]),
    html.Hr(),
    
    dbc.Row([
        dbc.Col(
            html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column2',
                        options=[{
                            'label': i, 'value': i
                        } for i in irr_cols],
                        value='Total Area'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type2',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                html.Div([
                    dcc.Dropdown(
                        id='yaxis-column2',
                        options=[{
                            'label': i, 'value': i
                        } for i in irr_cols],
                        value='Percent area'
                    ),
                    dcc.RadioItems(
                        id='yaxis-type2',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                dcc.Graph(
                    id='map-graph',
                    responsive=True,
                    config={
                        'displaylogo': False,
                        'showTips': True,
                        'scrollZoom': False
                    }
                )
            ], style = {
                'font-variant': 'small-caps', 'font-weight': 'bold'
            }), width=6, xs=12, sm=12, md=6
        ),
        dbc.Col(
            html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column5',
                        options=[{
                            'label': i, 'value': i
                        } for i in irr_area],
                        value='Total Area'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type5',
                        labelStyle={
                            'display': 'inline-block'
                        }
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                
            dcc.Graph(
                id='barh-chart',
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
    html.Hr(),
    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H1(
                    'Average Water Consumption as at 2020',
                    className='text-center'
                ), className='mb-4 mt-5'
            ))
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='xaxis-column3',
                        options=[{
                            'label': i, 'value': i
                        } for i in cols],
                        value='Transpiration_sum'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type3',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                html.Div([
                    dcc.Dropdown(
                        id='yaxis-column3',
                        options=[{
                            'label': i, 'value': i
                        } for i in cols],
                        value='Temperature(C)'
                    ),
                    dcc.RadioItems(
                        id='yaxis-type3',
                        labelStyle={'display': 'inline-block'}
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
            dcc.Graph(
                id='bar-chart',
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
                        id='xaxis-column4',
                        options=[{
                            'label': i, 'value': i
                        } for i in cols],
                        value='Rainfall'
                    ),
                    dcc.RadioItems(
                        id='xaxis-type4',
                        labelStyle={
                            'display': 'inline-block'
                        }
                    )
                ], style={
                    'width': '48%', 'display': 'inline-block',
                    'color': 'black'
                }),
                
            dcc.Graph(
                id='line-chart',
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
                      color_continuous_scale='jet',
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
        hole=.65, theme='white',colorscale='purples', textposition='inside',
        linecolor='black', textinfo='label+percent', sort=True,
        title='Total  ' + str(yaxis_column) + '  per month for  '\
            + str(xaxis_column)
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})

    return fig


@app.callback(
    Output('map-graph', 'figure'),
    Input('xaxis-column2', 'value'),
    Input('yaxis-column2', 'value'),
    Input('xaxis-type2', 'value')
)
def map_graph(xaxis_column, yaxis_column, xaxis_type):
    fig = px.scatter_mapbox(df_irr, lat='Latitude', lon='Longitude',
                            size=xaxis_column,color=yaxis_column, zoom=4,
                            mapbox_style='light',
                            color_continuous_scale='icefire',
                            template='presentation',
                            hover_data={
                                'Governorate': True, 'Latitude': False,
                                'Total Area': True, 'Longitude': False
                            }, width=550, height=550)
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})

    return fig


@app.callback(
    Output('barh-chart', 'figure'),
    Input('xaxis-column5', 'value'),
    Input('xaxis-type', 'value')
)
def barh_chart(xaxis_column, xaxis_type):
    fig = df_irr.iplot(
        asFigure=True, kind='bar',x='Governorate', y=xaxis_column,
        theme='white', orientation='h', xTitle=str(xaxis_column),
        yTitle='Governorate', subplots=True, subplot_titles=True,
        gridcolor='white', colors=color_scale
    )
    fig.update_layout(margin={'l': 40, 'r': 40, 'b': 40, 't': 40})

    return fig


@app.callback(
    Output('bar-chart', 'figure'),
    Input('xaxis-column3', 'value'),
    Input('yaxis-column3', 'value'),
    Input('xaxis-type3', 'value')
)
def bar_graph(xaxis_column, yaxis_column, xaxis_type):
    fig = df.iplot(
        asFigure=True, kind='bar', x='Date', y=[xaxis_column, yaxis_column],
        barmode='stack', bestfit=False, colors=color_scale, theme='white',
        gridcolor='white', subplots=True, subplot_titles=True
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})

    return fig


@app.callback(
    Output('line-chart', 'figure'),
    Input('xaxis-column4', 'value'),
    Input('xaxis-column4', 'value')
)
def line_graph(xaxis_column, xaxis_type):
    fig = df.iplot(
        asFigure=True, kind='scatter', x='Date', y=xaxis_column, mode='lines',
        interpolation='spline', bestfit=True, colors=color_scale,
        theme='white', gridcolor='white',
        title='Total  ' + str(xaxis_column) + ' Rate From 2009 to 2020'
    )
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 40, 'r': 40})

    return fig

