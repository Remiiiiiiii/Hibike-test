# theHibikeBot

import tweepy as tp
import time
import os

# login to twitter API
consumer_key = '3wi6SHhXtML8CyWIbzsHYGP9z'
consumer_secret = 'A4V2UvThaSao8PEi2TGQlS1xhAuiU9OTVIvJ3w3EDObXJxSt2f'
access_token = '1323040469891297281-2JsPkqcGmsxQHfcE8z17kixAtLuuGW'
access_secret = '0pB8EBcgBpU3DZJeO63Grq1V8L0nPfk9dxTwjilnGRUh4'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# iterates over pictures in HibikePic folder
os.chdir('HibikePic')
for Hibike_image in os.listdir('.'):
    api.update_with_media(Hibike_image)
    time.sleep(10)