#Print name of books liked by id. Id and access token are given by user.

import requests # pip install requests
import json	

base_url = raw_input("Enter the id : ") 
#base_url = '636504769758172' #naresh id
#base_url = '976238135727023'
base_url = 'https://graph.facebook.com/v2.3/' + base_url + '?'
ACCESS_TOKEN = raw_input("Paste here the access token : ")
#ACCESS_TOKEN = 'CAACEdEose0cBAGqs1WOWOBp22B0kvWItZCwPfiKHFyaWA45NZCvtgL8cS3USqWC7CUT8spTbJDKgU2D7x5bVm7w33IYiTjqUjK56uJOA1hpjpouEEKRcj6DnxoF3CO52kv5K1ouq4lrH24QyBS7BE5LcSw6RiYBC6UxN39ZAcugReNfdFhmiWhqJAIY6egEF6aRalIfk3mdu8yWCJ1yk9MqsjhiMHYZD'
fields ='name,books{name,likes}'

def get_books():
    """
        Returns the list of posts on my timeline
    """

    url = base_url + 'fields=' + fields + '&access_token='+ACCESS_TOKEN	
    r = requests.get(url)
    result = json.loads(r.text)
    print result['name']
    try:
	print result['books']
	books = result["books"]
	return books['data']
    except:
	print "Not read any books"
    return 0

r=get_books()
if r != 0:
    for book in r:
	print "Book:" + book['name'] #+ "is liked by " + book['likes'] + '\n'

