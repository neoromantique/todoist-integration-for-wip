from telethon import TelegramClient
#from telethon.errors.rpc_errors_401 import SessionPasswordNeededError
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types.messages import Messages
import tornado.ioloop
import tornado.web
import pprint
import json
from credentials import * 


# Create the client and connect
client = TelegramClient(username, api_id, api_hash)
client.connect()

# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))

# Define web server 'controller'
class myRequestHandler(tornado.web.RequestHandler):
    pprint.pprint('HTTP Listener initialized:')
    
    def post(self):
        data = tornado.escape.json_decode(self.request.body)

        if data['event_name'] == "item:added" and data["event_data"]["project_id"] == project_id:
            message = "/todo " + data["event_data"]["content"]
            # client.send_message('wipbots', message)
        if data['event_name'] == "item:completed" and data["event_data"]["project_id"] == project_id:
            message = "/done " + data["event_data"]["content"]
            client.send_message('wipchat', message)

        pprint.pprint(data['event_name'] + " in project " + str(data["event_data"]["project_id"]) + " is not handled") 

# Run server loop
if __name__ == "__main__":
    tornado.web.Application([(r"/.*", myRequestHandler),]).listen(5500)
    tornado.ioloop.IOLoop.instance().start()
