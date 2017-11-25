import urllib2
import json

def search(name):
    link = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=48a9c92b946e4c09b902e97f12663af1&query=https://api.nytimes.com/svc/books/v3/lists/overview.json?api-key=48a9c92b946e4c09b902e97f12663af1&query='" + name + "'"
    u = urllib2.urlopen(link)
    d = json.loads(u.read())
    if(d['num_results'] == 0):
        print("Results")
        link = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=48a9c92b946e4c09b902e97f12663af1&query=https://api.nytimes.com/svc/books/v3/lists/overview.json?api-key=48a9c92b946e4c09b902e97f12663af1&query=" + name
        u = urllib2.urlopen(link)
        d = json.loads(u.read())
    else:
        print("We found a movie with that exact title!")
    print link
    print d
    return d

#search('wonders')
dict = search('wonder')
