#!/usr/bin/python3

# This is a quick polygonal dice library
import random
random.seed()

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
