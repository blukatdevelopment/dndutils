#!/usr/bin/python3

import sys
sys.path.append('../')
from dice import roll_mass_result

def main():
  if(len(sys.argv) == 4):
    num_rolls = int(sys.argv[1])
    modifier = int(sys.argv[2])
    dc = int(sys.argv[3])
    result = roll_mass_result(num_rolls, modifier, dc, True, False, True)
  else:
    print("Usage: <Number of rolls> <modifier> <DC>")


main()