import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('data.csv', index_col=0, parse_dates=True)
fig = px.bar(df, x="cars", y="values", color="real")

app.layout = html.Div(children=[
    html.H1(children='Car Prices'),
    html.Div(children='''
        - Real vs Values -
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    port= os.environ.get('PORT')
    app.run_server(debug=False, host='0.0.0.0', port = port)