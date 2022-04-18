# -*- coding: utf-8 -*-
"""
    :author: Mykola Kobzar
    :repo: https://github.com/n-g-s/simple-503.git
"""

from flask import Flask, Response, jsonify, make_response

app = Flask(__name__)
MESSAGE = "Return HTTP Code: 503"


@app.route('/')
def index():
    keda_metric.inc()
    return Response(MESSAGE, mimetype="text/plain",status=503)

@app.route('/api')
def api():
    keda_metric.inc()
    return Response(MESSAGE, mimetype="text/plain",status=503)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
