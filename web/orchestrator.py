#!/usr/bin/python3
import sys
sys.path.append('./models')
sys.path.append('../roll72')
from user import User, attempt_encode_auth_token, attempt_decode_auth_token, get_user_by_id
from character import Character
from crypto import encode_raw
from roll72 import roll_ability_scores
import json

class Orchestrator:
  def __init__(self, app):
    self.app = app
    self.stored_token = None

  def is_logged_in(self, request):
    token = request.cookies.get('magical_login_token')
    result = attempt_decode_auth_token(self.app, token)

    if result["success"] and self.validate_user(result['user_id'], result['password']):
      return result["success"]

  def get_user(self, request):
    token = request.cookies.get('magical_login_token')
    result = attempt_decode_auth_token(self.app, token)
    return self.get_user_by_id(result['user_id'])

  def login_user(self, request):
    if request.json is None:
      return {
        "success": False,
        "error": "null"
      }
    data = request.json
    user_id = data['username']
    password = data['password']

    if not self.validate_user(user_id, password):
      return {
        "success": False,
        "error": "invalid"
      }
    result = attempt_encode_auth_token(self.app, user_id, password)

    if not result["success"]:
      print("Error:{}".format(result))
      return {
        "success": False,
        "error": result["error"]
      }

    result['user'] = self.get_user_by_id(user_id)
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

  def validate_user(self, user_id, password):
    user = self.get_user_by_id(user_id)
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

  def validate_character(self, request):
    character = self.create_character(request)
    try:
      character.load_json(request.json.character)
      existing_character = load_character()
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
    if character_id not in [0, 1, 2]:
      print("Invalid character_id {}".format(character_id))
      return None
    if self.load_character(character_id) is not None:
      print("Character already exists")
      return None
    character = self.create_character(user.uid, character_id)
    self.store_character(character)
    return character

  def get_characters_by_user_id(self, user_id):
    characters = []
    data = self.app.db.select_characters_by_user_uid(user_id)
    if len(data) > 0:
      for character_row in data:
        character_dict = {
          "user_id": character_row[0],
          "name": character_row[1],
          "raw": character_row[2]
        }
        character = Character()
        character.load_json(character_dict['raw'])
        characters.append(character)
    return characters

  def create_character(self, user_id, character_id):
    character = Character()
    character.ability_scores_array = self.generate_stat_array()
    character.user_id = user_id
    character.character_id = character_id
    return character

  def store_character(self, character):
    data = character.get_json()
    self.app.db.insert_character(character.user_id, character.character_id, data)

  def load_character(self, character_id):
    results = self.app.db.select_character_by_id(character_id)
    if len(results) > 0 and len(results[0]) > 2:
      character = Character()
      character.load_json(results[0][2])
      return character
    return None
    