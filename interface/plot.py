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
s2_b3 = root + "s2_b3.shp"
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
    # if type == "LS":
    #     print(obj_df)
    return ColumnDataSource(data=obj_df)

def dat():
    year = date.today().year
    month = date.today().month
    day = date.today().day
    month_name = calendar.month_name[month]
    title = " - %s %s %s" % (day, month_name, year)
    return title

def Layout(width=600,height=600):
    hover = HoverTool(
                tooltips=[
                    ("index", "$index"),
                    ("data (using $) (x,y)", "($x, $y)"),
                    ("data (using @) (x,y)", "(@x, @y)"),
                    ("canvas (x,y)", "($sx, $sy)")
                    ])

    TOOLS = "reset,wheel_zoom,pan"
    global p
    p = figure(name="Map",title="Nanyang Technological University"+dat(), tools=TOOLS,
               plot_width = int(width), plot_height = int(height),toolbar_location="below")

    # Add the lines to the map from our 'msource' ColumnDataSource -object
    # p.triangle('x','y',source=handdler(address,"PN"), color='brown',line_color="brown", legend_label='address')
    # p.triangle('x','y', source=handdler(amenity_points,"PN"), color='lightblue', legend_label='amenity_pn')
    # p.patches('x','y', source=handdler(amenity_polygons,"PG"), color='lightblue', legend_label='amenity_pg')
    # p.multi_line('x','y', source=handdler(bridges,"LS"), color='lightgrey', legend_label='bridges', line_width=1)
    p.patches('x','y', source=handdler(buildings,"PG"), color='lightgrey', legend_label='buildings')
    # p.patches('x','y', source=handdler(forests,"PG"), color='lightyellow', legend_label='forests')
    # p.patches('x','y', source=handdler(landcover,"PG"), color='lightblue', legend_label='landcover')
    # p.patches('x','y', source=handdler(now,"LS"), color='lightblue', legend_label='buildings')
    # p.multi_line('x','y', source=handdler(railways,"LS"), color='lightgrey', legend_label='railways', line_width=1)
    p.multi_line('x','y', source=handdler(roads,"LS"), color='lightgrey', legend_label='roads', line_width=1)
    # p.triangle('x','y', source=handdler(stations,"PN"), color='lightblue', legend_label='stations')
    p.patches('x','y', source=handdler(s2_b3,"PG"), color='blue', legend_label='S2 Level B3')
    # p.triangle('x','y', source=handdler(trees,"PN"), color='lightblue', legend_label='trees')
    # tunnels
    # p.patches('x','y', source=handdler(water_areas,"PG"), color='lightblue', legend_label='water')
    # water_lines

    p.xaxis.axis_label = "Longitude"
    p.yaxis.axis_label = "Latitude"
    p.add_tools(hover)
    return json.dumps(json_item(p, "myplot"))

if __name__ == "__main__":
    output_file("lines.html")
    Layout("Home Layout"+dat())
