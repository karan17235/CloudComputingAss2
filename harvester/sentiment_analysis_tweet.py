import sys
import re
from textblob import TextBlob
from nltk.tokenize import WordPunctTokenizer

tok = WordPunctTokenizer()

def sentiment_label(text):

    print("Working on tweet:"+ text)

    text = text.encode("utf-8")
    
    user_removed = re.sub(r'@[A-Za-z0-9]+','',text.decode('utf-8'))
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^A-Za-z]',' ',link_removed)
    lower_case_tweet = number_removed.lower()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = TextBlob((' '.join(words)).strip())

    sentiment_score = float(clean_tweet.sentiment.polarity)

    

    if sentiment_score > 0:
        label = "POSITIVE"
    elif sentiment_score == 0:
        label = "NEUTRAL"
    else:
        label = "NEGATIVE"
    
    return label

