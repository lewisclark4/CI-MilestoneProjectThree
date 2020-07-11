import os
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Foodology'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)