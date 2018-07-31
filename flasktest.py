#/usr/bin/env
#coding = utf-8
from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hell'

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()


#test1
