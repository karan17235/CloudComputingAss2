import tweepy
import time
import json
import sys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import couchdb
import sentiment_analysis_tweet

from twitter_credentials import get_cred

#@classmethod
#def parse(cls, api, raw):
#	status = cls.first_parse(api, raw)
#	setattr(status, 'json', json.dumps(raw))
#	return status

#tweepy.models.Status.first_parse = tweepy.models.Status.parse
#tweepy.models.Status.parse = parse


user = "admin"
password = "admin"
print("Setting CouchDb Server")
couchserver = couchdb.Server('http://%s:%s@172.26.38.45:5984/' % (user,password))

consumer_key, consumer_secret, access_token, access_secret = get_cred('srijan')
dbname = "immigrant_keywords"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
print("Getting Twitter Authentication")
api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self,data):
        try:
            print("Getting Status")
            x = json.loads(data)
            if dbname in couchserver:
                print("Found Database")
                db = couchserver[dbname]
            else:
                print("Creating Database")
                db = couchserver.create(dbname)

            print("Setting unique key")
            x['_id'] = str(x['id_str'])
            if (x.get("extended_tweet")):
                label = sentiment_analysis_tweet.sentiment_label(str(x["extended_tweet"]["full_text"]))
            elif x.get("text"):
                label = sentiment_analysis_tweet.sentiment_label(str(x["text"]))

            x["Label"] = label
 


            print("Saving Data into db")
            db.save(x)
            print("Saved!")
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        if status == 420:
            sys.stderr.write("Rate limit exceeded\n".format(status))
            time.sleep(15*60)
            return True
        else:
            print(status)
    def on_exception(self,e):
        time.sleep(10*60)
        print("Exception Raised..Now Sleeping")
print("Setting Twitter Stream")

while True:
    try:
        twitter_stream = Stream(auth, MyListener())
        twitter_stream.filter(track='immigrant housing australia,immigrant job australia, travelling australia, settling australia, migrating to australia', is_async=True)
    except IncompleteRead:
        print("Lagging Behind")
        continue
    
