from app import *
from dash_bootstrap_templates import load_figure_template
load_figure_template(["quartz"])

card_style = {
    'width': '800px',
    'min-height': '300px',
    'padding': '25px',
    'align-self': 'center'
}
df = pd.DataFrame(np.random.randn(100, 1), columns=["data"])
fig = px.line(df, x=df.index, y="data", template="quartz")


def render_layout(username):
    template = html.Div([
                dbc.Card([
                    dcc.Location(id='data-url'),
                    html.Legend('Olá, {}'.format(username)),
                    dcc.Graph(figure=fig),
                    html.Div([
                        dbc.Button('Logout', id='logout_button'),
                    ], style={'padding':'20px', 'justify-content':'end', 'display':'flex'})

                ], style=card_style)
            ], style={"height": "100vh", "vertical-align": "middle", "display": "flex", "justify-content": "center"})

    return template
