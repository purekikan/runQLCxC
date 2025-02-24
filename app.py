from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

from plotters import *

global key_category
global graph_category
global graph_option

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1("Interactive Dash Board : RunQL Challenge", className='mb-4 mt-4', style={'textAlign':'center'}),
 
    # After template ###############################################################################
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='Key Category',
                placeholder='Select a Subject of Your Interest',
                options=list(key_areas.keys())),
        ], width=4),
        dbc.Col([
            dcc.Dropdown(
                id='Graph Category',
                placeholder='Select a Graph',
                ),
        ], width=4),
        dbc.Col([         
            dcc.Dropdown(
                id='Graph Options',
                placeholder='Select Options for your Graph (if any)',
                ),
        ], width=4)
    ]),

    dbc.Row(dbc.Button('Plot', id='plot-toggle', n_clicks=0), justify="center", className='mt-4'),

    dbc.Row(dbc.Col(html.Img(id='matplotlib')), justify="center"),

    dbc.Row(dbc.Col([
            dcc.Graph(id='plotly', figure={})
        ], width=12), justify="center"),
])

# toggle this function when key_category is chosen
@app.callback(
    Output(component_id='Graph Category', component_property='options'),
    Output(component_id='Graph Category', component_property='value'),
    Input('Key Category', 'value'),
)
def on_select_key_category(selected_key_category):
    global key_category
    key_category = selected_key_category
    retlist = list(key_areas[selected_key_category].keys())
    return retlist, retlist[0]

# toggle this function when graph_category is chosen
# TODO: Add a dropdown to choose the graph options, 
#       if there is only 1 option, then don't show the dropdown, and call the plot function directly
@app.callback(
    Output(component_id='Graph Options', component_property='options'),
    Output(component_id='Graph Options', component_property='value'),
    Input('Graph Category', 'value'),
)
def on_select_graph_category(selected_graph_category):
    global graph_category
    graph_category = selected_graph_category
    retlist = list(key_areas[key_category][graph_category].keys())
    return retlist, retlist[0]

# toggle this function when graph_option is chosen
@app.callback(
    Input('Graph Options', 'value'),
)
def on_select_graph_option(selected_graph_option):
    global graph_option
    graph_option = selected_graph_option


# toggle this function when plot button is clicked
# TODO : Add functions to plot all options
@app.callback(
    Output(component_id='matplotlib', component_property='src'),
    Output('plotly', 'figure'),
    Output('plot-toggle', 'type'),
    Input('plot-toggle', 'n_clicks'),
)
def plot_data(n_clicks):
    if n_clicks == 0:
        button_type = 'button'
    else:
        button_type = 'reset'
    plotter = None
    working_list = key_areas[key_category][graph_category][graph_option]
    plotter = working_list[0]
    data_path = f'./dataset/{working_list[1]}'
    options = working_list[2:] if len(working_list) > 2 else []
    retval = plotter(data_path, options)
    if type(retval) == list:
        fig_bar_plotly = retval[1]
        retval = retval[0]
    else:
        fig_bar_plotly = None
    return retval, fig_bar_plotly, button_type



if __name__ == '__main__':
    app.run()