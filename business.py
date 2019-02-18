from yelpapi import YelpAPI
import json

yelp_api = YelpAPI('Oy2NIzC_PlqoBcFV47CjZ408Y5V-touLuxOR-zvLYQWcJWuYQ3M6D0Ws35MKNiR9rQM-biwN8BETbGYPSdYCwYXKCx67-eyg4gILfBtag1e6DjlEGM1vpoY0ISF9WnYx')

with open('business_id', 'r') as f:
    for line in f:
        id = line.rstrip()
        with open("business_"+id, 'w') as outfile:
            
