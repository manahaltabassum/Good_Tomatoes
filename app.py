from flask import Flask, render_template, request, session, redirect, url_for, flash
import book, movie

app = Flask(__name__)

@app.route('/')
def root ():
    return render_template ('welcome.html')

@app.route('/searched', methods = ['post','get'])
def searched():
    title = request.form['q']
    return render_template("searched.html", title=title)


@app.route('/searchedbook', methods = ['post','get'])
def searchedbook():
    bookname = request.form['q']
    search_dict = book.search(bookname)
    #results_dict = book.getResultsDict(search_dict)
    #print search_dict
    #print "AAAAHHHHHHHHHHHHH    " + bookname
    return render_template("reviews.html", type="book", search=bookname, dict = search_dict)

#@app.route('/searchedmovie', methods = ['post','get'])
#def searchedmovie():
    #moviename = request.form['q']
    #search_dict = movie.search(moviename)
    #return render_template("reviews.html", type= "movie", search=moviename, dict= search_dict)



if __name__ == '__main__':
    app.run(debug=True)
