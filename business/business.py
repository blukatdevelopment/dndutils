#!/usr/bin/python3

from dice import roll_die
import datetime

# Outcomes
DISASTER = "Disaster"
DECLINE = "Decline"
VERY_SLOW = "Very Slow"
SLOW = "Slow"
NORMAL = "Normal"
GREAT = "Great"
SPECTACULAR = "Spectacular"
BOOMING = "Booming"

class Business:
  def __init__(self, name=None, value=None, savings=None, owner=None, history_log=None, reinvestment_rate=None, json_obj=None, save_history=False):
    print("json{}".format(json_obj))
    if json_obj is not None:
      name = json_obj['name']
      value = json_obj['value']
      savings = json_obj['savings']
      owner = json_obj['owner']
      reinvestment_rate = json_obj['reinvestment_rate']
      if 'history_log' in json_obj:
        history_log = json_obj['history_log']

    self.name = name
    self.owner = owner
    self.value = value
    self.savings = savings
    self.reinvestment_rate = reinvestment_rate
    self.save_history = save_history
    if history_log is None:
      history_log = []
    self.history_log = history_log

  def update(self):
    income = self.roll_income()

    log_record = {}
    log_record["name"] = self.name
    log_record["owner"] = self.owner
    log_record["start_value"] = self.value
    log_record["start_savings"] = self.savings

    self.handle_income(income)

    log_record["end_value"] = self.value
    log_record["end_savings"] = self.savings
    log_record["timestamp"] = '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())

    if self.save_history:
      self.history_log.append(log_record)

  def handle_income(self, income):
    if income == 0:
      return
    elif income > 0:
      self.reinvest(income)
    else:
      self.pay_debt(-income)

  def reinvest(self, income):
    invest_amount = float(income) * float(self.reinvestment_rate)
    save_amount = float(income) - float(invest_amount)
    self.value += invest_amount
    self.savings += save_amount

  def pay_debt(self, debt):
    if self.savings >= debt:
      self.savings -= debt
      return

    debt -= self.savings
    self.savings = 0

    liquid_value = float(self.value) / float(2)

    if liquid_value > debt:
      liquid_value -= debt
      self.value = liquid_value * float(2)
      return

    self.value = liquid_value - debt

  def roll_income(self):
    if self.value < 1:
      return 0
    outcome = self.map_roll_to_outcome(roll_die(100)['result'])
    return self.determine_income(outcome, self.value)

  def map_roll_to_outcome(self, roll):
    if roll < 2:
      return DISASTER
    elif roll < 11:
      return DECLINE
    elif roll < 21:
      return VERY_SLOW
    elif roll < 41:
      return SLOW
    elif roll < 81:
      return NORMAL
    elif roll < 91:
      return GREAT
    elif roll < 100:
      return SPECTACULAR
    else:
      return BOOMING

  def determine_income(self, outcome, value):
    percentage_map = {}
    percentage_map[DISASTER] = -1.0
    percentage_map[DECLINE] = -0.33
    percentage_map[VERY_SLOW] = -0.15
    percentage_map[SLOW] = 0
    percentage_map[NORMAL] = 0.15
    percentage_map[GREAT] = 0.33
    percentage_map[SPECTACULAR] = 0.5
    percentage_map[BOOMING] = 1.0

    income = 0

    if outcome in percentage_map:
      income = float(value) * float(percentage_map[outcome])

    if outcome == DISASTER:
      bonus_percentage = float(roll_die(100)['result']) / float(100)
      income += float(value) * float(bonus_percentage)
    elif outcome == BOOMING:
      bonus_percentage = float(roll_die(100)['result']) / float(100)
      income += float(value) * float(bonus_percentage)
    return income
