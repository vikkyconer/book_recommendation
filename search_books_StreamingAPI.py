from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = '7dAmm5AJQzbCueZWgmc9FSg3r'
csecret = 'MXxkh4aerxyta2qHCgRw5GglTWpDrdRLgy0yxutWdlSasROOdR'
atoken = '3086559925-Y1VmQ66QIQ2nrnwFEwWUq2mtzgsVaMGS27sBTm9'
asecret = 'hKObBGxGTlIKr2Y9c5ZurocZImBAnxSPGly3LmFYN0JaP'

class listener(StreamListener):

	def on_data(self,data):
		print data
		return True
	def on_error(self,status):
		print status





auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["TwitterAPI"])
