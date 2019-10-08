from nltk.twitter import Twitter
tw = Twitter()
results = tw.tweets(to_screen=False, keywords = 'angry, upset', limit=1000)



