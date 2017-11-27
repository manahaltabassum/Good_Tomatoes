import urllib2
import json
import key

app_key = key.nytimes_key

'''Takes in the name of the movie and returns the entire
dict of results which has not been filtered through'''
def search(name):
    link = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=" + app_key + "&query=" + name
    u = urllib2.urlopen(link)
    d = json.loads(u.read())
    return d

'''Takes in the name of the movie and returns a dict
of only the given name if it exists'''
def advancedSearch(name):
    link = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=" + app_key + "&query='" + name + "'"
    u = urllib2.urlopen(link)
    d = json.loads(u.read())
    #if(d['num_results'] == 0):
        #print("No corresponding book was found")
    #else:
        #print("Corresponding book found!")
    return d

'''Builds the dictionary of results which is cleaner than that
returned by the NYTimes API. The name of the movie is the key
and the review information is the value as a subdict'''
def getResultsDict(info):
    ans = {}
    for entry in info['results']:
        #making the entries keys strings to
        # avoid key errors when accessing by the title
        t = "" + entry['display_title']
        title = t
        d = {}
        d['reviewLink'] = entry['link']['url']
        d['reviewTitle'] = entry['headline']
        d['reviewAuthor'] = entry['byline']
        d['reviewSummary'] = entry['summary_short']
        d['rating'] = entry['mpaa_rating']
        #sometimes release date is None
        d['released'] = entry['opening_date']
        ans[entry['display_title']] = d
    return ans


#example test cases
dict = search('wonder')
dict2 = advancedSearch('wonder')
d = getResultsDict(dict)
d2 = getResultsDict(dict2)
#for entry in d:
    #str = "" + entry + ""
    #print entry
    #print d[entry]
#print
#print d2
