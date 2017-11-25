import xmltodict, urllib2, json, requests
import key

app_key = key.goodreads_key




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
    return (d)




#use search and then filter out those with not same author
def advancedSearch(title, author):
    results = getResultsDict(search(title))
    auth = author.lower()
    auth.replace(' ','')
    print auth
    print isinstance(results, dict)
    new_dict = {}
    for key in results:
        #print results[key][0].lower()
        if ((results[key][0].lower()) == auth):
            #print True
            val = results[key]
            new_dict[key] = val
    for key, val in new_dict.items():
        print key, '=>', val
    return new_dict


    
    
def getResultsDict(info):
    #return info['GoodreadsResponse']['search']['results']['work'][0]['id']['@type']
    num_results = int(info['GoodreadsResponse']['search']['results-end'])
    #print ('num results = ' + num_results)
    counter = 0
    results = {}
    #return json.dumps(info['GoodreadsResponse']['search']['results']['work'][0], indent=2)
    #return info['GoodreadsResponse']['search']['results']['work'][0]['best_book']['title']
    if (num_results > 10):
        num_results = 10
    while (counter < num_results):
        key = info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['title']
        val = []
        author = info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['author']['name']
        val.append(str(author))
        rating = info['GoodreadsResponse']['search']['results']['work'][counter]['average_rating']
        val.append(str(rating))
        num_ratings = info['GoodreadsResponse']['search']['results']['work'][counter]['ratings_count']['#text']
        val.append(str(num_ratings))
        num_reviews = info['GoodreadsResponse']['search']['results']['work'][counter]['text_reviews_count']['#text']
        val.append(str(num_reviews))
        image_url = info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['image_url']
        val.append(str(image_url))
        book_id = info['GoodreadsResponse']['search']['results']['work'][counter]['best_book']['id']['#text']
        val.append(str(book_id))
        results[key] = val
        #print key
        #print val
        counter += 1
    #print len(results)
    '''
    for key, val in results.items():
        print key, '=>', val
    '''
    return results



def getReview(bookID):
    url = 'https://www.goodreads.com/book/show.xml'
    p = {'id': bookID, 'key': app_key}
    r = requests.get(url, params=p)
    print r.url
    info = r.text
    #print info
    d = xmltodict.parse(info)
    #print json.dumps(d, indent=2)
    #return (d)


#print search('The+Fault+in+Our+Stars')
#print getResultsDict(search('The Fault in Our Stars'))
#print getResultsDict(search('We Were Liars'))
#print search('The Fault in Our Stars')
advancedSearch('The Fault in Our Stars','John Green')
#print advancedSearch('American Pastoral', 'Philip Roth')
#print advancedSearch('we were liars','e lockhart')
print getReview(11870085)
