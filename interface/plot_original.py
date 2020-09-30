import geopandas as gpd
import json
from bokeh.models import ColumnDataSource, GeoJSONDataSource, HoverTool, Legend
from bokeh.plotting import figure, output_file
from bokeh.models.widgets import TextInput
from bokeh.embed import json_item, components
from bokeh.resources import CDN
from datetime import date
import calendar
import math
import re
from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
import random

root = "/home/user/dip/interface/static/map/"
address = root + "addresses-point.shp" 
amenity_points = root + "amenity_points-point.shp"
amenity_polygons = root + "amenity_polygons-polygon.shp"
bridges = root + "bridges-line.shp"
buildings = root + "buildings-polygon.shp"
forests = root + "forests-polygon.shp"
landcover = root + "landcover-polygon.shp"
now = root + "now-data.shp"
railways = root + "railways-line.shp"
roads = root + "roads-line.shp"
stations = root + "stations-point.shp"
trees = root + "trees-point.shp"
tunnels = root + "tunnels-line.shp"
water_areas = root + "water_areas-polygon.shp"
water_lines = root + "water_lines-line.shp"

def getPointCoords(row, geom, coord_type):
    """Calculates coordinates ('x' or 'y') of a Point geometry"""
    if coord_type == 'x':
        return row[geom].x
    elif coord_type == 'y':
        return row[geom].y

def getLineCoords(row, geom, coord_type):
    """Returns a list of coordinates ('x' or 'y') of a LineString geometry"""
    if coord_type == 'x':
        return list( row[geom].coords.xy[0] )
    elif coord_type == 'y':
        return list( row[geom].coords.xy[1] )

def getPolyCoords(row, geom, coord_type):
    """Returns the coordinates ('x' or 'y') of edges of a Polygon exterior"""
    # Parse the exterior of the coordinate
    exterior = row[geom].exterior
    if coord_type == 'x':
        # Get the x coordinates of the exterior
        return list( exterior.coords.xy[0] )
    elif coord_type == 'y':
        # Get the y coordinates of the exterior
        return list( exterior.coords.xy[1] )

#receive a POINT/LINESTRING/POLYGON path, return a source
def handdler(path, type):
    obj = gpd.read_file(path)
    if type == "MP": #MULTIPOLYGON
        return GeoJSONDataSource(geojson=obj.to_json())
    elif type == "LS": #LINESTRING
        func = getLineCoords
    elif type == "PN": #POINT
        func = getPointCoords
    elif type == "PG": #POLYGON
        func = getPolyCoords
    else:
        return
    obj['x'] = obj.apply(func, geom='geometry', coord_type='x', axis=1)
    obj['y'] = obj.apply(func, geom='geometry', coord_type='y', axis=1)
    obj_df = obj.drop('geometry', axis=1).copy()
    return ColumnDataSource(data=obj_df)

def dat():
    year = date.today().year
    month = date.today().month
    day = date.today().day
    month_name = calendar.month_name[month]
    title = " - %s %s %s" % (day, month_name, year)
    return title

def Layout(width=600,height=600,role='user',user_dict={}):
    hover = HoverTool(
                tooltips=[
                    ("index", "$index"),
                    ("data (using $) (x,y)", "($x, $y)"),
                    ("data (using @) (x,y)", "(@x, @y)"),
                    ("canvas (x,y)", "($sx, $sy)")
                    ])

    TOOLS = "reset,wheel_zoom,pan"
    global p
    p = figure(name="Map",title="Home Layout"+dat(), tools=TOOLS,
               plot_width = int(width), plot_height = int(height),toolbar_location="below")

    # Add the lines to the map from our 'msource' ColumnDataSource -object
    p.multi_line('x','y', source=handdler(innerwalls,"LS"), color='brown',line_color="brown",line_width=2)
    p.multi_line('x', 'y', source=handdler(doors,"LS"), color='lightblue', line_width=2)    
    p.triangle('x', 'y', source=handdler(anchors,"PN"), color='grey', line_width=1,legend_label='anchors')
    p.patches('x','y', source=handdler(pillars,"MP"), color='lightgrey')
    p.multi_line('x','y', source=handdler(WalkB3,"LS"), color='blue',line_dash="dotted",line_width=2, legend_label='walk paths_B3')
    p.multi_line('x','y', source=handdler(WalkB5,"LS"), color='red',line_dash="dashed",line_width=2, legend_label='walk paths_B5')
    p.patches('x','y', source=handdler(wallsB3,"PG"), color='lightgrey', legend_label='walls_b3')
    p.patches('x','y', source=handdler(wallsB5,"PG"), color='lightgreen', legend_label='walls_b5')
    
    legend_items = []
    for username in user_dict.keys():
        track_source = ColumnDataSource(data=dict(x=[],y=[]),name=str(user_dict[username]))
        item = p.circle("x", "y", source=track_source, 
            color="#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]),line_width=1) #random color
        legend_items.append((username + " " + str(user_dict[username]),[item]))

    if role in ['console','admin']:
        legend = Legend(items=legend_items,location='center')
        p.add_layout(legend,'right')
    else:
        route_source = ColumnDataSource(data=dict(x=[],y=[]),name='ROUTE')
        p.line("x", "y", source=route_source,  color='red', line_width=1,legend_label='route nodes')#for A* routing

    p.legend.click_policy='hide'
    p.xaxis.axis_label = "Distance in meters"
    p.yaxis.axis_label = "Distance in meters"
    p.add_tools(hover)
    return json.dumps(json_item(p, "myplot"))

if __name__ == "__main__":
    output_file("lines.html")
    Layout("Home Layout"+dat())
