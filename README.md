# twitter-news

Get the latest tweets mentioning some keyword(s) of your choice.

## Usage
To run the app, use the [streamlit](https://streamlit.io/) command from the terminal :
```
streamlit run get_tweets_app.py
```

You will need to store some tweeter api credentials inside a `secrets.ini` file. The format of the file is the following :

```
[API]
key = ...
secret_key = ...

[Token]
access_token = ...
access_token_secret = ...
```
