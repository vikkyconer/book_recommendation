from TwitterAPI import TwitterAPI


SEARCH_TERM = 'books'


CONSUMER_KEY = '7dAmm5AJQzbCueZWgmc9FSg3r'
CONSUMER_SECRET = 'MXxkh4aerxyta2qHCgRw5GglTWpDrdRLgy0yxutWdlSasROOdR'
ACCESS_TOKEN_KEY = '3086559925-Y1VmQ66QIQ2nrnwFEwWUq2mtzgsVaMGS27sBTm9'
ACCESS_TOKEN_SECRET = 'hKObBGxGTlIKr2Y9c5ZurocZImBAnxSPGly3LmFYN0JaP'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

r = api.request('search/tweets', {'q': SEARCH_TERM})

for item in r:
    print(item['text'] if 'text' in item else item)

print('\nQUOTA: %s' % r.get_rest_quota())