#!/usr/bin/python3

import sys
sys.path.append('../')
sys.path.append('../artillery/')
sys.path.append('./artillery/')
from discord_chat import send_message_to_discord
from dice import roll_dice, roll_result
from artillery import calculate_direction

# Categories
NATURAL="natural"
RANGED="ranged"
MAGIC="magic"
MELEE="melee"

def fumble(category):
  roll = roll_result(20)
  result = ""
  if category == NATURAL:
    result = natural_fumble(roll)
  elif category == RANGED:
    result = ranged_fumble(roll)
  elif category == MAGIC:
    result = magic_fumble(roll)
  elif category == MELEE:
    result = melee_fumble(roll)
  else:
    return "Invalid fumble category"

  ret = "Critical {} fumble {}: {}".format(category, roll, result)

  return ret

def direction():
  return calculate_direction()

def natural_fumble(roll):
  if roll == 1:
    return "The attack is disabled until you complete a short or long rest, and you take {} slashing damage".format(roll_dice(2, 6)["result"])
  elif roll == 2:
    return "This attack is disabled until you complete a short or long rest"
  elif roll < 11:
    return "Minor sprain: take {} bludgeoning damage the next time you use this attack".format(roll_dice(2, 6)["result"])
  elif roll < 20:
    return "Your attack hits the first creature {} of you within range.".format(direction())
  else:
    return "You got lucky"

def ranged_fumble(roll):
  if roll == 1:
    damage = roll_dice(2, 6)["result"]
    return "Weapon is broken, dealing {} bludgeoning damage".format(damage)
  elif roll == 2:
    return "Weapon is broken"
  elif roll < 11:
    return "Weapon malfunction: fix with an action."
  elif roll < 20:
    return "Your attack hits the first creature {} of you within range.".format(direction())
  else:
    return "You got lucky"

def magic_fumble(roll):
  if roll == 1:
    return "Roll 1d100 on the wild magic chart."
  elif roll == 2:
    return "Your spell focus turns into a non-magical banana"
  elif roll < 11:
    return "Your hands go numb for this turn and you drop anything you are carrying."
  elif roll < 20:
    return "Your attack hits the first creature {} of you within range.".format(direction())
  else:
    return "You got lucky"

def melee_fumble(roll):
  if roll == 1:
    damage = roll_dice(2, 6)["result"]
    return "The weapon breaks and you take {} slashing damage.".format(damage)
  elif roll == 2:
    return "The weapon breaks."
  elif roll < 11:
    return "Your attack hits you. Receive half damage."
  elif roll < 20:
    return "Your attack hits the first creature {} of you within range.".format(direction())
  else:
    return "You got lucky"

# Use this as a standalone script on the command line.
def main():
  if(len(sys.argv) == 2):
    arg = sys.argv[1]
    result = fumble(arg.lower())
    print(result)
  else:
    print("usage: <category>")
