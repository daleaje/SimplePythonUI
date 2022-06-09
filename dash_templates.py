# .... all the imports

CONTENT_STYLE1={
 "padding": "0.5rem 0.5rem",
  ....
}

def page1_dropdowns(app, dropdown_spec, refresh_button_id) -> List[dbc.Col]:
  # generate the dropdowns BU, plant, area 
  # implementation here
  
def make_button1(label, button_id, color="primary", style = None) -> dbc.Button:
  return dbc.Button(label, id=button_id, n_clicks=0, color=color, style=style, className="mr-1")

def make_table_page1(table_id) -> html.Div:
  table=html.Div(
   [
    dash_table.DataTable(
     css =[],
     id=table_id,
     columns=[],
     data=[],
     editable=False,
     # the rest of the datatable implementations configs
    )
   ]
  )
  return table
