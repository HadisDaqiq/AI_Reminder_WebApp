import googlemaps
from datetime import datetime

def locate():
    gmaps = googlemaps.Client(key='AIzaSyDPJEEdKJVSf-ODYxwAiWVdoYZU9yhPppk')
    location = []
    loc = gmaps.geolocate()
    lat = loc['location']['lat']
    lng = loc['location']['lng']

    reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
    array = reverse_geocode_result[0]
    street_number =array['address_components'][0]['short_name']
    route= array['address_components'][1]['short_name']

    street = street_number+" "+route
   # print(street)
    location.append(street)
    location.append(lat)
    location.append(lng)
    print(location)
    return location
