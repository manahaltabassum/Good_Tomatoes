import json, requests
import key

app_key = key.nytimes_key

'''Takes in the name of the movie and returns the entire
dict of results which has not been filtered through'''
def search(name):
    url =  "https://api.nytimes.com/svc/movies/v2/reviews/search.json"
    info_d = {'api-key': app_key, 'query':name}
    r = requests.get(url, params=info_d)
    d = r.json()
    if(d['num_results'] == 0):
        return None
    else:
        return getResultsDict(d)

'''Takes in the name of the movie and returns a dict
of only the given name if it exists'''
def advancedSearch(name):
    url =  "https://api.nytimes.com/svc/movies/v2/reviews/search.json"
    q = "'" + name + "'"
    info_d = {'api-key': app_key, 'query':q}
    r = requests.get(url, params=info_d)
    d = r.json()
    if(d['num_results'] == 0):
        return None
    else:
        return getResultsDict(d)

'''Helper Function: Builds the dictionary of results which is cleaner
than the one returned by the NYTimes API. The name of the movie is the
key and the review information is the value as a subdict'''
def getResultsDict(info):
    ans = {}
    for entry in info['results']:
        #making the entries keys strings to
        # avoid key errors when accessing by the title
        title = unicode(entry['display_title']).encode('utf-8')
        d = {}
        d['reviewLink'] = unicode(entry['link']['url']).encode('utf-8')
        d['reviewTitle'] = unicode(entry['headline']).encode('utf-8')
        d['reviewAuthor'] = unicode(entry['byline']).encode('utf-8')
        d['summary'] = unicode(entry['summary_short']).encode('utf-8')
        #sometimes image is None
        if entry['multimedia'] == None:
            d['image_url'] = entry['multimedia']
        else:
            d['image_url'] = unicode(entry['multimedia']['src']).encode('utf-8')
        d['rating'] = unicode(entry['mpaa_rating']).encode('utf-8')
        #sometimes release date is None
        if entry['opening_date'] == None:
            d['released'] = entry['opening_date']
        else:
            d['released'] = unicode(entry['opening_date']).encode('utf-8')
        ans[title] = d
    return ans


#example test cases

dict = search('wonder')
dict2 = advancedSearch('wonder')
for entry in dict:
    print entry
    print dict[entry]
print
print dict2

