#!/usr/bin/python3

from dice import roll_die
import datetime
import json
import os

BUSINESS_FILE_NAME='./business/businesses.json'
RECORD_PROGRESS=False


def timestamp():
  return '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())

def mkdir(path):
  try:
    os.mkdir(path)
  except OSError:
      print ("Creation of the directory %s failed" % path)
  else:
      print ("Successfully created the directory %s " % path)

def read_businesses():
  with open(BUSINESS_FILE_NAME) as json_file:
    businesses = json.load(json_file)
    return businesses

def update_businesses(businesses):
  with open(BUSINESS_FILE_NAME, 'w') as json_file:
    raw = json.dumps(businesses, indent=4)
    json_file.write(raw)

def record_progress(progress):
  if RECORD_PROGRESS is False:
    return timestamp()
  time = timestamp()
  path = './business/progress/{}.json'.format(time)
  raw = json.dumps(progress, indent=4)
  with open(path, 'w') as json_file:
    json_file.write(raw)
    return time

def get_individual_progress(business):
  outcome = get_outcome(business)
  income = outcome['income']

  updated = { 'reinvestment': business['reinvestment'] 'name': business['name'], 'value': income + business['value']}
  progress = { 'initial': business, 'outcome': outcome, 'updated': updated }
  return progress

def get_outcome(value):
  if value < 1:
    return { "income": 0, 'roll': -1, "description": "Closed" }
  roll = roll_die(100)['result']

  if roll < 2:
    percentage = float( 100 + roll_die(100)['result']) / float(100)
    income = float(value) * -float(percentage)
    return { "income": income, roll: roll, "description": "Disaster"}
  elif roll < 11:
    income = float(value) * -0.33
    return { "income": income, roll: roll, "description": "Decline"}
  elif roll < 21:
    income = float(value) * -0.15
    return { "income": income, roll: roll, "description": "Very Slow"}
  elif roll < 41:
    return { "income": 0, roll: roll, "description": "Slow"}
  elif roll < 81:
    income = float(value) * 0.15
    return { "income": income, roll: roll, "description": "Normal"}
  elif roll < 91:
    income = float(value) * 0.33
    return { "income": income, roll: roll, "description": "Great"}
  elif roll < 100:
    income = float(value) * 0.5
    return { "income": income, roll: roll, "description": "Spectacular"}
  else:
    percentage = float(100 + roll_die(100)['result']) / float(100)
    income = float(value) * percentage
    return { "income": income, roll: roll, "description": "Booming"}

def run_update():
  businesses = read_businesses()
  progress = { "individual": [], "total_initial_value": 0, "total_updated_value": 0, "total_income": 0 }
  updated = []
  for business in businesses:
    individual = get_individual_progress(business)
    progress['individual'].append(individual)
    progress['total_initial_value'] += individual['initial']['value']
    progress['total_updated_value'] += individual['updated']['value']
    updated.append(individual['updated'])
  progress['timestamp'] = record_progress(progress)
  update_businesses(updated)
  return progress

def demo():
  records = []
  for i in range(500):
    progress = run_update()
    timestamp = progress['timestamp']
    delta = progress["total_updated_value"] - progress["total_initial_value"]
    if(delta > 0):
      delta = "+" + str(delta)
    value = progress["total_updated_value"]
    print("{},{},{},{}".format(i, timestamp, delta, value))

demo()