import json
data = {}
data['business']= []

with open("url.json", 'w') as outfile:
    for zip_code in range(60001, 63000):
        data['business'].append({
            'zip_code': zip_code,
            'website': "http://www.yelp.com/search?find_desc=farmers+market&find_loc="+str(zip_code)+"&start=0&cflt=farmersmarket"
        })

with open('url.txt', 'w') as outfile:  
    json.dump(data, outfile)
