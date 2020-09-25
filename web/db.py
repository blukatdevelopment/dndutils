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

  def delete(self, sql, values):
    print("{}:{}".format(sql, values))
    cur = self.mysql.cursor()
    cur.execute(sql, values)
    self.mysql.commit()
    cur.close() 

#------------------------------------------------------------------------------#
#     users                                                                    #
#------------------------------------------------------------------------------#
  def insert_user(self, email, user_id, password, salt):
    sql = "INSERT INTO users(username, pass_hash, salt, email) VALUES (%s, %s, %s, %s)"
    values = [ user_id, password, salt, email]
    self.insert(sql, values)

  def select_user_by_id(self, user_id):
    sql = "SELECT * FROM users WHERE pid = %s"
    values = [user_id]
    return self.select(sql, values)

  def select_user_by_username(self, username):
    sql = "SELECT * FROM users WHERE username = %s"
    values = [username]
    return self.select(sql, values)

#------------------------------------------------------------------------------#
#     permissions                                                              #
#------------------------------------------------------------------------------#

  def insert_user_permission(self, user_id, permission):
    sql = "INSERT INTO permissions(user_id, permission) VALUES (%s, %s)"
    values = [ user_id, permission]
    self.insert(sql, values)

  def delete_user_permission(self, user_id, permission):
    sql = "DELETE FROM permissions WHERE user_id = %s AND permission = %s"
    values = [ user_id, permission]
    self.delete(sql, values)

  def select_user_permissions(self, user_id):
    sql = "SELECT * FROM permissions WHERE user_id = %s"
    values = [user_id]
    return self.select(sql, values)

#------------------------------------------------------------------------------#
#     characters                                                               #
#------------------------------------------------------------------------------#

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
    values = [str(user_id), str(character_id)]
    return self.select(sql, values)

#------------------------------------------------------------------------------#
#     downtime                                                                 #
#------------------------------------------------------------------------------#
  def insert_downtime(self,  character_id, user_id, activity_id, week, year, outcome_string):
    sql = "INSERT INTO downtime_activities(character_id, user_id, activity_id, week, year, outcome_string) VALUES (%s, %s, %s, %s, %s, %s)"
    values = [str(user_id), str(character_id), str(character_data)]
    self.insert(sql, values)

  def update_downtime_outcome(self, user_id, character_id, year, week, outcome_string):
    sql = "UPDATE downtime_activities SET outcome_string = %s "
    sql += "WHERE user_id = %s "
    sql += "AND character_id = %s " 
    sql += "AND year = %s "
    sql += "AND week = %s"
    values = [
      str(user_id),
      str(character_id),
      str(year),
      str(week),
      str(outcome_string),
    ]
    self.update(sql, values)

  def select_downtime_by_user_id(self, user_id):
    sql = "SELECT character_id, user_id, activity_id, week, year, outcome_string FROM downtime_activites WHERE user_id = (%s)"
    values = [str(user_id)]
    return self.select(sql, values)

  def select_downtime_for_character(self, user_id, character_id):
    sql = "SELECT character_id, user_id, activity_id, week, year, outcome_string FROM downtime_activites WHERE user_id = (%s) AND character_id = (%s)"
    values = [str(user_id), str(character_id)]
    return self.select(sql, values)

  def select_downtime_by_year(self, year):
    sql = "SELECT character_id, user_id, activity_id, week, year, outcome_string FROM downtime_activites WHERE year = (%s)"
    values = [str(user_id), str(year)]
    return self.select(sql, values)