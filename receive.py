#! /usr/bin/python

from flask import Flask, request, abort
import requests
from ciscosparkapi import CiscoSparkAPI, Webhook


#grab the at from a local at.txt file instead of global variable
fat=open ("at.txt","r+")
at=fat.readline().rstrip()
fat.close


app=Flask(__name__)


@app.route('/gerard', methods=['POST'])
def gerard():
    if request.method == 'POST':
        webhook_obj = Webhook(request.json)
        print(request.json)
        return '', 200
        message = api.messages.get(webhook_obj.data.id)
        me = api.people.me()
        
        if message.personId == me.id: 
           print("bot spoke")
           return 'Ok'
        else:
           roomid = webhook_obj.data.roomId
           message_text = message.text
           response_message = api.messages.create(roomid, text=message_text)
           print (response_message)
    else:
        abort(400)
    return 'Ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

