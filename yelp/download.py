import json
import requests
import time
from bs4 import BeautifulSoup
import random

def nextpage_url(text):
    # get links of next page
    # input: text of current page
    # output: url of next page. If no next page, output = None.
    
    soup= BeautifulSoup(text, 'lxml')
    for link in soup.find_all('link', rel="next"):
        return(link.get('href'))

def get_text(url):
    # input: link url
    # output: text of urlx
    time.sleep(random.uniform(1.833,3.283))
    r = requests.get(url)
    return r.text

########## BIG PROBLEM HERE ###############################################
def process(text):
    # processing html text
    # input: text
    # output: review file in json format
    
    soup = BeautifulSoup(text, 'lxml')
    
    a = json.loads(soup.find('script', type="application/ld+json").text)
    data['review'].append(a)
    
    # a = soup.find('script', type="application/ld+json")
    # print(a)
    # if a:
    #     print(a)
    #     b = json.loads(a.text)
    #     print(b)
    #     data['review'].append(b)
###########################################################################X
def download(url):
    # download all the reviews on each page
    text = get_text(url)
    next_url = nextpage_url(text)
    print(text)
    
    print("!!!!!!!!!!!!!!!!!!!!")
    print(next_url)
    
    process(text)
    
    print("aaaaaaaaaaaaaaaaaaaaaa")
    
    if next_url:
        
        # print("...................")
        
        text = get_text(next_url)
        process(text)
        
        print("???????????????????")
        
        next_url = nextpage_url(text)


with open('websites/business_id', 'r') as f:
    
    i = 1
    
    for name in f:
        
        if i < 10:
            
            data = {}
            data['review'] = []
            url = "http://www.yelp.com/biz/"+name.rstrip()
            download(url)
            
            i += 1
            
            with open('websites/304/'+name.splitlines()[0]+'.txt', 'w') as outfile:
                json.dump(data, outfile)
