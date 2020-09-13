import mysql.connector

class Db:
  def __init__(self, app):
    self.app = app
    self.mysql = mysql.connector.connect(
      host=app.config['MYSQL_HOST'],
      user=app.config['MYSQL_USER'],
      password=app.config['MYSQL_PASSWORD'],
      database=app.config['MYSQL_DB']
    )

  def select(self, sql, values):
    print("{}:{}".format(sql, values))
    cur = self.mysql.cursor()
    cur.execute(sql, values)
    data = cur.fetchall()
    cur.close()
    return data

  def insert(self, sql, values):
    print("{}:{}".format(sql, values))
    cur = self.mysql.cursor()
    cur.execute(sql, values)
    self.mysql.commit()
    cur.close() 

  def update(self, sql, values):
    print("{}:{}".format(sql, values))
    cur = self.mysql.cursor()
    cur.execute(sql, values)
    self.mysql.commit()
    cur.close() 

  def insert_user(self, email, user_id, password, salt):
    sql = "INSERT INTO users(username, pass_hash, salt, email) VALUES (%s, %s, %s, %s)"
    values = [ email, user_id, password, salt ]
    self.insert(sql, values)

  def select_user_by_id(self, user_id):
    sql = "SELECT * FROM users WHERE username = %s"
    values = [user_id]
    return self.select(sql, values)

  def select_characters_by_user_uid(self, uid):
    sql = "SELECT * FROM characters WHERE user_id = %s"
    values = [uid,]
    return self.select(sql, values)

  def insert_character(self, user_id, character_id, character_data):
    sql = "INSERT INTO characters(user_id, character_id, character_data) VALUES (%s, %s, %s)"
    values = [str(user_id), str(character_id), str(character_data)]
    self.insert(sql, values)

  def update_character(self, user_id, character_id, character_data):
    sql = "UPDATE characters SET character_data = %s WHERE user_id = %s AND character_id = %s"
    values = [str(character_data), str(user_id), str(character_id)]
    self.update(sql, values)

  def select_character(self, user_id, character_id):
    sql = "SELECT * FROM characters WHERE user_id = (%s) AND character_id = (%s)"
    values = [str(user_id), str(character_id),]
    return self.select(sql, values)