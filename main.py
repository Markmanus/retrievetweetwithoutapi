import snscrape.modules.twitter as sntwitter
import pandas as pd


#Retrieve tweets from search
query = "cryptocom (from:whalechart) until:2023-05-01 since:2019-01-20"
tweets = []
limit = 5000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date,tweet.user.username, tweet.rawContent])

df = pd.DataFrame(tweets, columns =['Date','User','Tweet'])

print(df)


