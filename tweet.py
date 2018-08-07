import tweepy

class my_stream_listener(tweepy.StreamListener):
	def on_status(self, status):
		print status.text


consumer_key = "eGUSxAIBWwFFDPYudQUHJDQlB"
consumer_secret = "Z1rNfvPdTSyvXMiYBE34i4SwrEAiHbysbP5vVL0TZEgM46zY1P"
access_token = "241473113-GJ3tZvZyAfHLSluY1AYFmE1AUgX2h1LlhbMH9Ogy"
access_token_secret = "F8WRcgUyLgjzPm8Xgvmd73UDgwVl4gctD0kh7dg3cIqmh"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
'''
user = api.get_user("prashacr7")
status = user.timeline(count=1)
l = []
l.extend(status)

for tweet in l:
	x=tweet.text.encode("utf-8")
	print x
'''

myStreamListener = my_stream_listener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=[''],async=True)
