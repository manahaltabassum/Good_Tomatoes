from flask import Flask, render_template, redirect
import book, movie

app = Flask(__name__)

@app.route('/')
def root ():
    return render_template ('welcome.html')

@app.route('/movie')
def movie():
    return render_template('movie.html');

@app.route('/book')
def book():
    return render_template('book.html');


@app.route('/searchedbook')
def searchedbook():
    search = request.form['']
    return render_template("bookreviews.html", search = search)




if __name__ == '__main__':
    app.run(debug=True)
