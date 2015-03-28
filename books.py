#Print name of books liked by id. Id and access token are given by user.

import requests # pip install requests
import json	

base_url = raw_input("Enter the id : ") 
base_url = 'https://graph.facebook.com/' + base_url
ACCESS_TOKEN = raw_input("Paste here the access token : ")
fields ='books{name,likes}'

def get_books():
    """
        Returns the list of posts on my timeline
    """

    parameters = {'access_token': ACCESS_TOKEN}
    r = requests.get('https://graph.facebook.com/741504455940261/books', params=parameters)
    result = json.loads(r.text)
    return result["data"]

r=get_books()
for book in r:
	print "Book:" + book['name'] #+ "is liked by " + book['likes'] + '\n'
