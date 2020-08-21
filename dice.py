#!/usr/bin/python3

# This is a quick polygonal dice library
import random
random.seed()

DISCORD_ENABLED=True


def discord_enabled():
    return DISCORD_ENABLED

def roll_result(die_size, modifier = 0, advantage = False, disadvantage = False):
    return roll_die(die_size, modifier, advantage, disadvantage)['result']

def roll_mass(num_rolls, modifier, dc, advantage = False, disadvantage = False, print_results=False):
  successes = 0
  outcomes = []

  for i in range(num_rolls):
    roll = roll_die(20, modifier, True)
    result = roll["result"]

    if(result >= dc):
      successes += 1
      outcomes.append("{} [success]".format(roll["description"]))
    else:
      outcomes.append("{} [fail]".format(roll["description"]))
  roll_type = "normal"
  if(advantage):
    roll_type = "advantage"
  if(disadvantage):
    roll_type = "disdvantage"

  description = "Performed {} {} rolls with {} VS DC of {}. {} successes".format(num_rolls, roll_type, modifier, dc, successes)

  return {
    "successes": successes,
    "outcomes": outcomes,
    "description": description
  }

def roll_dice(quantity, size, modifier=0):
    rolls = []
    result = modifier
    for i in range(quantity):
        roll = roll_die(size)
        rolls.append(roll)
        result += roll["result"]

    return {
        "result": result,
        "rolls": rolls
    }

def roll_die(die_size, modifier = 0, advantage = False, disadvantage = False):
    first = random.randint(1, die_size)
    second = random.randint(1, die_size)
    
    result = first

    if advantage and not disadvantage:
        result = max(first, second)
    if not advantage and disadvantage:
        result = min(first, second)
    result = result + modifier

    outcome = {}
    outcome['die_name'] = 'D' + str(die_size)
    outcome['die_size'] = die_size
    outcome['first'] = first
    outcome['second'] = second
    outcome['modifier'] = modifier
    outcome['advantage'] = advantage
    outcome['disadvantage'] = disadvantage
    outcome['result'] = result
    outcome['description'] = dice_roll_outcome_description(outcome)
    return outcome

def dice_roll_outcome_description(outcome):
    ret = ""
    mod = ""
    
    if outcome['modifier'] > 0:
        mod = "+" + str(outcome['modifier'])
    elif outcome['modifier'] < 0:
        mod = "-" + str(outcome['modifier'])

    if outcome['advantage']:
        ret = "rolled {}{} with advantage [{},{}]".format(str(outcome['die_name']), mod, str(outcome['first']), str(outcome['second']))
    elif outcome['disadvantage']:
        ret = "rolled a {}{} with disadvantage [{},{}]".format(str(outcome['die_name']), mod, str(outcome['first']), str(outcome['second']))
    else:
        ret = "rolled a {}{}".format(str(outcome['die_name']), mod)
    ret += "and got {}".format(str(outcome['result'])) 
    return ret

def demo_roll_dice():
    args = [
        (20, 0, False, False),
        (20, 5, False, True),
        (20, 5, True, False),
        (20, 5, True, True)
    ]
    for row in args:
        outcome = roll_die(row[0], row[1], row[2], row[3])
        print(outcome['description'])


class Die:
    def __init__(self, die_size, die_count = 1):
        self.die_size = die_size
        self.die_count = die_count
