import geopy
import folium
import pandas as pd
import time
import numpy as np

#replace the api_key with your own, can be registered for free at mapquest.com
geolocator = geopy.geocoders.OpenMapQuest(api_key="YOUR API KEY HERE")

#file should be stored in xlsx (Excel data)
df = pd.read_excel(r'test_data.xlsx')
df.head()

#iterate through the members list, appending two new columns for the 
# latitude and longitude of each member
addresses = df['Address_Line_1']
zipcodes = df['Zip']
city = df['City']
seriesLength = len(df['Zip'])
latitudeSer = pd.Series(np.zeros(seriesLength),index=df.index)
longitudeSer = pd.Series(np.zeros(seriesLength),index=df.index)
#next series is to report whether the address look up failed
goodOrBad = pd.Series(np.zeros(seriesLength,dtype=bool),index=df.index)

#Do not run this each time! Only run it upon receiving a new data set
# Otherwise, use just the map plotting tool

#probably going to need to do a considerable amount of data clean up
# 1. get rid of apartment numbers
# get rid of drive, street, et cetera
for j, address in enumerate(addresses):
    #do some text processing first
    #only take string to comma, avoiding apartment #s
    if addresses[j].find(',') != -1:
        addressNow = addresses[j][1:addresses[j].find(',')]
    else:
        addressNow = addresses[j]
    addressNow = addressNow.replace(".", '')
    
    #get the location
    time.sleep(0.1)
    location = geolocator.geocode(addressNow + ' ' + zipcodes[j])
    if location == None:
        #try adding the city
        newAddress = addressNow + ' ' + city[j] + ' ' + zipcodes[j]
        location = geolocator.geocode(newAddress)
        if location == None:
            #FAILED, set to center of Ann Arbor
            goodOrBad[j] = 0;
            location = geolocator.geocode('Ann Arbor, MI')
        else:
            goodOrBad[j] = 1;
            locationCoords = (location.latitude, location.longitude)
    else:
        goodOrBad[j] = 1;
        locationCoords = (location.latitude, location.longitude)
    print(addressNow + ' ' + zipcodes[j] + str(locationCoords))
    latitudeSer[j] = location.latitude
    longitudeSer[j] = location.longitude
df['latitude'] = latitudeSer
df['longitude'] = longitudeSer
df['goodOrBad'] = goodOrBad

df.head()
#export the data to a .xlsx file
df.to_excel('MembersListWithCoords.xlsx')

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



