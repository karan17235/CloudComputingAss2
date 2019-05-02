import tweepy
import time
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'PIBXhu0jRHKmfwGhwKn7wD4pr'
consumer_secret = 'HhJTL9t4qAC3LSHAhYq2C0VbqyMN15FAY1kwNBZFLNoUS6UDra'
access_token = '490286007-vVGoq9J7ErGRf39Mr4XotspjsnsPG1nyuwRKMrKX'
access_secret = 'd384phuU8wRXGbHCsqkyzFoj0U04cmKph8C3Dvt7U70XJ'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self,data):
        try:
            with open("melbourne.json","a") as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        if status == 420:
            sys.stderr.write("Rate limit exceeded\n".format(status))
            return False
        else:
            print(status)
            return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(locations=[144.74,-38.13,145.34,-37.52], is_async=True)
