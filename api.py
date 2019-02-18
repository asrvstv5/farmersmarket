from yelpapi import YelpAPI
import json

yelp_api = YelpAPI('Oy2NIzC_PlqoBcFV47CjZ408Y5V-touLuxOR-zvLYQWcJWuYQ3M6D0Ws35MKNiR9rQM-biwN8BETbGYPSdYCwYXKCx67-eyg4gILfBtag1e6DjlEGM1vpoY0ISF9WnYx')
business_id = []
outfile = open('business.json', 'w')
with open("zip_code.txt", 'r') as f:
    for line in f:
        zip_code = line.rstrip()
        try:
            search_results = yelp_api.search_query(term = "farmers market", location = str(zip_code)+", IL, US", categories = "farmersmarket")
            for i in search_results['businesses']:
                # response = yelp_api.reviews_query(id = i['id'])
                # print(i,response)
                # print('\n')
                name = i['id']
                if name not in business_id:
                    business_id.append(name)
                    json.dump(i, outfile)
                    print(name)
        except:
            continue

