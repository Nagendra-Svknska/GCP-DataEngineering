import tweepy as tw
import pandas as pd

consumer_key= 'dym87t0GsJDChrg8JFLGlm4RH'
consumer_secret= 'mU17GeBXjNJ7OoIc2opFXcw5M6FkfdcH6jnZR1ARxo4dEBsZjA'
access_token= '767153245-RVZvCT2sHDV7IjkMtgWDj3ODHOHbYs8qo5H0eGSk'
access_token_secret= '239ifePh920MUfT5W5mvNQguqnwpzKch2ZAQhvbvknCeO'


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
for tweet in tweets:
    print(tweet.text)
