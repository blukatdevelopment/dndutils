#!/usr/bin/python3

import sys
sys.path.append('../')
from dice import roll_die
from tkinter import *
from discord_chat import send_message_to_discord

FEET_PER_INCREMENT = 5
ENABLE_DISCORD = True

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

def business_logic_demo():
  for i in range(10):
    inaccuracy = artillery_inaccuracy()
    print(inaccuracy["description"])

class ArtilleryGUI:
  def __init__(self, master):
    self.master = master
    self.init_controls(master)

  def init_controls(self, master):
    self.label = Label(master, text='               ')
    self.label.grid(row = 0 , column = 0)
    self.button = Button(master, text="Roll innaccuracy", command = self.display_innacuracy)
    self.button.grid(row=1, column = 0)

  def display_innacuracy(self):
    inaccuracy = artillery_inaccuracy()
    self.label['text'] = inaccuracy['description']
    if(ENABLE_DISCORD):
      send_message_to_discord(inaccuracy['description'])

def main():
  root = Tk()
  root.title('Artillery inaccuracy')
  gui = ArtilleryGUI(root)
  root.mainloop()