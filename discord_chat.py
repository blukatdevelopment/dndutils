#!/usr/bin/python3

'''
  This hooks into discord to send strings in the form of messages.
'''

import requests
import json
from main import base_path

SETTINGS = base_path() + "settings.json"
DISCORD_URI=None


def get_discord_uri():
  if DISCORD_URI is not None:
    return DISCORD_URI

  with open(SETTINGS) as json_file:
    settings = json.load(json_file)
    
    return settings["discord_uri"]

def send_message_to_discord(message, print_output=False):
  if(print_output):
    print("Sending message to discord: {}".format(message))
  
  data = {
    "content": message
  }
  response = requests.post(get_discord_uri(), json=data)
  if(print_output):
    print("Status code from the call was {}".format(response.status_code))