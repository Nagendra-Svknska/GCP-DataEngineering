def publish_messages(project_id, topic_name,message):
    """Publishes multiple messages to a Pub/Sub topic."""
    # [START pubsub_quickstart_publisher]
    # [START pubsub_publish]
    from google.cloud import pubsub_v1

    # TODO project_id = "Your Google Cloud Project ID"
    # TODO topic_name = "Your Pub/Sub topic name"

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_name}`
    topic_path = publisher.topic_path(project_id, topic_name)

    data=message
    data=data.encode('utf-8')
    future = publisher.publish(topic_path, data=data)
    print(future.result())


    print('Published messages.')
    # [END pubsub_quickstart_publisher]
    # [END pubsub_publish]

import tweepy as tw

# import Tweet_Streaming as tstream

def get_api():
    # print 'entered get_api'
    auth = tw.OAuthHandler('wY2Wq2uW05iMvgbUEVZ2ShkzB','eeAmJqnsLvP8cnfuuyYHxto5fTGX0KQdgDx6jOTJSVI17qc4Eb')
    auth.set_access_token('701674298402934784-KmoYZznFIt0LXuy8b1WuKjrbv4kPSwq','GfOguC80gI4kvuqxwQPW41M9o2BViYwFrD9hPOaMzajp4')

    return auth



#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tw.StreamListener):

    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.count=0
        pass

    def on_status(self, status):

        print 'on status'
        print(status.text)

        if(self.count<5):
            message=status.text
            import unicodedata
            message=unicodedata.normalize('NFKD', message).encode('ascii', 'ignore')
            # print message
            # print type(message)
            # print (message)
            # for tweet in tw.Cursor(self.on_limit())
            # self.count=0
            self.count=self.count+1
            print ('self count variable :',self.count)
            project_id = 'first-gcp-wordcount'
            topic_name = 'test_twitter'
            publish_messages(project_id, topic_name, message)
        else :
            return False

    def on_error(self, status_code):
        print 'on error stub'
        # print status_code
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False



print 'search value :'
myStreamListener = MyStreamListener
auth=get_api()
# api=tstream.streaming_tweet()
myStream = tw.Stream(auth=auth, listener=myStreamListener())
myStream.filter(track=['python'])
# myStream.filter(track=['python'], async=True)