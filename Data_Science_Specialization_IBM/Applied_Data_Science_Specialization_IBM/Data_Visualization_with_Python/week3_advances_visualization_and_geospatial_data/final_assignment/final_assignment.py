import pandas as pd
import folium
import numpy as np

path = '/home/tbfk/Documents/VSC/Coursera/Applied_Data_Science_Specialization_IBM/Data_Visualization_with_Python/assignment/'

df_incidents = pd.read_csv(path + 'Police_Department_Incidents_-_Previous_Year__2016_.csv')

df_district = pd.DataFrame(df_incidents['PdDistrict'].value_counts())
df_district.reset_index(inplace = True)

df_district.rename(columns={"index":"Neighborhood", "PdDistrict":"Count"}, inplace=True)
df_district.head(10)

# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42

#world_geo = r'world_countries.json' # geojson file
#world_map = folium.Map(location=[latitude, longitude], zoom_start=12, tiles='Mapbox Bright')
sanfran_geo = r'sanfran_geojson' # geojson file

bins = list([5000,10000,15000,20000,25000,30000])

sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# generate choropleth map using the total immigration of each country to Canada from 1980 to 2013
folium.Choropleth(
    geo_data=sanfran_geo,
    data=df_district,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco',
    bins=bins
).add_to(sanfran_map)

# display map
sanfran_map.save(path + 'sanfran_map_crime.html')

