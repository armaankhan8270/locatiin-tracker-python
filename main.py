import phonenumbers
import folium
import opencage
filename=input("enter the name of user")
mynumber=input("enter mobile number")
from myphonenumber import number
from phonenumbers import geocoder
pipnumber = phonenumbers.parse(mynumber)
location = geocoder.description_for_number(pipnumber,"en")
print(location)
from phonenumbers import carrier
service=phonenumbers.parse(mynumber)
print(carrier.name_for_number(service,"en"))
from opencage.geocoder import OpenCageGeocode
key="a158bc0e3f29418e8ff946631f53bb2e"
geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)
mymap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(mymap)
mymap.save("user.html")

