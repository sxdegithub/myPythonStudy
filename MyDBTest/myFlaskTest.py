# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
from flask import Flask
# pip3 install  pyopenssl
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
