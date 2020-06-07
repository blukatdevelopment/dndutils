#!/usr/bin/python3

import sys
sys.path.append('../')

from dice import *
from business import Business
import json
import datetime

BUSINESS_FILE_NAME='./businesses.json'

HANDLE_IN_MEMORY = False
WEEKS_PER_SIMULATION = 50
in_memory_cache = None

def get_businesses():
  if HANDLE_IN_MEMORY and in_memory_cache is not None:
    return in_memory_cache

  with open(BUSINESS_FILE_NAME) as json_file:
    businesses_raw = json.load(json_file)
    businesses = []
    for business in businesses_raw:
      businesses.append(Business(json_obj = business, save_history=True))
    return businesses

def save_businesses(businesses):
  global in_memory_cache
  if HANDLE_IN_MEMORY:
    in_memory_cache = businesses
    return

  serialized = []
  logs = []
  for business in businesses:
    logs = logs + business.history_log
    business.history_log = []
    serialized.append(business.__dict__)
  
  logs_file = './logs/{:%Y%m%d%H%M%S_%f}.json'.format(datetime.datetime.now())

  with open(BUSINESS_FILE_NAME, 'w') as json_file:
    raw = json.dumps(serialized, indent=4)
    json_file.write(raw)

  with open(logs_file, 'w') as json_file:
    raw = json.dumps(logs, indent=4)
    json_file.write(raw)


def run_update():
  businesses = get_businesses()
  for business in businesses:
    business.update()
  save_businesses(businesses)

def market_analysis():
  records = []
  for i in range(WEEKS_PER_SIMULATION):
    run_update()
  for business in get_businesses():
    print(json.dumps(business.__dict__, indent=4))

market_analysis()