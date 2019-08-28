def getTweet():
    import tweepy as tw
    import pandas as pd

    consumer_key = 'dym87t0GsJDChrg8JFLGlm4RH'
    consumer_secret = 'mU17GeBXjNJ7OoIc2opFXcw5M6FkfdcH6jnZR1ARxo4dEBsZjA'
    access_token = '767153245-RVZvCT2sHDV7IjkMtgWDj3ODHOHbYs8qo5H0eGSk'
    access_token_secret = '239ifePh920MUfT5W5mvNQguqnwpzKch2ZAQhvbvknCeO'

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    # Define the search term and the date_since date as variables
    search_words = "#wildfires"
    date_since = "2018-11-16"

    # Collect tweets
    tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(5)
    users_locs = []
    # using for loop
    for tweet in tweets:
        # print(tweet.text)
        # print (tweet.user.screen_name)
        # print (tweet.user.location)

        users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.text] for tweet in tweets]

    # print users_locs
    tweet_text = pd.DataFrame(data=users_locs,
                              columns=['user', "location", "tweet"])

    # print tweet_text

    return tweet_text


def publish_messages(project_id, topic_name):
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

    for n in range(1, 10):
        data = u'Message number {}'.format(n)
        # Data must be a bytestring
        data = data.encode('utf-8')
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data=data)
        print(future.result())

    print('Published messages.')
    # [END pubsub_quickstart_publisher]
    # [END pubsub_publish]


# to run the file locally
publish_messages('first-gcp-wordcount','test_twitter')

