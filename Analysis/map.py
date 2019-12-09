# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import numpy as np


"""
This section import the csv 911 calls.
Year, Month, Zone columns are created.
Four most important types are filtered.
"""
file1 = "Seattle_Real_Time_Fire_911_Calls.csv"
data = pd.read_csv(file1, nrows=1000) # nrows is the data number

# Add "Year" and "Mpnth" columns
data['Year'] = pd.DatetimeIndex(data['Datetime']).year
year2019 = data['Year'] == 2019 
#data=data[year2019] # in this demo only 2019 data are selected
data['Month'] = pd.DatetimeIndex(data['Datetime']).month
available_indicators = data['Year'].unique()


# Seattle center
lat_mean = 47.608013
lon_mean = -122.335167

# Add Zone column
conditions = [
    (data['Longitude'] >= lon_mean) & (data['Latitude'] >= lat_mean),
    (data['Longitude'] < lon_mean) & (data['Latitude'] >= lat_mean),
    (data['Longitude'] >= lon_mean) & (data['Latitude'] < lat_mean),
    (data['Longitude'] < lon_mean) & (data['Latitude'] < lat_mean)]
choices = ['NE', 'NW', 'SE', 'SW']
data['Zone'] = np.select(conditions, choices)

# Select Type
medic = (data['Type'] == "Medic Response")
aid = data['Type'] == "Aid Response"
car = data['Type'] == "MVI - Motor Vehicle Incident"
fire = data['Type'] == "Auto Fire Alarm"
df=data[(medic | aid | fire | car)]

# filter out 0 zone values
df = df[(df['Zone'] == 'NE')|(df['Zone'] == 'NW')|(df['Zone'] == 'SE')|(df['Zone'] == 'SW')]

"""
Interactive map section
Define the layout and callback functions
"""
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='map-graph'),
    html.Label('Year'),
    dcc.Dropdown(
                id='year-option',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value=2019
            ),
    html.Label('Call Type'),
    dcc.RadioItems(
        id = 'type-option',
        options=[
            {'label': 'Medic Response', 'value': 'Medic Response'},
            {'label': 'MVI - Motor Vehicle Incident', 'value': 'MVI - Motor Vehicle Incident'},
            {'label': 'Auto Fire Alarm', 'value': 'Auto Fire Alarm'},
            {'label': 'Aid Response', 'value': 'Aid Response'}
        ],
        value='Medic Response'
    ),
    html.Label('Zone'),
    dcc.RadioItems(
        id = 'zone-option',
        options=[
            {'label': 'NE', 'value': 'NE'},
            {'label': 'NW', 'value': 'NW'},
            {'label': 'SE', 'value': 'SE'},
            {'label': 'SW', 'value': 'SW'}
        ],
        value='NE'
    ),
    html.Label('Month'),
    dcc.Slider(
        id = 'month-slider',
        min = df['Month'].min(),
        max = df['Month'].max(),
        value = df['Month'].min(),
        marks = {str(Month): str(Month) for Month in df['Month'].unique()},
        step=None),
    html.Div([
        dcc.Graph(
            id='statistics',
        )
    ], style={'width': '49%', 'display': 'inline-block'}),
],style={'columnCount': 2})
          



layout_map = dict(
    autosize=True,
    height=1000,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
    title='911 Calls in Seattle',
    mapbox=dict(
        style = "open-street-map",
        center=dict(
            lon=-122.3,
            lat=47.5
        ),
        zoom=10,
    )
)

# functions
def gen_map(map_data):
    # groupby returns a dictionary mapping the values of the first field
    # 'classification' onto a list of record dictionaries with that
    # classification value.
    return {
        "data": [{
                "type": "scattermapbox",
                "lat": list(map_data['Latitude']),
                "lon": list(map_data['Longitude']),
                "mode": "markers",
                "name": list(map_data['Zone']),
                "marker": {
                    "size": 6,
                    "opacity": 0.7
                }
        }],
        "layout": layout_map
    }



     
@app.callback(
    Output('map-graph', 'figure'),
    [Input('year-option', 'value'),
     Input('type-option', 'value'),
     Input('zone-option', 'value'),
     Input('month-slider', 'value')])
          
def update_figure(year,selected_type,selected_zone,month_value):
    filtered_df = df[(df.Type == selected_type) & (df.Month == month_value) & (df.Year == year) & (df.Zone == selected_zone)]
    return gen_map(filtered_df)

@app.callback(
    Output('statistics', 'figure'),
    [Input('year-option', 'value'),
     Input('type-option', 'value'),
     Input('month-slider', 'value')])

def update_graph(year,selected_type,month_value):
    dff = df[(df.Type == selected_type) & (df.Month == month_value) & (df.Year == year)]
    df_st = dff.Zone.value_counts()
    df_st = df_st.reset_index()

    return {
        'data': [dict(
            x=df_st['index'],
            y=df_st['Zone'],
            type = 'bar'
        )],
        'layout': dict(
            xaxis={
                'title': 'Zone'
            },
            yaxis={
                'title': 'Counts'
            },
            hovermode='closest'
        )
    }



if __name__ == '__main__':
    app.run_server(debug=True)


