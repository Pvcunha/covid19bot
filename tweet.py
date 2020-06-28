import os
import time
import tweepy


class TwitterHandler:
    def __init__(self):
        
        #Tokens set up
        self.CONSUMER_KEY = str(os.environ.get('CONSUMER_KEY'))
        self.CONSUMER_SECRET = str(os.environ.get('CONSUMER_SECRET'))
        self.ACCESS_TOKEN = str(os.environ.get('ACCESS_TOKEN'))
        self.ACCESS_SECRET = str(os.environ.get('ACCESS_SECRET'))
       
       #Handling auth
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        
        self.api = tweepy.API(self.auth)

    #Posting on twitter
    def post(self, text):
        self.api.update_status(text)
        print(f'Postado: {text}')

bot = TwitterHandler()