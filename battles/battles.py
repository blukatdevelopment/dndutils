#!/usr/bin/python3

import sys
sys.path.append('../')
from dice import roll_die

def simulation(attacker, defender):
  print("Begin battle. Attacker: {} Defender: {}".format(attacker.strength, defender.strength))
  while attacker.strength > 0 and defender.strength > 0:
    attacker.strength -= defender.attack()
    defender.strength -= defender.attack()
    print("Attacker: {}, Defender:{}".format(attacker.strength, defender.strength))
  if(attacker.strength > 0):
    print("Attacker won with {} strength".format(attacker.strength))
  else:
    print("Defender won with {} strength".format(defender.strength))

class Army:
  def __init__(self, strength=100):
    self.strength = strength

  def attack(self):
    attack_power = int(self.strength/2)
    roll = roll_die(max(attack_power, 1))['result']
    return min(roll, self.strength)

def main():

  if(len(sys.argv) == 3):
    simulation(Army(int(sys.argv[1])), Army(int(sys.argv[2])))
  else:
    simulation(Army(), Army())

main()