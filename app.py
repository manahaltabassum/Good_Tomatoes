from flask import Flask, render_template, request, session, redirect, url_for, flash
import book, movie

app = Flask(__name__)

title = None

@app.route('/')
def root ():
    return render_template ('welcome.html')
'''
@app.route('/searched', methods = ['post','get'])
def searched():
    title = request.form['q']
    bookDict = book.search(title)
    bookTitle = bookDict.keys()[0]
    bookID = bookDict[bookTitle]["book_id"]
    return render_template("searched.html", title=title, bookSearch = bookDict, bkTitle = bookTitle, bkID = bookID)
'''

@app.route('/searched', methods = ['post','get'])
def searched():
    global title
    if 'q' in request.form:
        title = request.form['q']
    if (book.search(title) != None):
        best_book = book.getBest(book.search(title)).items()[0]
    else:
        best_book = None;
    if (movie.advancedSearch(title) != None):
        best_movie = movie.advancedSearch(title).items()[0]
    else:
        best_movie = None;
    return render_template("searched.html", title=title, book = best_book, movie = best_movie)

@app.route('/searchedbook', methods = ['post','get'])
def searchedbook():
    global title
    #bookname = request.form['q']
    search_dict = book.search(title)
    author = None;
    if ('author' in request.form):
        author = request.form['author']
        search_dict = book.advancedSearch(title, author)

    return render_template("bookreviews.html", type="book", search=title, dict = search_dict, author = author)

@app.route('/searchedmovie', methods = ['post','get'])
def searchedmovie():
    global title
    #moviename = request.form['q']
    search_dict = movie.search(title)
    return render_template("moviereviews.html", type= "movie", search=title, dict= search_dict)

@app.route('/fullbook', methods = ['post','get'])
def fullbook():
    global title
    review = book.getReview(request.form['bookID'])
    return render_template("fullbook.html", review = review)


if __name__ == '__main__':
    app.run(debug=True)
