import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# URL directa para exportar la hoja como CSV (con gid=0)
url ="https://docs.google.com/spreadsheets/d/1pfKozIhhxKbGF2dhtIZMyFyeJhk0aK4wshZYzh5MQTs/edit?gid=0#gid=0

# Leer CSV desde la URL
sitada = pd.read_csv(url)

# Limpiar nombres de columnas (quitar espacios y poner todo en mayúsculas)
sitada.columns = sitada.columns.str.strip().str.upper()

# Crear columna geometry con puntos a partir de LONGITUD y LATITUD
sitada['geometry'] = sitada.apply(lambda row: Point(row['LONGITUD'], row['LATITUD']), axis=1)

# Convertir DataFrame a GeoDataFrame
gdf = gpd.GeoDataFrame(sitada, geometry='geometry')

# Definir sistema de referencia (WGS84)
gdf.set_crs(epsg=4326, inplace=True)

# Guardar GeoDataFrame en archivo GeoJSON
gdf.to_file('sistemas_prueba.geojson', driver='GeoJSON')

