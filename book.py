import xmltodict, urllib2, json, requests
import key

app_key = key.goodreads_key

def search(query):
    #r = requests.get('https://www.goodreads.com/search/index.xml?key=4IkeRB9CP85RCSGGl2yi5A&q=Ender%27s+Game')
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
    url = 'https://www.goodreads.com/book/title.xml'
    info_d = {'author': author, 'key': app_key, 'title': title}
    r = requests.get(url, params=info_d)
    print r.url
    info = r.text
    d = xmltodict.parse(info)
    #return (d)
    #book_isbn = d['GoodreadsResponse']['book']['id']
    #return book_isbn
    #return search(book_isbn)

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
        results[key] = val
        #print key
        #print val
        counter += 1
    #print len(results)
    for key, val in results.items():
        print key, '=>', val


#print search('The+Fault+in+Our+Stars')
print getResultsDict(search('The Fault in Our Stars'))
#print getResultsDict(search('We Were Liars'))
#print search('The Fault in Our Stars')
#print advancedSearch('The Fault in Our Stars','John Green')
#print advancedSearch('American Pastoral', 'Philip Roth')
#print advancedSearch('we were liars','e lockhart')
