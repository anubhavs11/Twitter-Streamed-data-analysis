
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1000286369413873664-nAgh2tNaoBoxvBung3gqg0H4cF2GBe"
access_token_secret = "zTtq8xWSa7ZIEzy1pKtzmIF7Wx9TXIV7c3xHL6sZG67cG"
consumer_key = "e4omtXv9uLZnKWgMIKDcDOmPR"
consumer_secret = "M429qBFcSOaEiOINGAUi4B7PomzE3txAQzLIPTK3u7PyPKPYGU"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)


    stream.filter(track=['python', 'java', 'c++'])

