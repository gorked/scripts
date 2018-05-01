import requests
import json

user = 'noah'
direction = 'HOME'

API_KEY = '<API_KEY>'

NOAH_HOME = '<ADDRESS>'
LAKEHOUSE = '<ADDRESS>'
DAVID_HOME = '<ADDRESS>'
BOX = '900+Jefferson+Avenue+Redwood+City+CA'
SLACK = '<ADDRESS>'
LINKEDIN = '<ADDRESS>'

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
