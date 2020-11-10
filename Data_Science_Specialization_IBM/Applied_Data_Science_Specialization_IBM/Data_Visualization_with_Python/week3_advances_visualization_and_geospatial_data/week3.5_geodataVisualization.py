import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # needed for waffle Charts
import pandas as pd
import numpy as np
import folium
from folium import plugins

path = '/home/tbfk/Documents/VSC/Coursera/Applied_Data_Science_Specialization_IBM/Data_Visualization_with_Python/'


#---Simple Maps
# define the world map
world_map = folium.Map()

# display world map
world_map.save(path + 'world_map.html')

# define the world map centered around Mexico with a higher zoom level
latitude = 23.626
longitude = -102.538
mexico_map = folium.Map(location=[latitude, longitude], zoom_start=4)

# display world map
mexico_map.save(path + 'mexico_map.html')

# There are different tile formats available:
# 'Stamen Terrain': to visualize its hill shading and natural vegetation
# 'Stamen Toner': for data mashups and exploring river meanders and coastal zones

mexico_map = folium.Map(location=[latitude, longitude], zoom_start=4, tiles='Stamen Terrain')

# display world map
mexico_map.save(path + 'mexico_terrain_map.html')


#---Maps with Markers
#df_incidents = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')
df_incidents = pd.read_csv(path + 'Police_Department_Incidents_-_Previous_Year__2016_.csv')
print('Dataset downloaded and read into a pandas dataframe!')

# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]

# Now let's superimpose the locations of the crimes onto the map. 
# The way to do that in Folium is to create a feature group with 
# its own features and style and then add it to the sanfran_map.

# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42

# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# loop through the 100 crimes and add each to the map
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.CircleMarker(
        [lat, lng],
        radius=5, # define how big you want the circle markers to be
        color='yellow',
        fill=True,
        popup=label,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(sanfran_map)

# show map
sanfran_map.save(path + 'sanfran_map_simple.html')


# The same map as above with grouped crimes
# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location = [latitude, longitude], zoom_start = 12)

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(sanfran_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)

# display map
sanfran_map.save(path + 'sanfran_map_groups.html')


#---Choropleth Maps
