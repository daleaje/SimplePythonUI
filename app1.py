from datetime import datetime
from urllib.parse import quote
from typing import Typle, List

from dash.dependencies import Input, Output, State
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd

from . import helpers, dash_templates
from .dash_app import app

def make_layout_1() -> html.Div:
  dropdown_spec = [
   {
     "id":"dropdown-0",
     "placeholder":"Select business unit...",
     "callback": lambda: [
       {"label",i["name"], "value": i["id"]} for i in helpers.query_bu()
     ],
   },
   {
     "id":"dropdown-1",
     "placeholder":"Select Plant...",
     "callback": lambda: [
       {"label",i["name"], "value": i["id"]} for i in helpers.query_p(value)
     ],
   },
   {
     "id":"dropdown-2",
     "placeholder":"Select Area...",
     "callback": lambda: [
       {"label",i["name"], "value": i["id"]} for i in helpers.query_a(value)
     ],     
   },
  ]
  
  # main page layout
  content = html.Div(
   [
    html.Div(
     [
      dash_templates.make_button1(
        "Menu",
        "btn_sidebar",
        color="white",
        style={"display":"inline-block"},
      ),
     ]
    ),
    html.Hr(),
    # single row to display heading to dropdows, reset, search
    dbc.Row(
      [
       dbc.Col(
         # filter dd layout
         dash_templates.page1_dropdown(app, dropdown_spec, "refresh-button")
         + [
          # reset button
           dash_templates.make_button1(
             "Reset","refresh-button", style={"width":"auto", "float":"right"}
           ),
           html.Hr(),
         ]
       ),
       html.Hr(),                 
      ]
    ), 
     ...
     # actual table
     dash_templates.make_table_page1("main-table"),
   ],
   id="display-page",
   style=dash_templates_CONTENT_STYLE1,
  )
  
  return html.Div([dcc.Store(id="side_click"),sidebar, content])
  
# main callback that gets triggered when the are dd changes
@app.callback(
 Output("main-table","data"),
 Input("dropdown-2","value"),
  prevent_initial_call=True,
)
def fill_table(area_id: str) -> Tuple[dict, str]:
  df = pd.DataFrame()
  if area_id:
    df=helpers.get_area_with_equipment(area_id=area_id)
    
    # only process if there are rows in df
    if df.shape[0]:
      # create url for tagnumber col
      link = "/match/" + df.Id.apply(quote)
      # combine tagnumber and linto into markdown format url
      df["TagLink"] = "[" + df["TagNumber"] + "](" + link + ")"
      
      # copy tagLink into tagnumber and remove
      df["TagNumber"] = "[  ](" + link + ")"
      df = df.drop(columns=["TagLink"])
      
   # convert pandas dataframe to list of dicts, ‘records’ : list like [{column -> value}, … , {column -> value}]
  data = df.to_dict(orient="records")
  return data, ""
      
      
      
  
def make_layout_2() -> html.Div:
  ....
