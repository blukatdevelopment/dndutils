#!/usr/bin/python3


# This script helps when more people sign up for a session than there are slots.
import sys
sys.path.append('../')
from dice import roll_result
from discord_chat import send_message_to_discord
AVAILABLE_SLOTS=4
INTERESTED_PARTIES=[
  'Jabber',
  'Axel',
  'Pigshanks',
  'Steel',
  'Bruce'
]


def main():
  chosen_parties = []
  output = "Selecting from {}\n".format(INTERESTED_PARTIES)
  for i in range(AVAILABLE_SLOTS):
    found = False
    while not found:
      choice = roll_result(len(INTERESTED_PARTIES))
      chosen_party = INTERESTED_PARTIES[int(choice)]
      if chosen_party not in chosen_parties:
        chosen_parties.append(chosen_party)
        output += "Chose {}\n".format(chosen_party)
        found = True
  print(output)
  send_message_to_discord(output)
main()