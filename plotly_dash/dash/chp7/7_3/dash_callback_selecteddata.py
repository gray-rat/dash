import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

gapminder = px.data.gapminder()
gapminder2007 = gapminder[gapminder['year'] == 2007]
dash_stylesheets = ['http://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

app.layout = html.Div(
    [
        html.H1('Gapminder Graph'),
        dcc.Graph(
            id='gapminder-g',
            figure=px.scatter(
                gapminder2007,
                x='gdpPercap',
                y='lifeExp',
                hover_name='country',
                # クリック+shiftキーで複数データを選択
                template={'layout': {'clickmode': 'event+select'}},
            ),
        ),
        html.P(id='hoverdata-p', style={'fontsize': 32, 'textAlign': 'center'}),
    ],
    style={'width': '80%', 'margin': 'auto', 'textAlign': 'center'},
)

@app.callback(
    Output('hoverdata-p', 'children'),
    # Graphの selectedData 属性を指定する
    Input('gapminder-g', 'selectedData'),
)
def show_hover_data(selectedData):
    return json.dumps(selectedData)

if __name__ == '__main__':
    app.run_server(debug=True)