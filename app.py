from flask import Flask, render_template, request, session, redirect, url_for, flash
from utils import book, movie

app = Flask(__name__)

title = None

@app.route('/')
def root ():
    return render_template ('welcome.html')

@app.route('/searched', methods = ['post','get'])
def searched():
    global title
    if 'q' in request.form:
        title = request.form['q']
    bookdict = book.search(title)
    if (bookdict != None and bookdict != {}):
        best_book = book.getBest(bookdict).items()[0]
    else:
        best_book = None;
    moviedict = movie.advancedSearch(title)
    if (moviedict != None and moviedict != {}):
        best_movie = moviedict.items()[0]
    else:
        best_movie = None;
    return render_template("searched.html", title=title, book = best_book, movie = best_movie)

@app.route('/searchedbook', methods = ['post','get'])
def searchedbook():
    global title
    search_dict = book.search(title)
    author = None;
    numResults = None;
    if ('author' in request.form):
        author = request.form['author']
        search_dict = book.advancedSearch(title, author)
    if ('numResults' in request.form):
        numResults = request.form['numResults']
        search_dict = book.numResults(numResults, search_dict)
    return render_template("bookreviews.html", type="book", search=title, dict = search_dict, author = author, num = numResults)

@app.route('/searchedmovie', methods = ['post','get'])
def searchedmovie():
    global title
    #moviename = request.form['q']
    search_dict = movie.search(title)
    return render_template("moviereviews.html", type= "movie", search=title, dict= search_dict)

@app.route('/fullbook', methods = ['post','get'])
def fullbook():
    bookname = None
    review = None
    if 'bookID' in request.form:
        review = book.getReview(request.form['bookID'])
    if 'bookname' in request.form:
        bookname = request.form['bookname']
    dic = book.search(title)
    return render_template("fullbook.html", title = bookname, dict = dic, review = review)


if __name__ == '__main__':
    app.run(debug=True)
