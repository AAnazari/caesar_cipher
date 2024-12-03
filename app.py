from flask import Flask, render_template, request

# Importing the Cipher function to encrypt the message
from caesar_cipher.cipher import caesar

# Importing the validate_shift function from the utils file
from caesar_cipher.utils import validate_shift

app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        offset = int(request.form["shift"])

        try:
            # Validate the shift value
            offset = validate_shift(offset)

            result = caesar(message, offset)
            return render_template("index.html", result=result)

        except ValueError as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")
'''
def hello():
    return '<h1>Caesar Cipher</h1>'
'''

@app.route('/about/')
def about():
    return '<h3>This is a Caesar Cipher Web App.</h3>'


