from librerias import dash, html, dbc, dcc, Output, Input, State, callback, gspread, ServiceAccountCredentials, pd, dash_auth,app
from base_de_datos import client
from df_spotify import df
from callbacks import toggle_pages, toggle_dropdown_visibility, update_page_store
from header import header

app.layout = html.Div(style={'display': 'flex',
                              'height': '100%',
                              'flex-direction': 'row',
                              'flex-grow': 1}, 
                              children=[
    header(),

    html.Div(style={
        'flex': '100%',
        'padding': '20px',
        'width': '100%',
        'position': 'relative',
        'width':'full',
        'marginTop':'10px',
        'marginBottom':'10px',
        'marginLeft':'10px',
        'marginRight':'10px',
        'zIndex': 1,
    }, children=[
        dcc.Dropdown(
            id='year-dropdown',
            options=[
                {'label': '2020', 'value': '2020'},
                {'label': '2021', 'value': '2021'},
                {'label': '2022', 'value': '2022'},
                {'label': '2023', 'value': '2023'}
            ],
            value='2023',
            clearable=True,
            style={'display': 'block',
                    'marginBottom': '20px',
                    'marginLeft':'10px',
                    'marginRight':'10px',
                    'color':'black'}
        ),
         dcc.Dropdown(
            id='artist-dropdown',
            options=[
                {'label': artist, 'value': artist} for artist in df['artist(s)_name'].unique()
            ],
            multi=True,
            placeholder='Select Artist(s)',
            style={'display': 'block', 'marginBottom': '5px',                    
                   'marginLeft':'10px',
                    'marginRight':'10px', 
                    'color':'black'}
        ),

    ##################################   CONTENIDO    ##################################
        dbc.Row(style={'padding': '20px', 'marginTop': '5px','marginBottom': '5px'}, children=[
            dbc.Col(dcc.Graph(id='content-graph', style={'height': '60vh'}), width=4),
            dbc.Col(dcc.Graph(id='content-graph-2', style={'height': '60vh'}), width=8),
        ]),
        dbc.Row(style={'padding': '20px', 'marginTop': '5px','marginBottom': '5px'}, children=[
            dbc.Col(dcc.Graph(id='content-graph-3', style={'height': '50vh'}), width=6),
            dbc.Col(dcc.Graph(id='content-graph-4', style={'height': '50vh'}), width=6),
        ]),
    ]),
    dcc.Store(id='page-store', storage_type='session', data={'page': 'page-1'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
