#!/usr/bin/python3

import sys
sys.path.append('../')

from dice import *
from business import Business
import datetime
import json

BUSINESS_FILE_NAME='./businesses.json'

HANDLE_IN_MEMORY = True
WEEKS_PER_SIMULATION = 10
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

  with open(BUSINESS_FILE_NAME, 'w') as json_file:
    raw = json.dumps(businesses, indent=4)
    json_file.write(raw)

def run_update():
  businesses = get_businesses()
  updated = []
  for business in businesses:
    business.update()
    updated.append(business)
  save_businesses(updated)

def market_analysis():
  records = []
  for i in range(WEEKS_PER_SIMULATION):
    run_update()
  for business in get_businesses():
    print(json.dumps(business.__dict__, indent=4))

def timestamp():
  return '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())

market_analysis()