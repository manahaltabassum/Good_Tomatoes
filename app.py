from flask import Flask, render_template, request, session, redirect, url_for, flash
import book, movie

app = Flask(__name__)

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
    title = request.form['q']
    return render_template("searched.html", title=title)

@app.route('/searchedbook', methods = ['post','get'])
def searchedbook():
    bookname = request.form['q']
    print bookname
    search_dict = book.search(bookname)
    return render_template("reviews.html", type="book", search=bookname, dict = search_dict)

@app.route('/searchedmovie', methods = ['post','get'])
def searchedmovie():
    moviename = request.form['q']
    print moviename
    search_dict = movie.search(moviename)
    return render_template("reviews.html", type= "movie", search=moviename, dict= search_dict)



if __name__ == '__main__':
    app.run(debug=True)
