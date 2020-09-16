#!/usr/bin/python3
import sys
sys.path.append('./models')
from character import Character
import datetime
import jwt

class User:
  def __init__(self, data):
    self.uid = data['numerical_id']
    self.username = data['username']
    self.password = data['password']
    self.email = data['email']
    self.salt = data['salt']
    self.characters = []
    self.permissions = []

def get_user_by_id(db, user_id):
  data = db.select_user_by_id(user_id)
  return format_user_from_data(data)

def get_user_by_username(db, username):
  data = db.select_user_by_username(username)
  return format_user_from_data(data)

def format_user_from_data(data):
  print("Data{}".format(data))
  if len(data) == 0:
    return None

  user = User({
    "numerical_id": data[0][0],
    "username": data[0][1],
    "email": data[0][2],
    "password": data[0][3],
    "salt": data[0][4]
  })

  return user

def attempt_encode_auth_token(app, username, password):
  if user_id is None or password is None:
    return {
      "success": False,
      "error": "null"
    }

  try:
    payload = {
      'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
      'iat': datetime.datetime.utcnow(),
      'pi': username,
      'pw': password
    }
    
    ret = {
      "success": True,
      "token": jwt.encode(
        payload,
        app.config.get('SECRET_KEY'),
        algorithm='HS256'
      )
    }
    return ret
  except Exception as e:
    return {
      "success": False,
      "error": e
    }

def attempt_decode_auth_token(app, auth_token):
  if auth_token is None:
    return {
      "success": False,
      "error": "null",
      "description": "Token was null. user had no token"
    }
  try:
    payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
    return {
      "success": True,
      "username": payload['pi'],
      "password": payload['pw']
    }
  except jwt.ExpiredSignatureError:
    return {
      "success": False,
      "error": "expired",
      "description": 'Signature expired. Please log in again.'
    }
  except jwt.InvalidTokenError:
    return {
      "success": False,
      "error": "invalid",
      "description": 'Invalid token. Please log in again.'
    }