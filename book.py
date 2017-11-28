import xmltodict, json, requests
import key

#THIS FIXES ENCODE ERROR
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app_key = key.goodreads_key


'''All search methods return a dictionary with entries in the following manner:
{<title1>:[<author1>,<avg_rating1>,<num_ratings1>,<num_reviews1>,<image_url1>,<book_id1>]
 <title2>:[<author2>,<avg_rating2>,<num_ratings2>,<num_reviews2>,<image_url2>,<book_id1>]
 ...}
'''

'''Takes in the title of the book and returns the entire
dict of results which has not been filtered through'''
def search(query):
    url = 'https://www.goodreads.com/search/index.xml'
    q = query
    info_d = {'key': app_key, 'q': q}
    r = requests.get(url, params=info_d)
    #print r.url
    #return r
    info = r.text
    d = xmltodict.parse(info)
    #print isinstance(d, dict)
    #print json.dumps(d, indent=2)
    return getResultsDict(d)




'''Takes in the title and author of the book and returns a dict
of search results that is more specific than the regular search'''
def advancedSearch(title, author):
    auth = author.split()
    #print auth
    for x in range(len(auth)):
        auth[x] = auth[x].lower()
    #print auth
    results = search(title)
    new_dict = {}
    for key in results:
        found = False
        for x in range(len(auth)):
            if (auth[x] in (results[key]['author'].lower())):
                found = True
            else:
                found = False
        if (found == True):
            new_dict[key] = results[key]
    if (len(new_dict) == 0):
        return None
    else:
        return new_dict



'''Builds the dictionary of results which is cleaner than that
returned by the goodreads API. Check above for the structure.'''
def getResultsDict(info):
    num_results = int(info['GoodreadsResponse']['search']['results-end'])
    print ('num results = ' + str(num_results))
    if (num_results == 0):
        return None
    counter = 0
    results = {}
    while (counter < num_results):
        key = info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['title']
        val = {}
        author = str(info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['author']['name'])
        val['author'] = author
        rating = info['GoodreadsResponse']['search']['results']['work'][counter]['average_rating']
        val['rating'] = str(rating)
        num_ratings = info['GoodreadsResponse']['search']['results']['work'][counter]['ratings_count']['#text']
        val['num_ratings'] = str(num_ratings)
        num_reviews = info['GoodreadsResponse']['search']['results']['work'][counter]['text_reviews_count']['#text']
        val['num_reviews'] = str(num_reviews)
        image_url = info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['image_url']
        val['image_url'] = str(image_url)
        book_id = info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['id']['#text']
        val['book_id'] = str(book_id)
        results[key] = val
        counter += 1
    #print len(results)
    #for key, val in results.items():
        #print key, '=>', val
    return results

'''Uses the bookID in order to search up the reviews. Need to access bookID
from the resultsDict from before in order to use this method. It will return
html code for a reviews_widget which can just be added into the html code'''
def getReview(bookID):
    url = 'https://www.goodreads.com/book/show.xml'
    p = {'id': bookID, 'key': app_key}
    r = requests.get(url, params=p)
    #print r.url
    info = r.text
    #print info
    d = xmltodict.parse(info)
    #print json.dumps(d, indent=2)
    return d['GoodreadsResponse']['book']['reviews_widget']
    #return (d)



'''Takes in a dictionary and traverses through it
to give you the best entry which is determined by the greatest
number of ratings. It returns a dictionary with one key.''' 
def getBest(info):
    best_result = None
    best_num_ratings = 0
    result = {}
    for key in info:
        print info[key]['num_ratings']
        if (int(info[key]['num_ratings']) > best_num_ratings):
            best_result = key
            print best_result
            best_num_ratings = int(info[key]['num_ratings'])
            print best_num_ratings
    result[best_result] = info[best_result]
    return result


#TEST CASES

#print search('The+Fault+in+Our+Stars')
#print search('The Fault in Our Stars')
#print advancedSearch('The Fault in Our Stars', 'John Green')
#print getResultsDict(search('The Fault in Our Stars'))
#print getResultsDict(search('We Were Liars'))
#print search('The Fault in Our Stars')
#advancedSearch('The Fault in Our Stars','John Green')
#print advancedSearch('American Pastoral', 'Philip Roth')
#print advancedSearch('we were liars','e lockhart')
#print getReview(11870085)
#print search('love')
#print getBest(search('The Fault in Our Stars'))
