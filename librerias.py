import dash
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_auth
from dash import Dash, html, dcc, Output, Input, State, callback
from dash.dependencies import Input, Output, State
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

external_stylesheets = [dbc.themes.DARKLY]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)