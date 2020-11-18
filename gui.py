#!/usr/bin/python3
import sys
sys.path.append('./critical_fumble')
sys.path.append('./critical_success')
sys.path.append('./artillery')
from artillery import artillery_inaccuracy
from critical_fumble import fumble
from critical_success import critical
from discord_chat import send_message_to_discord
from dice import *
from tkinter import *


class DmGUI:
  def __init__(self, master):
    self.master = master
    self.init_controls()

  def init_controls(self):
    
    CritFumbleGUI(self.master)
    ArtilleryGUI(self.master)
    MassRoller(self.master)

class CritFumbleGUI:
  def __init__(self, master):
    self.master = master
    self.init_controls(master)

  def init_controls(self, master):
    self.label = Label(master, text='               ')
    self.label.grid(row = 1 , column = 4)
    self.melee_fumble = Button(master, text="Nat 1 Melee", command = self.melee_fumble)
    self.melee_fumble.grid(row=1, column = 0)
    self.ranged_fumble = Button(master, text="Nat 1 Ranged", command = self.ranged_fumble)
    self.ranged_fumble.grid(row=1, column = 1)
    self.natural_fumble = Button(master, text="Nat 1 Natural", command = self.natural_fumble)
    self.natural_fumble.grid(row=1, column = 2)
    self.magic_fumble = Button(master, text="Nat 1 Magic", command = self.magic_fumble)
    self.magic_fumble.grid(row=1, column = 3)

    self.melee_crit = Button(master, text="Nat 20 Melee", command = self.melee_crit)
    self.melee_crit.grid(row=2, column = 0)
    self.ranged_crit = Button(master, text="Nat 20 Ranged", command = self.ranged_crit)
    self.ranged_crit.grid(row=2, column = 1)
    self.natural_crit = Button(master, text="Nat 20 Natural", command = self.natural_crit)
    self.natural_crit.grid(row=2, column = 2)
    self.magic_crit = Button(master, text="Nat 20 Magic", command = self.magic_crit)
    self.magic_crit.grid(row=2, column = 3)

  def melee_fumble(self):
    text = fumble("melee")
    self.label['text'] = text
    send_message_to_discord(text)

  def ranged_fumble(self):
    text = fumble("ranged")
    self.label['text'] = text
    send_message_to_discord(text)

  def natural_fumble(self):
    text = fumble("natural")
    self.label['text'] = text
    send_message_to_discord(text)

  def magic_fumble(self):
    text = fumble("magic")
    self.label['text'] = text
    send_message_to_discord(text)

  def melee_crit(self):
    text = critical("melee")
    self.label['text'] = text
    send_message_to_discord(text)

  def ranged_crit(self):
    text = critical("ranged")
    self.label['text'] = text
    send_message_to_discord(text)

  def natural_crit(self):
    text = critical("natural")
    self.label['text'] = text
    send_message_to_discord(text)

  def magic_crit(self):
    text = critical("magic")
    self.label['text'] = text
    send_message_to_discord(text)

class ArtilleryGUI:
  def __init__(self, master):
    self.master = master
    self.init_controls(master)

  def init_controls(self, master):
    self.label = Label(master, text='               ')
    self.label.grid(row = 3 , column = 4)
    self.button = Button(master, text="Roll innaccuracy", command = self.display_innacuracy)
    self.button.grid(row=3, column = 0)

  def display_innacuracy(self):
    inaccuracy = artillery_inaccuracy()
    self.label['text'] = inaccuracy['description']
    send_message_to_discord(inaccuracy['description'])

class MassRoller:
  def __init__(self, master):
    self.mod_label = Label(master, text="Mod")
    self.mod_label.grid(row=4, column=0)
    self.mod = Text(master, height=1, width=2)
    self.mod.grid(row=4, column=1)

    self.ac_label = Label(master, text="AC/DC")
    self.ac_label.grid(row=4, column=2)
    self.ac = Text(master, height=1, width=2)
    self.ac.grid(row=4, column=3)

    self.quantity_label = Label(master, text="#")
    self.quantity_label.grid(row=4, column=4)
    self.quantity = Text(master, height=1, width=2)
    self.quantity.grid(row=4, column=5)

    self.button = Button(master, text="Advantage", command = self.advantage)
    self.button.grid(row=4, column=6)

    self.button = Button(master, text="Disadvantage", command = self.disadvantage)
    self.button.grid(row=4, column=7)

    self.button = Button(master, text="Normal", command = self.normal)
    self.button.grid(row=4, column=8)

    self.output = Label(master, text="")
    self.output.grid(row=4, column=9)

  def get_args(self):
    return {
      "mod": self.mod.get("1.0", END),
      "ac": self.ac.get("1.0", END),
      "quantity": self.quantity.get("1.0", END),
    }

  def advantage(self):
    args = self.get_args()
    text = roll_mass(int(args["quantity"]), int(args["mod"]), int(args["ac"]), True, False)["description"]
    self.output['text'] = text
    send_message_to_discord(text)

  def disadvantage(self):
    args = self.get_args()
    text = roll_mass(int(args["quantity"]), int(args["mod"]), int(args["ac"]), False, True)["description"]
    self.output['text'] = text
    send_message_to_discord(text)

  def normal(self):
    args = self.get_args()
    text = roll_mass(int(args["quantity"]), int(args["mod"]), int(args["ac"]), False, False)["description"]
    self.output['text'] = text
    send_message_to_discord(text)

def main():
  root = Tk()
  root.title('DM Screen Roll Panel')
  gui = DmGUI(root)
  root.mainloop()

main()
