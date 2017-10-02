#!flask/bin/python
from flask import Flask
from HabrParser import parser

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/NewNews')
def sendMessage():
    text = parser.print_actual_test_article()
    return text;

if __name__ == '__main__':
    app.run(debug=True)