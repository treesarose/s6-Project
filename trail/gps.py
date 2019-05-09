from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='MMCA1629')
place = input ("Place: ")
gn = geolocator.geocode(place)
lan = gn.latitude
lon = gn.longitude
loc = str(lan)+","+str(lon)
print (loc+"\n++++++++++++++++++\n")
print(gn.address+"\n++++++++++++++++++\n")
print(gn.raw)
