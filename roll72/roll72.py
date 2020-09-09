# Roll ability scores for a character
import random

MIN_SCORE = 72

# Returns a dict with accepted rolls, total, and minimum roll
def roll_4d6_drop_lowest():
  result = {}
  result["rolls"] = []
  for i in range(4):
    roll = random.randint(1, 6)
    result["rolls"].append(roll)
  
  result["minimum"] = min(result["rolls"])
  result["rolls"].remove(min(result["rolls"]))
  result["total"] = sum(result["rolls"])
  return result

def roll_ability_scores():
  while True:
    sum = 0
    results = []
    for i in range(6):
      result = roll_4d6_drop_lowest()
      results.append(result)
      sum += result["total"]
    if sum >= MIN_SCORE:
      return results
  return None

def format_result(result):
  out = str(result["rolls"])
  out += "(Dropped {})".format(result["minimum"])
  out += str(result["total"])
  return out

def format_results(results):
  out = ""
  for result in results:
    out += format_result(result) + "\n"
  return out


def main():
  results = roll_ability_scores()
  if results is None:
    print("Could not roll higher than {} in {} attempts".format(MIN_SCORE, MAX_ATTEMPTS))
  else:
    print(format_results(results))

#uncomment this to run locally
#main()
