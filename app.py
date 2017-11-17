from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def root:
    return 'Welcome'

if __name__ == '__main__':
    app.run(debug=True)
