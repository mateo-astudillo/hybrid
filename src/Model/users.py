from passlib.hash import sha512_crypt as sha
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()
SALT = os.getenv("SALT")
USERS_DB = os.getenv("USERS_DB")
CARS_DB = os.getenv("CARS_DB")


class UsersManager():
	def __init__(self):
		super().__init__()

		self.controller = None

		# sql = 'CREATE TABLE IF NOT EXISTS users (\
		# 	ID INTEGER NOT NULL,\
		# 	USERNAME varchar(64) UNIQUE,\
		# 	PASSWORD varchar(43),\
		# 	PRIMARY KEY(ID)\
		# );'
		sql = 'CREATE TABLE IF NOT EXISTS users (\
			USERNAME varchar(64) UNIQUE,\
			PASSWORD varchar(43)\
		);'

		self.connection = sqlite3.connect(database=USERS_DB)
		self.cursor = self.connection.cursor()
		self.cursor.execute(sql)

	def set_controller(self, controller):
		self.controller = controller

	def login(self, username:str, password:str):
		password_hashed = sha.using(salt=SALT).hash(password)
		password_saved = self.cursor.execute(
			"SELECT PASSWORD FROM users WHERE USERNAME = (?);", (username,)
		).fetchone()
		if password_hashed == password_saved:
			return True
		return False

	def register(self, username:str, password:str):
		password_hashed = sha.using(salt=SALT).hash(password)
		self.cursor.execute("INSERT INTO users VALUES(?, ?);", (username, password_hashed) )

	def get_credentials(self):
		username = self.cursor.execute("SELECT username FROM users;").fetchone()
		password = self.cursor.execute("SELECT password FROM users;").fetchone()
		return (username, password)
