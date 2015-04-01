#Print name of books liked by id. Id and access token are given by user.

import requests # pip install requests
import json	

base_url = raw_input("Enter the id : ") 
base_url = 'https://graph.facebook.com/v2.3/' + base_url + '?'
ACCESS_TOKEN = raw_input("Paste here the access token : ")
fields ='books{name,likes}'

def get_books():
    """
        Returns the list of posts on my timeline
    """

    url = base_url + 'fields=' + fields + '&access_token='+ACCESS_TOKEN	
    r = requests.get(url)
    result = json.loads(r.text)
    books = result["books"]
    return books['data']

r=get_books()
for book in r:
	print "Book:" + book['name'] #+ "is liked by " + book['likes'] + '\n'
