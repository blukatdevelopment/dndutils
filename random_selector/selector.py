#!/usr/bin/python3


# This script helps when more people sign up for a session than there are slots.
import sys
sys.path.append('../')
from dice import roll_result
from discord_chat import send_message_to_discord

def get_interested_parties():
  i = 2
  interested_parties = []
  while i < len(sys.argv):
    interested_parties.append(sys.argv[i])
    i += 1
  return interested_parties

def select_x(x, options):
  selected = []
  for i in range(x):
    selection_made = False
    while not selection_made:
      roll = roll_result(len(options)-1)
      selected_option = options[roll]
      if selected_option not in selected:
        selected.append(selected_option)
        selection_made = True
  return selected

def main():
  if len(sys.argv) < 3:
    print("Usage: selector <number of slots> <player names>")
  available_slots = int(sys.argv[1])
  interested_players = get_interested_parties()
  selected_players = select_x(available_slots, interested_players)
  output = "Selecting from {}\n".format(interested_players)
  for i in range(len(selected_players)):
    output += "Chose player {}\n".format(selected_players[i])
  print(output)
  send_message_to_discord(output)
main()