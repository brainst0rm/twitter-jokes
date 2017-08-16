import tweepy, requests, sys, time
from keys import *

#auth

def mybot():
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(akey, asecret)
    api = tweepy.API(auth)
    # status update
    responseData = requests.get('http://api.icndb.com/jokes/random/?escape=javascript')
    mystatustext = str(responseData.json()['value']['joke'] + '#mybot')[:140]
    api.update_status(mystatustext)
    # api.update_status('my app update')

def main():
    print('its working')
while True:
    mybot()
    time.sleep(300) # 5 minute

if __name__ == "__main__":
    mybot()
