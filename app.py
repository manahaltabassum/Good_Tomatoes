from flask import Flask, render_template, request, session, redirect, url_for, flash
import book, movie

app = Flask(__name__)

@app.route('/')
def root ():
    return render_template ('welcome.html')

@app.route('/movie', methods = ['post','get'])
def moviepage():
    return render_template('movie.html');

@app.route('/book', methods = ['post','get'])
def bookpage():
    return render_template('book.html');


@app.route('/searchedbook', methods = ['post','get'])
def searchedbook():
    bookname = request.form['q']
    search_dict = book.search(bookname)
    results_dict = book.getResultsDict(search_dict)
    print results_dict
    #print "AAAAHHHHHHHHHHHHH    " + bookname
    return render_template("bookreviews.html", search=bookname)




if __name__ == '__main__':
    app.run(debug=True)
