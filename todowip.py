from telethon import TelegramClient
#from telethon.errors.rpc_errors_401 import SessionPasswordNeededError
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types.messages import Messages
from http.server import BaseHTTPRequestHandler, HTTPServer
import tornado.ioloop
import tornado.web
import pprint

import json

# (1) Use your own values here (https://core.telegram.org/api/obtaining_api_id)
api_id = 000000
api_hash = '00000000000000000000000'

phone = '+000000000000'
username = 'theone'

project_id = '2176677882'

# (2) Create the client and connect
client = TelegramClient(username, api_id, api_hash)
client.connect()

# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))

# Helper function to send messages to wipchat telegram group 

# Define web server 'controller'
class MyDumpHandler(tornado.web.RequestHandler):
    pprint.pprint('HTTP Listener initialized:')
    pprint.pprint('##########################')
    pprint.pprint('#######---W I P-----######')
    pprint.pprint('##########################')
    
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        if data['event_name'] == "item:added" and data["event_data"]["project_id"] == project_id:
            message = "/todo " + data["event_data"]["content"]
            # client.send_message('wipbots', message)
        if data['event_name'] == "item:completed" and data["event_data"]["project_id"] == project_id:
            message = "/done " + data["event_data"]["content"]
            client.send_message('wipchat', message)
        pprint.pprint(data['event_name'])

# Run server loop
if __name__ == "__main__":
    tornado.web.Application([(r"/.*", MyDumpHandler),]).listen(5500)
    tornado.ioloop.IOLoop.instance().start()




