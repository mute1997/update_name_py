import tweepy
from tweepy.auth import OAuthHandler
from tweepy.api import API

class myException(Exception): pass

class StreamListener(tweepy.streaming.StreamListener):
    def __init__(self):
        super(StreamListener,self).__init__()

    def on_status(self,status):
        text = status.text
        if("@mute1008 update_name" in text):
            print text.replace("@mute1008 update_name ","")
            auth = get_oauth()
            api = tweepy.API(auth)
            api.update_profile(name = text.replace("@mute1008 update_name ",""))
        return True
    
    def on_error(self,status):
        print("can't get")

    def on_timeout(self):
        raise myException

def get_oauth():
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    return auth

if __name__ == '__main__':
    auth = get_oauth()
    stream = tweepy.Stream(auth,StreamListener(),secure=True)
    stream.userstream()
