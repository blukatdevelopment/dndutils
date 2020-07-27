#!/usr/bin/python3

import sys
sys.path.append('../')
from dice import roll_mass
from discord_chat import send_message_to_discord

def format_message(result):
  message = "Performing mass roll:\n"
  for row in result["outcomes"]:
    message += "{}\n".format(row)
  message += "{}\n".format(result["description"])
  return message

def main():
  if(len(sys.argv) == 4):
    num_rolls = int(sys.argv[1])
    modifier = int(sys.argv[2])
    dc = int(sys.argv[3])
    result = roll_mass(num_rolls, modifier, dc, True, False)
    message = format_message(result)
    print(message)
    send_message_to_discord(message)
  else:
    print("Usage: <Number of rolls> <modifier> <DC>")


main()