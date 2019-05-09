from urllib import urlopen
import json
from urlparse import urlparse
from urllib import urlencode
import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='MMCA1629')
place = raw_input("Place: ")
gn = geolocator.geocode(place)
lan = gn.latitude
lon = gn.longitude
loc = str(lan)+","+str(lon)
#print("OPTIONS: \n Resort \n Hotel \n Resturant \n National Park \n Mountain/ Hill Station \n Beach  \n Desert \n Forest \n Zoo \n Aquariam \n Garden \n Monument \n Temple \n Church \n Museum \n Art Gallery \n Fort \n Palace/Castle \n Library \n Bridge \n Statue \n Skyscraper \n Theme park \n Festival/Carnival")
spot = raw_input("Type: ")
print (spot+", "+loc)
token="EAAD3gqWnsLUBALe2MTLa0yZATpTabBwHr0n122RvSnpKukINGjqmPat9d5j36wQJrGZAq3JZC3CR52EOhb5ZCB8nwQjdJohajCnUbBe58aBLCsYZAQBZBtwJb8ibfUhpL3dflj22nZALUosgIPTlfWZAzWtbVaGWpwflmqPwBBXqeLKAVLSJZCzJ2FGkLVZAFC1VghhBlRSXI3E0wiQobW1BCOmgAH0Cj0nV0ZD"
url="https://graph.facebook.com/search?type=place&q="+spot+"&center="+loc+"&distance=5000&fields=name,checkins,overall_star_rating,rating_count,phone,about,description,website,price_range,hours,location&limit=500&access_token="+token+""
try:
    facebook_connection = urlopen(url)
    data = facebook_connection.read().decode('utf8')
    json_object = json.loads(data)
    posts=json_object[data]
    log,lat,city,country=[],[],[],[]
    for i in posts:
        loc=i['location']
        log.append(loc['longitude'])
        lat.append(loc['latitude'])
        city.append(loc['city'])
        country.append(loc['country'])    
    df=pd.DataFrame(posts)
    df['latitude'] = lat
    df['longitude'] = log
    df['city'] = city
    df['country'] = country
    df.to_csv("FB"+place+".csv",encoding="utf8")
    print(df)
except Exception as ex:
    print (ex)
