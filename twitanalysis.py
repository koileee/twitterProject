import twitauth
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
