import tweepy


def get_api():
    auth = tweepy.OAuthHandler('wY2Wq2uW05iMvgbUEVZ2ShkzB', 'eeAmJqnsLvP8cnfuuyYHxto5fTGX0KQdgDx6jOTJSVI17qc4Eb')
    api = tweepy.API(auth)
    api.update_status('tweepy + oauth!')
    return api