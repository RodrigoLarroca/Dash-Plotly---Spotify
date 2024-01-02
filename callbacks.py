from librerias import Output, Input, State, dash, callback, app, px
from base_de_datos import client
from df_spotify import df

@app.callback(
    Output('pages-list', 'style'),
    [Input('toggle-pages', 'n_clicks')]
)
def toggle_pages(n_clicks):
    return {'display': 'none'} if n_clicks is None or n_clicks % 2 == 0 else {'display': 'block'}

@app.callback(
    Output('year-dropdown', 'style'),
    [Input('page-store', 'data')]
)
def toggle_dropdown_visibility(page_data):
    if not page_data or page_data['page'] != 'page-4':
        return {'display': 'block', 'color': 'blue'}
    else:
        return {'display': 'none'}

def update_content(selected_year, page_data):
    df_year = df[df['released_year'] == selected_year]
    content = f"Contenido actualizado con filtro de año {selected_year} para la página {page_data['page']}."
    return content

#################################### FUNCION PRINCIPAL ####################################
@app.callback(
    Output('page-store', 'data'),
    [Input('page-1', 'n_clicks'),
     Input('page-2', 'n_clicks'),
     Input('page-3', 'n_clicks'),
     Input('page-4', 'n_clicks')],
    [State('page-store', 'data')]
)
def update_page_store(p1, p2, p3, p4, current_page):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
    return {'page': ctx.triggered[0]['prop_id'].split('.')[0]}

@app.callback(
    [Output('content-graph', 'figure'),
     Output('content-graph-2', 'figure'),
     Output('content-graph-3', 'figure'),
     Output('content-graph-4', 'figure')],
    [Input('year-dropdown', 'value'),
     Input('page-store', 'data'),
     Input('artist-dropdown', 'value')]
)
def update_graphs(selected_year, page_data, selected_artist):
    if not page_data:
        return [dash.no_update] * 4

    page_clicked = page_data['page']
    df_filtered = df.copy()

    if selected_artist:
        df_filtered = df_filtered[df_filtered['artist(s)_name'].isin(selected_artist)]

    if selected_year:
        df_filtered = df_filtered[df_filtered['released_year'] == selected_year]

    graphs = {
        'page-1': {
            'fig1': px.bar(x=['Observaciones'], y=[df_filtered.shape[0]], title=f'Total de observaciones', labels={'y': 'Observaciones'}, template='plotly_dark').update_traces(marker_color='blue'),
            'fig2': px.bar(df_filtered.groupby('artist(s)_name').streams.sum().nlargest(10).reset_index(), x='streams', y='artist(s)_name', orientation='h', title=f'Top 10 artistas con + reproducciones', labels={'streams': 'Reproducciones', 'artist(s)_name': 'Artistas'}, template='plotly_dark').update_traces(marker_color='green'),
            'fig3': px.bar(df_filtered.nlargest(10, 'streams'), x='streams', y='track_name', orientation='h', title=f'Top 10 canciones con + reproducciones', labels={'streams': 'Reproducciones', 'track_name': 'Canciones'}, template='plotly_dark').update_traces(marker_color='orange'),
            'fig4': px.bar(df_filtered.nlargest(10, 'in_spotify_playlists'), x='in_spotify_playlists', y='track_name', orientation='h', title=f'Top canciones guardadas en playlist', labels={'in_spotify_playlists': 'Spotify playlists', 'track_name': 'Canciones'}, template='plotly_dark').update_traces(marker_color='purple'),
        },
        'page-2': {},
        'page-3': {},
        'page-4': {},
    }

    return [graphs[page_clicked][f'fig{i+1}'] for i in range(4)]