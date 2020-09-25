CREATE USER IF NOT EXISTS 'dndutils'@'localhost' IDENTIFIED BY 'utils';
GRANT ALL PRIVILEGES ON dndutils.* TO 'dndutils'@'localhost';

CREATE DATABASE IF NOT EXISTS dndutils;

USE dndutils;

CREATE TABLE IF NOT EXISTS users(
  pid INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  email VARCHAR(256) NOT NULL,
  pass_hash VARCHAR(256) NOT NULL,
  salt VARCHAR(256) NOT NULL,
  PRIMARY KEY(pid)
);

CREATE TABLE IF NOT EXISTS permissions(
  user_id INT NOT NULL,
  permission VARCHAR(100) NOT NULL,
  PRIMARY KEY(user_id, permission)
);

CREATE TABLE IF NOT EXISTS characters(
  user_id INT NOT NULL,
  character_id VARCHAR(256) NOT NULL,
  character_data TEXT NOT NULL,
  PRIMARY KEY(user_id, character_id)
);

CREATE TABLE IF NOT EXISTS downtime_activities(
  character_id INT NOT NULL,
  user_id INT NOT NULL,
  activity_id INT NOT NULL,
  week INT NOT NULL,
  year INT NOT NULL,
  outcome_string TEXT,
  PRIMARY KEY(user_id, character_id, week)
);