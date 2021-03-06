import json

class Character:
  def __init__(self, json_text=None):
    self.loaded = False
    init_blank_fields(self)
    if json_text is not None:
        self.load_json(json_text)

  def load_json(self, json_text):
    data = json.loads(json_text)
    for field in get_all_fields():
      # immutable fields should be loaded exactly once.
      if self.loaded and field in get_immutable_fields():
        print("Not updating immutable field {}".format(field))
      elif field in data:
        setattr(self, field, data[field])
      else:
        setattr(self, field, "")
    self.loaded = True

  def get_json(self):
    data = {}
    for field in get_all_fields():
      data[field] = getattr(self, field)
    return json.dumps(data)

  def is_valid(self):
    try:
      for field in get_list_fields():
        value = getattr(self, field)
        if not isinstance(value, list):
          print("{} was not a list".format(field))
          return False
      for field in get_string_fields():
        value = getattr(self, field)
        if not isinstance(value, str) and not isinstance(value, int):
          print("{} was not a string nor int".format(field))
          return False
    except Exception as e:
      print("Encountered exception {}".format(e))
      return False
    return True

  def immutable_fields_changed(self, other_character):
    for field in get_immutable_fields():
      if getattr(self, field) != getattr(other_character, field):
        print("{} was changed!".format(field))
        return False

def init_blank_fields(character):
  for field in get_list_fields():
    setattr(character, field, [])
  for field in get_string_fields():
    setattr(character, field, "")

def get_all_fields():
  return get_list_fields() + get_string_fields()

def get_immutable_fields():
  return [
    "user_id",
    "character_id",
    "ability_scores_array"
  ]  

def get_list_fields():
  return [
    "known_spells",
    "inventory",
    "currency",
    "features_and_traits",
    "ability_scores_array",
    "proficiencies"
  ]

def get_string_fields():
  return [
    "user_id",
    "character_id",
    # Ability scores
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
    # Ability score mods
    "strength_mod",
    "dexterity_mod",
    "constitution_mod",
    "intelligence_mod",
    "wisdom_mod",
    "charisma_mod",
    # Saving throws
    "strength_save",
    "dexterity_save",
    "constitution_save",
    "intelligence_save",
    "wisdom_save",
    "charisma_save",
    # Saving throw proficiencies
    "strength_save_prof",
    "dexterity_save_prof",
    "constitution_save_prof",
    "intelligence_save_prof",
    "wisdom_save_prof",
    "charisma_save_prof",
    # Skills
    "acrobatics",
    "animal_handling",
    "arcana",
    "athletics",
    "deception",
    "history",
    "insight",
    "intimidation",
    "investigation",
    "medicine",
    "nature",
    "perception",
    "performance",
    "persuasion",
    "religion",
    "sleight_of_hand",
    "stealth",
    "survival",
    # skill proficiencies
    "acrobatics_prof",
    "animal_handling_prof",
    "arcana_prof",
    "athletics_prof",
    "deception_prof",
    "history_prof",
    "insight_prof",
    "intimidation_prof",
    "investigation_prof",
    "medicine_prof",
    "nature_prof",
    "perception_prof",
    "performance_prof",
    "persuasion_prof",
    "religion_prof",
    "sleight_of_hand_prof",
    "stealth_prof",
    "survival_prof",
    # Top section
    "biography",
    "proficiency_bonus",
    "character_name",
    "class_and_level",
    "background",
    "player_name",
    "race",
    "alignment",
    "experience_points",
    # Middle section
    "armor_class",
    "initiative",
    "speed",
    "hit_point_maximum",
    "hit_dice",
    # Attacks
    "attack_1",
    "attack_bonus_1",
    "attack_damage_1",
    "attack_2",
    "attack_bonus_2",
    "attack_damage_2",
    "attack_3",
    "attack_bonus_3",
    "attack_damage_3",
    # Spell slots
    "spell_dc",
    "spell_attack_bonus",
    "spellslots_1st",
    "spellslots_2nd",
    "spellslots_3rd",
    "spellslots_4th",
    "spellslots_5th",
    "spellslots_6th",
    "spellslots_7th",
    "spellslots_8th",
    "spellslots_9th",
    # Currency
    "gold_pieces"
    ]

def main():
  character = Character()
  data = character.get_json()
  character.character_name = "bopeep"
  character.load_json(data)
  print("{}".format(character.get_json()))
