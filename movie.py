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
        t = "" + entry['display_title']
        title = t
        d = {}
        d['reviewLink'] = entry['link']['url']
        d['reviewTitle'] = entry['headline']
        d['reviewAuthor'] = entry['byline']
        d['summary'] = entry['summary_short']
        d['rating'] = entry['mpaa_rating']
        #sometimes release date is None
        d['released'] = entry['opening_date']
        ans[entry['display_title']] = d
    return ans


#example test cases
'''
dict = search('wonder')
dict2 = advancedSearch('wonder')
for entry in dict:
    print entry
    print dict[entry]
print
print dict2
'''
