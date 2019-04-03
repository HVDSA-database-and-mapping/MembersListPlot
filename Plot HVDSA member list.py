import geopy
import folium
import pandas as pd
import time
import numpy as np

#replace the api_key with your own, can be registered for free at mapquest.com
geolocator = geopy.geocoders.OpenMapQuest(api_key="YOUR API KEY HERE")

#file should be stored in xlsx (Excel data)
df = pd.read_excel(r'MembersListWithCoords.xlsx')
df.head()

#define the map here, add the latitude and longitude points, with names and addresses
#only plot out the points that are TRUE in goodOrBad column
AnnArborCoords = geolocator.geocode('Ann Arbor, MI')
m = folium.Map(location=[AnnArborCoords.latitude, AnnArborCoords.longitude])

validation = df['goodOrBad']
#add a circle for each point in the members list
for j, address in enumerate(df['Address_Line_1']):
      if validation[j] == True:
            #could be modified to include phone number
            toPrint = df['first_name'][j] + ' ' + df['last_name'][j] 
            folium.CircleMarker(
            popup=toPrint,
            radius=3,
            location=(df['latitude'][j], df['longitude'][j]),
            color = '#ff0000',
            fill=True,
            fill_color = "#ff0000#"
            ).add_to(m)
m




