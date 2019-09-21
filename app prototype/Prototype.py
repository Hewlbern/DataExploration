import dash
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

import plotly.plotly as py
from plotly import graph_objs as go
from plotly.graph_objs import *

# external scripts
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# data

# def initialize: - this will be how we initialize the functions

# FreewayFDSlatlon.xlsx FreewayFDSdata.xlsx

vls = pd.ExcelFile('FreewayFDSdata.xlsx')
dff = pd.read_excel(vls, 'Volume', parse_dates=True, index_col="Time")
dff = dff.T

xls = pd.ExcelFile('freewayfdslatlon.xlsx')  # this loads the data only once saving memory
df = pd.read_excel(xls, 'Volume', parse_dates=True, index_col="Time")
df = df.T

df2 = pd.read_excel(xls, 'Occupancy', parse_dates=True, index_col="Time")
df2 = df2.T

df3 = pd.read_excel(xls, 'Speed', parse_dates=True, index_col="Time")
df3 = df3.T

Detectors = list(df.columns)

mf = pd.read_excel(xls, 'Coordinates', index_col="Short Name")

#   return df, df2, df3, Detectors, mf

mapbox_access_token = 'pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw'


# input slider value then output into data frame filter for slider time volume value


# This function creates a excel like table - not necessarily useful but left it here in case someone wants it later
def generate_table(dataframe, max_rows=3):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]

        # Styling

    )


# timeslider arrangement
def heatmap(SVO):
    # creates heatmap data for map
    SVO['Period'] = np.arange(len(SVO))
    mintime = SVO['Period'].min()
    maxtime = SVO['Period'].max()
    return mintime, maxtime


mintime, maxtime = heatmap(df)

hf = df.reset_index().set_index('Period')
# print(hf)
df2['Period'] = np.arange(len(df2))
hf2 = df2.reset_index().set_index('Period')
df3['Period'] = np.arange(len(df3))
hf3 = df.reset_index().set_index('Period')


#  uploading data - this allows you to drag and drop excel or other files

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            xls = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            return xls
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            xls = pd.read_excel(io.BytesIO(decoded))
            return xls
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])


"""
create a function taking a date as argument that will display the data on your map only for that date. 
Or two arguments (startDate, enDate), and your function will display the data between those two dates. 
This function has to filter the data, and display it.

"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H2("Managed Motorway Data App", style={'font-family': 'Dosis'}),
    html.P("Select different days using the dropdown and the slider\
                        below or by selecting different time frames on the\
                        histogram. Select Data type by clicking the Radio option",
           className="explanationParagraph twelve columns"),

    html.Div([

        html.Div([
            dcc.RadioItems(
                id='tdatam',
                options=[{'label': i, 'value': i} for i in ['Volume', 'Speed', 'Occupancy']],
                value='Volume',
                labelStyle={'display': 'inline-block'}
            ),
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    html.A('Select Files')
                ]),
                style={
                    'borderWidth': '10px',
                    'borderStyle': 'dashed',
                    'textAlign': 'center',
                    'float': 'right',
                },
                # Allow multiple files to be uploaded
                multiple=True
            ),
        ],
            style={'width': '100%', 'display': 'flex'}),

        html.Div([

            dcc.Graph(id='graph'),
            html.P("", id="popupAnnotation", className="popupAnnotation"),
            dcc.Slider(
                id="Slider",
                marks={i: 'Hour {}'.format(i) for i in range(0, 24)},
                min=mintime / 4,
                max=maxtime / 4,
                step=.01,
                value=19,
            )
        ], style={"padding-bottom": '50px', "padding-right": '50px', "padding-left": '50px', "padding-top": '50px'}),
        dcc.Tabs(id="tabs", children=[
            dcc.Tab(label='Performance Metrics', children=[
                html.Div([

                    html.P(
                        "Select different Freeway using the dropdown and click and hold on the graph to zoom in on specific parts of the graph. Higher Number the worse the congestion"),

                    dcc.Graph(
                        id='Freeway',
                        figure={
                            'data': [
                                {'x': ["Today", "Yesterday", "Average"], 'y': [4, 1, 2], 'type': 'bar',
                                 'name': 'Monash'},
                                {'x': ["Today", "Yesterday", "Average"], 'y': [2, 4, 5], 'type': 'bar',
                                 'name': u'Western'},
                            ],
                            'layout': {
                                'title': 'Network Performance Indicators'
                            }
                        }
                    )])
            ]),
            dcc.Tab(label='Detector Information', children=[
                html.Div([

                    html.P(
                        "Select different Detectors using the dropdown and click and hold on the graph to zoom in on specific parts of the graph. Select Data type by clicking the Radio option"),

                    dcc.Dropdown(
                        id='xaxis-column',
                        options=[{'label': i, 'value': i} for i in Detectors],

                        style={"width": '48%'},
                        multi=True
                    ),
                    dcc.RadioItems(
                        id='xaxis-type',
                        options=[{'label': i, 'value': i} for i in ['Volume', 'Speed', 'Occupancy']],
                        value='Volume',
                        labelStyle={'display': 'inline-block'}
                    ),
                    dcc.Graph(id='indicator-graphic')])
            ]),
            dcc.Tab(label='NetworkLens', children=[
                html.Div([

                    html.P(
                        "Nodes are detection points and the linkages describe how effective a link is."),

                    cyto.Cytoscape(
                        id='cytoscape',
                        layout={'name': 'preset'},
                        style={'width': '100%', 'height': '400px'},
                        elements=[
                            {'data': {'id': 'one', 'label': 'Node 1'}, 'position': {'x': 75, 'y': 75}},
                            {'data': {'id': 'two', 'label': 'Node 2'}, 'position': {'x': 200, 'y': 200}},
                            {'data': {'source': 'one', 'target': 'two'}}
                        ]
                    )])]),
            dcc.Tab(label='Example Data', children=[
                html.Div([
                    generate_table(dff)
                ], style={'overflowX': 'scroll', 'overflowY': 'scroll', 'height': '500px'})
            ])])

    ]
    )
])


# Marker


def datatime(t, hf):
    floortime = np.floor(t)
    heat = hf.filter(items=[floortime], axis=0).T.drop("index")
    return heat[floortime]


@app.callback(
    Output('graph', 'figure'),

    [Input('Slider', 'value'),
     Input('tdatam', 'value')],
    [State('graph', 'relayoutData')]

)
def update_map(time, tdata, gstate):
    # use state?
    zoom = 10.0
    latInitial = -37.8136
    lonInitial = 144.9631
    bearing = 0
    # print(time)
    # print(hf)
    # This is super janky and works way better with straight javascript. Fuck this noise.
    # This switched data types for map.
    if tdata == "Volume":
        # this is dynamic print(period)
        # print(time)
        # print(datatime(period,hf))
        return go.Figure(
            data=Data([
                Scattermapbox(
                    lat=mf.Y,
                    lon=mf.X,
                    mode='markers',
                    hoverinfo="text",
                    text=["Monash Freeway", "Western Link",
                          "Eastern Link",
                          "Melbourne CBD", "Swan Street"],
                    # opacity=0.5,
                    marker=Marker(size=15,
                                  color=datatime(time, hf),
                                  colorscale='Viridis',
                                  opacity=.8,
                                  showscale=True,
                                  cmax=2500,
                                  cmin=400
                                  ),
                ),
            ]),
            layout=Layout(
                autosize=True,
                height=750,
                margin=Margin(l=0, r=0, t=0, b=0),
                showlegend=False,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    center=dict(
                        lat=latInitial,  # -37.8136
                        lon=lonInitial  # 144.9631
                    ),
                    style='dark',
                    bearing=bearing,
                    zoom=zoom
                ),
                updatemenus=[
                    dict(
                        buttons=([
                            dict(
                                args=[{
                                    'mapbox.zoom': 10,
                                    'mapbox.center.lon': '144.9631',
                                    'mapbox.center.lat': '-37.8136',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Reset Zoom',
                                method='relayout'
                            )
                        ]),
                        direction='left',
                        pad={'r': 0, 't': 0, 'b': 0, 'l': 0},
                        showactive=False,
                        type='buttons',
                        x=0.45,
                        xanchor='left',
                        yanchor='bottom',
                        bgcolor='#323130',
                        borderwidth=1,
                        bordercolor="#6d6d6d",
                        font=dict(
                            color="#FFFFFF"
                        ),
                        y=0.02
                    ),
                    dict(
                        buttons=([
                            dict(
                                args=[{
                                    'mapbox.zoom': 15,
                                    'mapbox.center.lon': '151.15',
                                    'mapbox.center.lat': '-33.873',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Western Link',
                                method='relayout'
                            ),
                            dict(
                                args=[{
                                    'mapbox.zoom': 15,
                                    'mapbox.center.lon': '145.218',
                                    'mapbox.center.lat': '-37.81',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Eastern Link',
                                method='relayout'
                            ),
                            dict(
                                args=[{
                                    'mapbox.zoom': 12,
                                    'mapbox.center.lon': '145.061',
                                    'mapbox.center.lat': '-37.865',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Monash Freeway',
                                method='relayout'
                            ),
                            dict(
                                args=[{
                                    'mapbox.zoom': 15,
                                    'mapbox.center.lon': '145.005',
                                    'mapbox.center.lat': '-37.826389',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Swan Street',
                                method='relayout'
                            )
                        ]),
                        direction="down",
                        pad={'r': 0, 't': 0, 'b': 0, 'l': 0},
                        showactive=False,
                        bgcolor="rgb(50, 49, 48, 0)",
                        type='buttons',
                        yanchor='bottom',
                        xanchor='left',
                        font=dict(
                            color="#FFFFFF"
                        ),
                        x=0,
                        y=0.05
                    )
                ]
            )
        )

    elif tdata == "Speed":
        return go.Figure(
            data=Data([
                Scattermapbox(
                    lat=mf.Y,
                    lon=mf.X,
                    mode='markers',
                    hoverinfo="text",
                    text=["Monash Freeway", "Western Link",
                          "Eastern Link",
                          "Melbourne CBD", "Swan Street"],
                    # opacity=0.5,
                    marker=Marker(size=15,
                                  color=datatime(time, hf3),
                                  colorscale='Viridis',
                                  opacity=.8,
                                  showscale=True,
                                  cmax=50,
                                  cmin=150
                                  ),
                ),
            ]),
            layout=Layout(
                autosize=True,
                height=750,
                margin=Margin(l=0, r=0, t=0, b=0),
                showlegend=False,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    center=dict(
                        lat=latInitial,  # -37.8136
                        lon=lonInitial  # 144.9631
                    ),
                    style='dark',
                    bearing=bearing,
                    zoom=zoom
                ),
                updatemenus=[
                    dict(
                        buttons=([
                            dict(
                                args=[{
                                    'mapbox.zoom': 10,
                                    'mapbox.center.lon': '144.9631',
                                    'mapbox.center.lat': '-37.8136',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Reset Zoom',
                                method='relayout'
                            )
                        ]),
                        direction='left',
                        pad={'r': 0, 't': 0, 'b': 0, 'l': 0},
                        showactive=False,
                        type='buttons',
                        x=0.45,
                        xanchor='left',
                        yanchor='bottom',
                        bgcolor='#323130',
                        borderwidth=1,
                        bordercolor="#6d6d6d",
                        font=dict(
                            color="#FFFFFF"
                        ),
                        y=0.02
                    ),
                    dict(
                        buttons=([
                            dict(
                                args=[{
                                    'mapbox.zoom': 15,
                                    'mapbox.center.lon': '151.15',
                                    'mapbox.center.lat': '-33.873',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Western Link',
                                method='relayout'
                            ),
                            dict(
                                args=[{
                                    'mapbox.zoom': 15,
                                    'mapbox.center.lon': '145.218',
                                    'mapbox.center.lat': '-37.81',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Eastern Link',
                                method='relayout'
                            ),
                            dict(
                                args=[{
                                    'mapbox.zoom': 12,
                                    'mapbox.center.lon': '145.061',
                                    'mapbox.center.lat': '-37.865',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Monash Freeway',
                                method='relayout'
                            ),
                            dict(
                                args=[{
                                    'mapbox.zoom': 15,
                                    'mapbox.center.lon': '145.005',
                                    'mapbox.center.lat': '-37.826389',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Swan Street',
                                method='relayout'
                            )
                        ]),
                        direction="down",
                        pad={'r': 0, 't': 0, 'b': 0, 'l': 0},
                        showactive=False,
                        bgcolor="rgb(50, 49, 48, 0)",
                        type='buttons',
                        yanchor='bottom',
                        xanchor='left',
                        font=dict(
                            color="#FFFFFF"
                        ),
                        x=0,
                        y=0.05
                    )
                ]
            )
        )
    elif tdata == "Occupancy":
        return go.Figure(
            data=Data([
                Scattermapbox(
                    lat=mf.Y,
                    lon=mf.X,
                    mode='markers',
                    hoverinfo="text",
                    text=["Monash Freeway", "Western Link",
                          "Eastern Link",
                          "Melbourne CBD", "Swan Street"],
                    # opacity=0.5,
                    marker=Marker(size=15,
                                  color=datatime(time, hf2),
                                  colorscale='Viridis',
                                  opacity=.8,
                                  showscale=True,
                                  cmax=3,
                                  cmin=0
                                  ),
                ),
            ]),
            layout=Layout(
                autosize=True,
                height=750,
                margin=Margin(l=0, r=0, t=0, b=0),
                showlegend=False,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    center=dict(
                        lat=latInitial,  # -37.8136
                        lon=lonInitial  # 144.9631
                    ),
                    style='dark',
                    bearing=bearing,
                    zoom=zoom
                ),
                updatemenus=[
                    dict(
                        buttons=([
                            dict(
                                args=[{
                                    'mapbox.zoom': 10,
                                    'mapbox.center.lon': '144.9631',
                                    'mapbox.center.lat': '-37.8136',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Reset Zoom',
                                method='relayout'
                            )
                        ]),
                        direction='left',
                        pad={'r': 0, 't': 0, 'b': 0, 'l': 0},
                        showactive=False,
                        type='buttons',
                        x=0.45,
                        xanchor='left',
                        yanchor='bottom',
                        bgcolor='#323130',
                        borderwidth=1,
                        bordercolor="#6d6d6d",
                        font=dict(
                            color="#FFFFFF"
                        ),
                        y=0.02
                    ),
                    dict(
                        buttons=([
                            dict(
                                args=[{
                                    'mapbox.zoom': 15,
                                    'mapbox.center.lon': '151.15',
                                    'mapbox.center.lat': '-33.873',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Western Link',
                                method='relayout'
                            ),
                            dict(
                                args=[{
                                    'mapbox.zoom': 15,
                                    'mapbox.center.lon': '145.218',
                                    'mapbox.center.lat': '-37.81',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Eastern Link',
                                method='relayout'
                            ),
                            dict(
                                args=[{
                                    'mapbox.zoom': 12,
                                    'mapbox.center.lon': '145.061',
                                    'mapbox.center.lat': '-37.865',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Monash Freeway',
                                method='relayout'
                            ),
                            dict(
                                args=[{
                                    'mapbox.zoom': 15,
                                    'mapbox.center.lon': '145.005',
                                    'mapbox.center.lat': '-37.826389',
                                    'mapbox.bearing': 0,
                                    'mapbox.style': 'dark'
                                }],
                                label='Swan Street',
                                method='relayout'
                            )
                        ]),
                        direction="down",
                        pad={'r': 0, 't': 0, 'b': 0, 'l': 0},
                        showactive=False,
                        bgcolor="rgb(50, 49, 48, 0)",
                        type='buttons',
                        yanchor='bottom',
                        xanchor='left',
                        font=dict(
                            color="#FFFFFF"
                        ),
                        x=0,
                        y=0.05
                    )
                ]
            )
        )


@app.callback(
    Output('indicator-graphic', 'figure'),

    [Input('xaxis-column', 'value'),
     Input('xaxis-type', 'value')],
)
# def update_map(timevalue):
#   hf.filter(items=[timevalue], axis=0).T.drop("index")

def update_graph(xaxis_column_name, tdata):
    if tdata == "Volume":

        volume = []

        if xaxis_column_name != None:
            for i in range(0, len(xaxis_column_name)):
                graph_obj = go.Scatter(
                    x=df.index,
                    y=df[xaxis_column_name[i]])

                volume.append(graph_obj)
            return {
                'data': volume
            }
        return

    elif tdata == "Occupancy":
        occupancy = []

        if xaxis_column_name != None:
            for i in range(0, len(xaxis_column_name)):
                graph_obj = go.Scatter(
                    x=df2.index,
                    y=df2[xaxis_column_name[i]])

                occupancy.append(graph_obj)
            return {
                'data': occupancy
            }
        return

    elif tdata == "Speed":
        speed = []

        if xaxis_column_name != None:
            for i in range(0, len(xaxis_column_name)):
                graph_obj = go.Scatter(
                    x=df3.index,
                    y=df3[xaxis_column_name[i]])

                speed.append(graph_obj)
            return {
                'data': speed
            }
        return


# Here is how we will initialise functions eventually.

# @app.server.before_first_request
# def defineTotalList():
#    global totalList
#    totalList = initialize()


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "//fonts.googleapis.com/css?family=Dosis:Medium",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/62f0eb4f1fadbefea64b2404493079bf848974e8/dash-uber-ride-demo.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

if __name__ == '__main__':
    app.run_server(debug=True)
