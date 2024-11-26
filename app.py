from flask import Flask

app = Flask(__name__)



@app.route('/')
def hello():
    return '<h1>Caesar Cipher</h1>'

@app.route('/about/')
def about():
    return '<h3>This is a Caesar Cipher Web App.</h3>'


