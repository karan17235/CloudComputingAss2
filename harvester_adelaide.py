import tweepy
import time
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'KLuHLSpESjdyg3MSOnX2QM7hd'
consumer_secret = 'XFdbhNhHH2SAX1kO4BJ8mXqakelwuCZduh7flCWZbjBabR1fPr'
access_token = '962792160-dBQwMGmaoCa3atwCBNfMSVjgc0zvLZW0J1CTbfth'
access_secret = 'tLL5UadqSXrpKd0oqu22kqRyMleoBsElmGXYuqRXNqrO8'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self,data):
        try:
            with open("adelaide.json","a") as f:
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
twitter_stream.filter(locations=[138.42,-35.10,138.87,-34.78], is_async=True)
