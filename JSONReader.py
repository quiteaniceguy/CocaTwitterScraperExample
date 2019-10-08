import json

tweets = []
for line in open('/home/thomas/twitter-files/tweets.20191005-000211.json', 'r'):
    tweets.append(json.loads(line))

for tweet in tweets:
    print(tweet["text"])
"""
data = json.load(open('/home/thomas/twitter-files/tweets.20191005-000211.json'))

for d in data:
    print(d['id'])
"""
