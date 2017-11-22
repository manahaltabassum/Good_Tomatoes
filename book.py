import xmltodict, urllib2, json, requests
import key

app_key = key.goodreads_key

def search(query):
    #r = requests.get('https://www.goodreads.com/search/index.xml?key=4IkeRB9CP85RCSGGl2yi5A&q=Ender%27s+Game')
    url = 'https://www.goodreads.com/search/index.xml'
    q = query
    info_d = {'key': app_key, 'q': q}
    r = requests.get(url, params=info_d)
    print r.url
    #return r
    info = r.text
    d = xmltodict.parse(info)
    #print isinstance(d, dict)
    return (d)

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


print search('The+Fault+in+Our+Stars')
#print advancedSearch('The Fault in Our Stars','John Green')
#print advancedSearch('American Pastoral', 'Philip Roth')
#print advancedSearch('we were liars','e lockhart')
