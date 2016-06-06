import urllib
import json

location=raw_input("Enter location: ")

serviceurl="http://maps.googleapis.com/maps/api/geocode/json?"

url= serviceurl+urllib.urlencode({"senor": "false", "address" : location})
urlo=urllib.urlopen(url)

data=urlo.read()

js=json.loads(str(data))

print "place ID: ", js["results"][0]["place_id"]