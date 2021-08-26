"""
Home page script
"""
import dash_html_components as html 
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1('Problem Statement', style={
                'font-family': 'Overpass, sans-serif',
                'font-size': '280%', 'font-weight': 'bold',
                'font-variant': 'small-caps', 'text-align': 'center'
            },className='text-center'), className='mb-5 mt-5',
            width={'size': 6, 'offset': 6}, xs=6, sm=6, md=6)
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                dbc.Container([
                    html.P(children='Innovation and technology are trending\
                                    in the industry 4.0 revolution, and \
                                    dealing with environmental issues is no\
                                    exception. The articulation of artificial\
                                    intelligence (AI) and its application to \
                                    the green economy, climate change, and \
                                    sustainable development is becoming \
                                    mainstream. Water is one of the resources\
                                    which has direct and indirect \
                                    interconnectedness with climate change, \
                                    development, and sustainability goals. \
                                    In recent decades, several national and \
                                    international studies revealed the \
                                    application of AI and algorithm-based \
                                    studies for integrated water management\
                                    resources and decision-making systems.')
                    ], style={
                        'font-family': 'Overpass, sans-serif',
                        'font-size': '150%',
                        'font-weight': 'normal'
                    }))
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                dbc.Container([
                    html.P(children='Despite the government\'s efforts to \
                                    save every drop of water as the country\
                                    faces water scarcity, 98.4 million\
                                    Egyptians still live under the water\
                                    poverty line by 50 percent, below the \
                                    international line of 1,000 m3.\
                                    The danger of the water crisis in Egypt\
                                    increased with the presence of regional\
                                    conflicts over the water of the Nile River.',
                    style={
                        'font-family': 'Overpass, sans-serif',
                        'font-size': '150%', 'font-weight': 'normal'
                    }),
                    html.P(children='Flood irrigation represents the biggest\
                                    challenge to wasting water, as 77% of \
                                    the Nile\'s water is consumed through it.',
                    style={
                        'font-family': 'Overpass, sans-serif',
                        'font-size': '150%', 'font-weight': 'normal'
                    }),

                    html.P(children="The data used in the development of this\
                                    web application was collected from the\
                                    Climate Change Knowledge portal of the \
                                    World Bank and The FAO portal to monitor\
                                    Water Productivity through Open access of\
                                    Remotely sensed derived data (WaPOR).",
                    style={
                        'font-family': 'Overpass, sans-serif',
                        'font-size': '150%', 'font-weight': 'normal'
                    }), 
                    html.P(children='This dashboard will reveal insights on\
                                the water resources available, the effects of\
                                weather in the context of water consumption,\
                                and provide a clear understanding on the\
                                current water security in Egypt.',
                    style={
                        'font-family': 'Overpass, sans-serif',
                        'font-size': '150%', 'font-weight': 'normal'
                    })
                ])
            )
        ]),
    ])
])