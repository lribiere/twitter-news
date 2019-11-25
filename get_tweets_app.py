import tweepy
import configparser
import pandas as pd
import streamlit as st

API_SECTION_NAME = 'API'
TOKEN_SECTION_NAME = 'Token'
KEY_FIELD_NAME = 'key'
SECRET_KEY_FIELD_NAME = 'secret_key'
ACCESS_TOKEN_FIELD_NAME = 'access_token'
ACCESS_TOKEN_SECRET_FIELD_NAME = 'access_token_secret'

AUTHOR_NAME = 'author_name'
AUTHOR_SCREEN_NAME = 'screen_name'
TWEET_TEXT = 'full_text'
TWEET_TIME = 'time'
ALL_COLUMNS = [AUTHOR_NAME,
               AUTHOR_SCREEN_NAME,
               TWEET_TEXT,
               TWEET_TIME]

'''
# Tweeter News App
This very simple webapp allows you to collect and visualize some tweets.
'''


def check_secrets():
    # TODO
    pass


secrets = configparser.ConfigParser()
secrets.read('secrets.ini')
check_secrets()

api_key = secrets[API_SECTION_NAME][KEY_FIELD_NAME]
api_secret_key = secrets[API_SECTION_NAME][SECRET_KEY_FIELD_NAME]
access_token = secrets[TOKEN_SECTION_NAME][ACCESS_TOKEN_FIELD_NAME]
access_token_secret = secrets[TOKEN_SECTION_NAME][ACCESS_TOKEN_SECRET_FIELD_NAME]

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_dict = {AUTHOR_NAME: [],
              AUTHOR_SCREEN_NAME: [],
              TWEET_TEXT: [],
              TWEET_TIME: []}
query = st.text_input('Enter some keywords')
if query is not '':
    for tweet in tweepy.Cursor(api.search,
                               q=query,
                               result_type='mixed',
                               count=100,
                               tweet_mode='extended').items(1000):
        author_name = tweet.author.name
        author_screen_name = tweet.author.screen_name
        tweet_text = tweet.full_text
        tweet_time = tweet.created_at
        tweet_dict[AUTHOR_NAME].append(author_name)
        tweet_dict[AUTHOR_SCREEN_NAME].append(author_screen_name)
        tweet_dict[TWEET_TEXT].append(tweet_text)
        tweet_dict[TWEET_TIME].append(tweet_time)

    tweets_df = pd.DataFrame.from_dict(tweet_dict)
    st.write(tweets_df)
    filename = '_'.join(query.split(' ')) + '_tweet.csv'
    tweets_df.to_csv(filename, index=False)
