#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "867126361038745600-n6be8H21Pt0ozfjjKgclIxFB2snN5VM"
access_token_secret = "riYL5KckA814dk5lKVAUuBNyHRGYkXZum3VivJx4A8Kws"
consumer_key = "rsu3Izl6lShtLczsXj6QET5hi"
consumer_secret = "5s28SOzXTmAhbdkDFWWHSlD0guWZDmy3uqvPj4RZc5hIiQPFn6"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        # decoded = json.loads(data)
        # print (decoded['user']['screen_name'],decoded['text'])
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
#    stream.filter(track=['tiramisu',"black forest","cheesecake","pandan","pavlova","tres leches","victoria sponge","baklava","dorayaki","madeleines"])
#    stream.filter(track=['farmers market'])
    # //start at 11/08/2017 7:50 pm
    stream.filter(track=['food poisoning'])
    # start at 9/19/2018
