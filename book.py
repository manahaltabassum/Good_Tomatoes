import xmltodict, json, requests
import key

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
    #results = getResultsDict(search(title))
    results = search(title)
    auth = author.lower()
    auth.replace(' ','')
    #print auth
    #print isinstance(results, dict)
    new_dict = {}
    for key in results:
        #print results[key][0].lower()
        if ((results[key][0].lower()) == auth):
            #print True
            val = results[key]
            new_dict[key] = val
    '''
    for key, val in new_dict.items():
        print key, '=>', val
    '''
    return new_dict



'''Builds the dictionary of results which is cleaner than that
returned by the goodreads API. Check above for the structure.'''
def getResultsDict(info):
    num_results = int(info['GoodreadsResponse']['search']['results-end'])
    print ('num results = ' + str(num_results))
    counter = 0
    results = {}
    while (counter < num_results):
        key = unicode(info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['title']).encode('utf-8')
        #val = []
        val = {}
        author = unicode(info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['author']['name']).encode('utf-8')
        val['author'] = author
        #val.append(unicode(author).encode('utf-8'))
        rating = info['GoodreadsResponse']['search']['results']['work'][counter]['average_rating']
        val['rating'] = str(rating)
        #val.append(str(rating))
        num_ratings = info['GoodreadsResponse']['search']['results']['work'][counter]['ratings_count']['#text']
        val['num_ratings'] = str(num_ratings)
        #val.append(str(num_ratings))
        num_reviews = info['GoodreadsResponse']['search']['results']['work'][counter]['text_reviews_count']['#text']
        val['num_reviews'] = str(num_reviews)
        #val.append(str(num_reviews))
        image_url = info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['image_url']
        val['image_url'] = str(image_url)
        #val.append(str(image_url))
        book_id = info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['id']['#text']
        val['book_id'] = str(book_id)
        #val.append(str(book_id))
        results[key] = val
        #print key
        #print val
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
