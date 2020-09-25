import sys
sys.path.append('./models')
sys.path.append('../roll72')
sys.path.append('../downtime')
from user import User, attempt_encode_auth_token, attempt_decode_auth_token, get_user_by_id, get_user_by_username
from character import Character
from crypto import encode_raw
from roll72 import roll_ability_scores
from downtime import get_downtime_activities
import json

class Orchestrator:
  def __init__(self, app):
    self.app = app
    self.stored_token = None

#------------------------------------------------------------------------------#
#     users                                                                    #
#------------------------------------------------------------------------------#

  def is_logged_in(self, request):
    token = request.cookies.get('magical_login_token')
    result = attempt_decode_auth_token(self.app, token)

    if result["success"] and self.validate_user(result['username'], result['password']):
      return result["success"]

  def get_user(self, request):
    token = request.cookies.get('magical_login_token')
    result = attempt_decode_auth_token(self.app, token)
    return self.get_user_by_username(result['username'])

  def login_user(self, request):
    if request.json is None:
      return {
        "success": False,
        "error": "null"
      }
    data = request.json
    username = data['username']
    password = data['password']

    if not self.validate_user(username, password):
      return {
        "success": False,
        "error": "invalid"
      }
    result = attempt_encode_auth_token(self.app, username, password)

    if not result["success"]:
      print("Error:{}".format(result))
      return {
        "success": False,
        "error": result["error"]
      }

    result['user'] = self.get_user_by_username(username)
    return result

  def register_user(self, request):
    json = request.json
    if json is None or json['username'] is None or json['password'] is None or json['email'] is None:
      return {
        "success": False,
        "error": "null"
      }
    
    if self.get_user_by_id(json['username']) is not None:
      return {
        "success": False,
        "error": "duplicate",
        "description": "That username is already taken. Please try another"
      }
    try:
      encoded = encode_raw(json['password'])
      self.app.db.insert_user(json['email'], json['username'], encoded['hashed'], encoded['salt'])

      return {
        "success": True
      }
    except Exception as e:
      print("{}".format(e))
      return {
        "success": False,
        "error": e
      }

  def validate_user(self, username, password):
    user = self.get_user_by_username(username)
    if user is list:
      user = user[0]
    if user is None:
      return False
    result = encode_raw(password, user.salt)

    return user.password == result["hashed"]

  def generate_stat_array(self):
    scores = roll_ability_scores()
    array = []
    for roll in scores:
      array.append(roll['total'])
    return array

  def get_user_by_id(self, user_id):
    return get_user_by_id(self.app.db, user_id)

  def get_user_by_username(self, username):
    return get_user_by_username(self.app.db, username)

#------------------------------------------------------------------------------#
#     permissions                                                              #
#------------------------------------------------------------------------------#

  def has_permission(self, user_id, permission):
    perms = self.get_user_permissions(user_id)
    return permission in perms

  def get_user_permissions(self, user_id):
    results = self.app.db.select_user_permissions(user_id)
    perms = []
    for row in results:
      perms.append(row[1])
    return perms

#------------------------------------------------------------------------------#
#     characters                                                               #
#------------------------------------------------------------------------------#
  def validate_character(self, request):
    character = self.create_character(request)
    try:
      character.load_json(request.json['character'])
      existing_character = load_character(character.user_id, character.character_id)
      if existing_character is not None and character.immutable_fields_changed(existing_character):
        return False
    except Exception as e:
      return False
    return character is not None and character.is_valid()

  def request_character(self, request):
    character_id = request.json['character_id']
    user = self.get_user(request)
    if user is None:
      print("could not get user")
      return None
    if character_id is None:
      print("character_id is null")
      return None
    if character_id not in self.get_valid_character_ids():
      print("Invalid character_id {}".format(character_id))
      return None
    if self.load_character(user.uid, character_id) is not None:
      print("Character already exists")
      return None
    character = self.create_character(user.uid, character_id)
    self.store_character(character)
    return character

  def get_valid_character_ids(self):
    return [0, 1, 2]

  def get_characters_json_by_user_id(self, user_id):
    characters = self.get_characters_by_user_id(user_id)
    data = []
    for character in characters:
      if character.character_id in self.get_valid_character_ids():
        data.append(character.get_json())
    return data

  def get_characters_by_user_id(self, user_id):
    characters = []
    data = self.app.db.select_characters_by_user_uid(user_id)
    if len(data) > 0:
      for character_row in data:
        character_dict = {
          "user_id": character_row[0],
          "character_id": character_row[1],
          "raw": character_row[2]
        }
        character = Character()
        character.load_json(character_dict['raw'])
        character.user_id = user_id
        character.character_id = character_dict['character_id']
        characters.append(character)
    return characters

  def create_character(self, user_id, character_id):
    character = Character()
    character.ability_scores_array = self.generate_stat_array()
    character.user_id = user_id
    character.character_id = character_id
    character.strength = character.ability_scores_array[0]
    character.dexterity = character.ability_scores_array[1]
    character.constitution = character.ability_scores_array[2]
    character.intelligence = character.ability_scores_array[3]
    character.wisdom = character.ability_scores_array[4]
    character.charisma = character.ability_scores_array[5]
    return character

  def update_character(self, request):
    user = self.get_user(request)
    if user is None:
      print("No user")
      return None

    json_obj = request.json
    print("json {}".format(request.json))
    if json_obj is None or json_obj['character'] is None:
      print("No character in json")
      return None
    
    character = Character(json.dumps(json_obj['character']))
    existing_character = self.load_character(character.user_id, character.character_id)
    if existing_character is None:
      print("Character does not currently exist")
      return None

    if not character.is_valid():
      print("Character invalid")
      return None

    # Copy immutable fields to existing character data
    existing_character.load_json(character.get_json())

    self.store_character(existing_character)
    return character

  def store_character(self, character):
    data = character.get_json()
    if self.load_character(character.user_id, character.character_id) is None:
      self.app.db.insert_character(character.user_id, character.character_id, data)
    else:
      self.app.db.update_character(character.user_id, character.character_id, data)

  def load_character(self, user_id, character_id):
    results = self.app.db.select_character(user_id, character_id)
    if len(results) > 0 and len(results[0]) > 2:
      character = Character()
      character.load_json(results[0][2])
      character.user_id = user_id
      character.character_id = character_id
      return character
    return None

#------------------------------------------------------------------------------#
#     downtime                                                                 #
#------------------------------------------------------------------------------#

  def get_downtime_selection_data(request):
    ret = {}
    user = self.get_user(request)

    characters = self.get_characters_by_user_id(user.uid)
    activities = get_downtime_activities()

    

    return 