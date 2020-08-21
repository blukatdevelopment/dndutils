#!/usr/bin/python3

import sys
sys.path.append('../')
from dice import roll_die
from tkinter import *
from discord_chat import send_message_to_discord

FEET_PER_INCREMENT = 5

def artillery_inaccuracy():
  direction = calculate_direction()
  distance = calculate_distance()
  description = "Shot strayed to the {} by {} feet.".format(direction, distance)
  return { "distance": distance, "direction": direction, "description": description }

def calculate_direction():
  dir_map = {
    1: "NorthWest",
    2: "North",
    3: "NorthEast",
    4: "West",
    5: "East",
    6: "SouthEast",
    7: "South",
    8: "SouthWest"
  }
  roll = roll_die(8)['result']
  return dir_map[roll]

def calculate_distance():
  roll = roll_die(8)['result']
  return roll * 5