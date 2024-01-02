from dash import html
import dash_bootstrap_components as dbc

def header():
    header_style = {
        'background-color': '#522071',
        'color': 'white',
        'padding': '20px',
        'display': 'flex',
        'flex-direction': 'column',
        'height': 'full',
        'width': '15%'
    }

    title_style = {
        "textAlign": "center",
        "marginBottom": "30px",
        "marginTop": "0px",
        "fontSize": "36px",
        "fontWeight": "bold",
        "borderBottom": "3px solid white",
        "color": "#FFD700",
        "paddingBottom": "2px",
        "fontFamily": "Arial Black, sans-serif"
    }

    toggle_container_style = {
        'display': 'flex',
        'alignItems': 'center',
        'marginBottom': '5px'
    }

    toggle_style = {
        "cursor": "pointer",
        "fontSize": "24px",
        "margin-right": "8px",
        "fontFamily": "Arial Black, sans-serif"
    }

    page_style = {
        "cursor": "pointer",
        "marginBottom": "3px",
        "marginTop": "2px",
        "fontSize": "15px",
        "margin-left": "8px",
        "fontFamily": "Arial Black, sans-serif"
    }

    page_container_style = {
        "display": "none",
        "flex-grow": 1, 
    }

    return html.Div(
        style=header_style,
        children=[
            html.H1("Lana", style=title_style),
            html.Div([
                html.Div( id="toggle-pages",
                    style=toggle_container_style,
                    children=[
                        html.Div("Éxitos",  style=toggle_style),
                        html.Div("⇩", style={"marginLeft": "25px",'fontSize': '24px', 'fontFamily': 'Arial Black, sans-serif'}),
                    ]
                ),
                html.Div(
                    id="pages-list",
                    style=page_container_style,
                    children=[
                        html.Div("Top", id='page-1', style=page_style),
                        html.Div("Agregar...", id='page-2', style=page_style),
                        html.Div("Agregar...", id='page-3', style=page_style),
                        html.Div("Agregar...", id='page-4', style=page_style),
                    ]
                )
            ])
        ]
    )