#! /usr/bin/python

from flask import Flask, request, abort
import requests
from ciscosparkapi import CiscoSparkAPI, Webhook

app=Flask(__name__)


@app.route('/gerard', methods=['POST'])
def gerard():
    if request.method == 'POST':
        webhook_obj = Webhook(request.json)
        print(request.json)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4040)

