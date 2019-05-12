import tweepy
import time
import json
import sys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import couchdb
from twitter_credentials import get_cred
import sentiment_analysis_tweet

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

consumer_key, consumer_secret, access_token, access_secret = get_cred('karan')
dbname = "melbourne"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
print("Getting Twitter Authentication")
api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self,data):
        try:
            print("Getting Status")
            print(type(data))
            x = json.loads(data)
            print(type(data))
            print(x)
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
        except tweepy.RateLimitError:
            print("Rate Limit Error")
            time.sleep(15*60)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        if status == 420:
            sys.stderr.write("Rate limit exceeded\n".format(status))
        else:
            print(status)

print("Setting Twitter Stream")
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(locations=[144.5937,-38.5047,145.6299,-37.5113], is_async=True)
