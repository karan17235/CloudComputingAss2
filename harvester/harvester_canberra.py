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


print("Setting CouchDb Server")
ip = sys.argv[1]
admin = sys.argv[2]
password = sys.argv[3]
ip='http://'+admin+':'+password+'@'+ip+':5984/' 
couchserver = couchdb.Server(ip)

consumer_key, consumer_secret, access_token, access_secret = get_cred('avijit')
dbname = "canberra"
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
twitter_stream.filter(locations=[148.7828,-35.9149,149.4063,-35.1213], is_async=True)
