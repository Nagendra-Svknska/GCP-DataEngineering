import tweepy

# import Tweet_Streaming as tstream

def get_api():
    # print 'entered get_api'
    auth = tweepy.OAuthHandler('wY2Wq2uW05iMvgbUEVZ2ShkzB','eeAmJqnsLvP8cnfuuyYHxto5fTGX0KQdgDx6jOTJSVI17qc4Eb')
    auth.set_access_token('701674298402934784-KmoYZznFIt0LXuy8b1WuKjrbv4kPSwq','GfOguC80gI4kvuqxwQPW41M9o2BViYwFrD9hPOaMzajp4')

    return auth



#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print 'status'

        print(status.text)

    def on_error(self, status_code):
        print 'on error stub'
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False



print 'search value :'
myStreamListener = MyStreamListener
auth=get_api()
# api=tstream.streaming_tweet()
myStream = tweepy.Stream(auth=auth, listener=myStreamListener())
myStream.filter(track=['python'])
myStream.filter(track=['python'], async=True)