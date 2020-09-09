#!/usr/bin/python3



from flask import Flask, request, make_response, url_for, redirect
from flask import render_template, jsonify
from db import Db
import json
import os
from orchestrator import Orchestrator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuperDuperSecure'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dndutils'
app.config['MYSQL_PASSWORD'] = 'utils'
app.config['MYSQL_DB'] = 'dndutils'
app.db = Db(app)

orc = Orchestrator(app)

@app.route('/', methods=['GET'])
def index():
  if(not orc.is_logged_in(request)):
    return redirect(url_for('login'), code=302)
  user = orc.get_user(request)
  return render_template("index.html", username=user.username)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    result = orc.login_user(request)

    if result['success']:
      json = jsonify({
          "success": 1,
          "redirect": url_for("index")
        })
      resp = make_response(json)
      resp.set_cookie("magical_login_token", result['token'])
      print('success')
      return resp, 200
    else:
      print('Failure: {}'.format(result))
      return "Your login failed"

  return render_template("login.html")

@app.route('/register', methods=['POST'])
def register():
  reg_result = orc.register_user(request)
  if reg_result['success']:
    result = orc.login_user(request)
    if result['success']:
      json = jsonify({
          "success": 1,
          "redirect": url_for("index")
        })
      resp = make_response(json)
      resp.set_cookie("magical_login_token", result['token'])
      print('success')
      return resp, 200
    else:
      print("Error registering: {}".format(result))
      return "Error", 400
  else:
    print("Error registering: {}".format(reg_result))
    return "Error", 400

@app.route('/my_characters', methods=['GET'])
def my_characters():
  if(not orc.is_logged_in(request)):
    return redirect(url_for('login'), code=302)
  user = orc.get_user(request)
  characters = orc.get_characters_json_by_user_id(user.uid)
  return render_template("my_characters.html", characters=characters)

@app.route('/request_character', methods=['POST'])
def request_character():
  if(not orc.is_logged_in(request)):
    return "Forbidden", 401
  character = orc.request_character(request)
  print("request character finished")
  if character is None:
    return "Internal Server Error", 500
  return {
    "character_id": character.character_id,
    "character": character.get_json()
  }, 201

@app.route('/update_character', methods=['POST'])
def update_character():
  if(not orc.is_logged_in(request)):
    return "Forbidden", 401
  character = orc.update_character(request)
  if character is None:
    return "Internal Server Error", 500
  return {
    "character_id": character.character_id,
    "character": character.get_json()
  }, 201

@app.route('/character/view/<int:user_id>/<int:character_id>/', methods=['GET'])
def view_character(user_id, character_id):
  character = orc.load_character(user_id, character_id)

  if character is None:
    return redirect(url_for('not_found'), code=302)

  output = character.get_json() if character is not None else "None"
  return render_template('view_character.html', characters=[character.get_json()])

@app.route('/not_found', methods=['GET'])
def not_found():
  return "Not found"

@app.route('/character_roster', methods=['GET'])
def roster():
  return "Character roster"

@app.route('/vault', methods=['GET'])
def vault():
  return "Vault"

@app.route('/downtime', methods=['GET'])
def downtime():
  return "Downtime"


if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)