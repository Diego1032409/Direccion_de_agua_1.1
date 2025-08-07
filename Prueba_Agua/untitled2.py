
# Importamos las librerías
#Pandas se encarga de extraer los datos de la tabla de excel y la convierte en una tabla de python
import pandas as pd
#Nos permite guardar las coordenadas y tambien leer archivos .geojson
import geopandas as gpd
#Libreria que se encarga de manipular puntos (Se uso para crear coordenadas)
from shapely.geometry import Point

# URL del archivo de Google Sheets (exportado como CSV)
# Corrected URL for exporting as CSV (assuming the data is in the first sheet with gid=0)
url = "https://docs.google.com/spreadsheets/d/1pfKozIhhxKbGF2dhtIZMyFyeJhk0aK4wshZYzh5MQTs/export?format=csv&gid=0"

# Leemos los datos del archivo
sitada = pd.read_csv(url)

# Limpiamos los encabezados
sitada.columns = sitada.columns.str.strip().str.upper()

# Print column names to diagnose KeyError
print("Column names after cleaning:", sitada.columns)


# Creamos la columna de geometría con latitud y longitud
geometry = [Point(xy) for xy in zip(sitada["LONGITUD"], sitada["LATITUD"])]
# Usamos un CRS válido, como EPSG:4326 para latitud y longitud
gdf = gpd.GeoDataFrame(sitada, geometry=geometry, crs="EPSG:4326")

# Guardamos como archivo GeoJSON
gdf.to_file("sistemas_prueba.geojson", driver="GeoJSON")

# Descargamos el archivo al dispositivo
from google.colab import files
files.download("sistemas_prueba.geojson")
