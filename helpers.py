# all import stuff

def query_area(plant:str) -> List[Dict[str,str]]:
  query = f"""
  SELECT Area.name AS Name, Area.$dtId AS Id
  FROM DIGITALTWINS Plant
  JOIN Area RELATED Plant.has_area
  WHERE Plant.$dtId = '{plant}'"""
  
  res = adt_query(query)
  return sort_name_id(res)

def sort_name_id(name_id) -> List[Dict[str,str]]:
  #implementation here
  
# the rest of the query implementations
