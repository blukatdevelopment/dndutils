#!/usr/bin/python3

import sys, fileinput
sys.path.append('../')
from dice import roll_dice, roll_result
from main import base_path

POSITIVE = "positive"
NEUTRAL = "neutral"
HARMFUL = "harmful"
HOSTILE = "hostile"

def load_table(category):
  file_path = base_path() + "encounters/" + category + ".txt"
  lines = []

  with fileinput.input(files=(file_path)) as f:
    for line in f:
      lines.append(line)
  return lines

def get_category():
  category_dict = {
    "1": HOSTILE,
    "2": HARMFUL,
    "3": NEUTRAL,
    "4": NEUTRAL,
    "5": POSITIVE,
    "6": POSITIVE
  }
  result = roll_result(6)
  return category_dict[str(result)]

def get_table(category):
  if category == POSITIVE:
    return positive_table
  if category == NEUTRAL:
    return neutral_table
  if category == HARMFUL:
    return harmful_table
  if category == HOSTILE:
    return hostile_table

def get_encounter():
  category = get_category()
  table = get_table(category)
  roll = roll_result(len(table))-1
  encounter = table[roll]
  return "{} {}: {}".format(category, roll, encounter)

hostile_table = load_table(HOSTILE)
harmful_table = load_table(HARMFUL)
neutral_table = load_table(NEUTRAL)
positive_table = load_table(POSITIVE)