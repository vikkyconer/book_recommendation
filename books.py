#Print name of books liked by id. Id and access token are given by user.

import requests # pip install requests
import json	

MAX_SPACE = 60
#base_url = raw_input("Enter the id : ") 
#base_url = '636504769758172' #naresh id
#base_url = '976238135727023'
#base_url = '738301736264268' # GSB id 
base_url = 'https://graph.facebook.com/v2.3/me?'
ACCESS_TOKEN = raw_input("Paste here the access token : ")
fields = 'friends{name,books{name,likes}}'

def get_spaces(some_string):
    length_of_string = len(some_string)
    spaces = MAX_SPACE - length_of_string
    return " " * spaces
    
def get_books():
    """
        Returns the list of posts on my timeline
    """

    url = base_url + 'fields=' + fields + '&access_token=' + ACCESS_TOKEN
    r = requests.get(url)
    result = json.loads(r.text)
    friends = result['friends']
    friends_list = friends['data']
    return friends_list

def print_books(friends_list):
    for friend_books in friends_list:
        print '\n' + str(friend_books['name']) + '\n'
        try:
            #print "In Try"
            books = friend_books["books"]["data"]
            #print books
            for book in books:
                print '\t' + book['name'] + get_spaces(book['name']) + "likes =" + str(book['likes'])
                
        except:
            print '\t' + "Not read any books"
    #next = friends['paging']

print_books(get_books())
