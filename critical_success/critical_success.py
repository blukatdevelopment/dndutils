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

def critical(category):
  roll = roll_result(20)
  result = ""
  if category == NATURAL:
    result = natural_critical(roll)
  elif category == RANGED:
    result = ranged_critical(roll)
  elif category == MAGIC:
    result = magic_critical(roll)
  elif category == MELEE:
    result = melee_critical(roll)
  else:
    return "Invalid critical category"

  ret = "{} critical {} In addition to double damage dice: {}".format(category, roll, result)

  return ret

def direction():
  return calculate_direction()

def natural_critical(roll):
  if roll == 1:
    return 'The target is frightened until the end of your next turn.'
  elif roll == 2:
    return 'The target must use all their movement to move away from you in a straight line.'
  elif roll < 11:
    return 'If the target is holding a weapon, you can steal it from them.'
  elif roll < 20:
    return 'The target goes prone. If the target is already prone, they instead take 1d6 bludgeoning damage.'
  else:
    return 'You gain an extra action this turn'

def ranged_critical(roll):
  damage = 0
  if roll == 1:
    return 'The target has disadvantage on all attack rolls until the end of your next turn.'
  elif roll == 2:
    damage = roll_dice(3, 6)["result"]
    return 'The target must succeed a DC 14 con save or fall into shock and take {} psychic damage'.format(str(damage))
  elif roll < 11:
    return 'The target drops their weapon.'
  elif roll < 20:
    return 'The target blinded for the next 10 minutes.'
  else:
    return 'You gain an extra action this turn'

def magic_critical(roll):
  if roll == 1:
    return 'If the target has resistance to this damage type, it loses it for 10 minutes. If not, it instead becomes vulnerable to this damage type for 10 minutes.'
  elif roll == 2:
    return 'One creature you choose within 5 feet of the target is also damaged by this spell.'
  elif roll < 11:
    hours = roll_dice(1, 4)
    return 'The enemy turns into a {} for {} hours, or until they take damage'.format(random_object(), str(hours))
  elif roll < 20:
    return wild_magic()
  else:
    return 'You gain an extra action this turn'

def random_object():
  objects = [
    'banana',
    'short sword',
    'potted plant',
    'cat',
    'miniature statue of themself',
    'jar of mayonaise',
    'can of peanut brittle that actually contains a springloaded snake toy',
    'comfortable sweater',
    'bar of premium dark chocolate',
    'purse'
  ]
  roll = roll_result(10)
  return objects[roll]

def melee_critical(roll):
  damage = 0
  if roll == 1:
    return 'Target must succeed DC 14 con save or go unconscious until they succeed a DC12 con save on the end of their turn.'
  elif roll == 2:
    damage = roll_dice(3, 6)["result"]
    return 'Target suffers internal trauma and takes {} bludgeoning damage.'.format(damage)
  elif roll < 11:
    return 'You can use your reaction to make a single melee attack against this creature.'
  elif roll < 20:
    return 'If the target is holding a weapon, you knock it onto the ground.'
  else:
    return 'You gain an extra action this turn'

def wild_magic():
  outcomes = {
    "1": "Shadowy tendrils lash around you. Each creature of your choice that you can see within 30 feet of you must succeed on a Constitution saving throw or take 1d12 necrotic damage. You also gain 1d12 temporary hit points.",
    "2": "You teleport up to 30 feet to an unoccupied space you can see.",
    "3": "An intangible spirit, which looks like a flumph or a pixie (your choice), appears within 5 feet of one creature of your choice that you can see within 30 feet of you. At the end of the current turn, the spirit explodes, and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 1d6 force damage.",
    "4": "Magic infuses one weapon of your choice that you are holding. Until the end of your next turn, the weapon's damage type changes to force, and it gains the light and thrown properties, with a normal range of 20 feet and a long range of 60 feet. If the weapon leaves your hand, the weapon reappears in your hand at the end of the current turn.",
    "5": "Whenever a creature hits you with an attack roll before your rage ends, that creature takes 1d6 force damage, as magic lashes out in retribution.",
    "6": "Until the end of your next turn, you are surrounded by multi colored, protective lights. You gain a +1 bonus to AC, and while within 10 feet of you, your allies gain the same bonus.",
    "7": "Flowers and vines temporarily grow around you. Until the end of your next turn, the ground within 15 feet of you is difficult terrain for your enemies.",
    "8": "A bolt of light shoots from your chest. Another creature of your choice that you can see within 30 feet of you must succeed on a Constitution saving throw or take 1d6 radiant damage and be blinded until the start of your next turn.",
  }
  roll = roll_result(8)
  return "You hit a ley line and trigger a wild magic surge {}: {}".format(str(roll), outcomes[str(roll)])


# Use this as a standalone script on the command line.
def main():
  if(len(sys.argv) == 2):
    arg = sys.argv[1]
    result = critical(arg.lower())
    print(result)
  else:
    print("usage: <category>")
