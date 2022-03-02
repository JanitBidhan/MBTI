import tweepy

def twitterPull(username):

    client = tweepy.Client(bearer_token='#ENTER YOUR BEARER TOKEN HERE')

    i = 0

    tweetlist = ''

    userID = client.get_user(username = username).data.id
    tweets = client.get_users_tweets(id = userID, max_results = 100, exclude = ['retweets'])

    for tweet in tweets[0]:

        tweetlist = "|||".join([tweetlist, tweet.text])

    return tweetlist