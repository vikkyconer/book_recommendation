#Print name of books liked by id. Id and access token are given by user.

import requests # pip install requests
import json	

#base_url = raw_input("Enter the id : ") 
#base_url = '636504769758172' #naresh id
base_url = '976238135727023'
base_url = 'https://graph.facebook.com/v2.3/' + base_url + '?'
#ACCESS_TOKEN = raw_input("Paste here the access token : ")
ACCESS_TOKEN = 'CAACEdEose0cBAGqs1WOWOBp22B0kvWItZCwPfiKHFyaWA45NZCvtgL8cS3USqWC7CUT8spTbJDKgU2D7x5bVm7w33IYiTjqUjK56uJOA1hpjpouEEKRcj6DnxoF3CO52kv5K1ouq4lrH24QyBS7BE5LcSw6RiYBC6UxN39ZAcugReNfdFhmiWhqJAIY6egEF6aRalIfk3mdu8yWCJ1yk9MqsjhiMHYZD'
fields = 'friends{books,name}'
def get_books():
    """
        Returns the list of posts on my timeline
    """

    url = base_url + 'fields=' + fields + '&access_token='+ACCESS_TOKEN	
    r = requests.get(url)
    result = json.loads(r.text)
    friends = result['friends']
    friends_list = friends['data']
    for friend_books in friends_list:
	print ""
	print friend_books['name']
	print ""
        try:
	    books = friend_books["books"]
	    book_data = books['data']
	    for book in book_data:
		print "Book:" + book['name'] #+ "is liked by " + book['likes'] + '\n'
        except:
	    print "Not read any books"
    #next = friends['paging']        

get_books()

