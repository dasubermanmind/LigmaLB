import os

from flask import Flask


app = Flask(__name__)

env = os.environ['APP']

@app.route('/')
def default():
    return f'This is the {env} app'

if __name__ == '__main__':
    app.run(host='0.0.0.0')