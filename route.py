import requests
import json

user = 'noah'
direction = 'HOME'

API_KEY = 'AIzaSyAj1zDIkQO0FlvWU1PN7LGr8RJWmQHHVj8'

NOAH_HOME = '6+Seville+Way+San+Mateo+CA'
LAKEHOUSE = '448+Fathom+Drive+San+Mateo+CA'
DAVID_HOME = '939+University+Ave+Palo+Alto+CA'
BOX = '900+Jefferson+Avenue+Redwood+City+CA'
SLACK = '155+5th+Street+San+Francisco+CA'
LINKEDIN = '222+2nd+Street+San+Francisco+CA'

def get_travel_time(origin, destination, key):
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&key=%s" % (origin, destination, key)
    r = requests.get(url)
    output = json.loads(r.text)
    duration = output["routes"][0]["legs"][0]["duration"]["text"]
    route = output["routes"][0]["summary"]
    return "%s via %s" % (duration, route)

if user == 'noah':
    if direction == 'HOME':
        print(get_travel_time(BOX, NOAH_HOME, API_KEY))
    elif direction == 'WORK':
        print(get_travel_time(NOAH_HOME, BOX, API_KEY))
    else:
        print('FAIL')

#print(get_travel_time(BOX, NOAH_HOME, API_KEY))
