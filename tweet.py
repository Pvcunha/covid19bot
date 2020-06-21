import time
import tokens
import tweepy


class TwitterHandler:
    def __init__(self):
        self.CONSUMER_KEY, self.CONSUMER_SECRET = tokens.get_consumer_keys()
        self.ACCESS_TOKEN, self.ACCESS_SECRET = tokens.get_access_tokens_keys()

        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        
        self.api = tweepy.API(self.auth)

    def post(self, text):
        self.api.update_status(text)
        print(f'Postado: {text}')
