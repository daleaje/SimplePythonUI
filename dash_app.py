# python standard libs
from datetime import datetime
from typing import Dict

# external libs
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from flask.globals import session

# local files
from . import logger


app.layout = html.Div(
  [
    html.Header(
      id='sitename',
      children=[
        html.A(id='home', href='/home'),        
      ],
    ),
    html.Nav(
      id='site-specific-nav',
      children=[
        html.Ul(
         [
          html.Li(dcc.Link('Home', href='/home')),
          html.Li(dcc.Link('Match Results', href='/match')),
         ]
        )
      ],
    ),
    html.Main(
      className="container",
      children=[
       html.Section(
         className="column1",
         children=[
           html.Div(children=[html.H6(id="welcome message", children="Welcome")]),
           html.Div(
             html.Div(id="page-content"),
             className="row",
           ),
         ],
         style={"width":"100%"},
       ),
      ]
    ),
    html.Footer(
      html.Ul(
        [
         html.Li(f'Last update {datetime.UtcNow()}'),         
        ]
      ),
    ),
    dcc.Location(id="url"),
  ],
  className="layout-sample"
)

@app.callback(
  Output("page-content", "children"),
  Input("url","pathname")
)
def navigate(url: str) -> html.Div:
  from .app1 import make_layout_1
  from .app2 import make_layout_2
  
  if url.startswith("/home"):
    return make_layout_1()
  if url.startswith("/match"):
    return make_layout_2()
  return make_layout_1()

@app.callback(
 Output(component_id="welcome_message", component_property="children"),
 Input(component_id="welcome_message", component_property="children"),
)
def update_user_message(*args: str, **kwargs: Dict[str,str]) -> str:
  user=session.get(SESSION_NAME_USER)
  if not user:
    raise PreventUpdate
  logger.info(f'Welcome user: {user["name"]}')
  return f'Welcome user: {user["name"]}'
