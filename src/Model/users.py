from passlib.hash import sha256_crypt as sha
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()
SALT = os.getenv("SALT")
DATABASE = os.getenv("DATABASE")


class UsersManager():
	def __init__(self):
		super().__init__()

		sha.default_rounds = 1000
		
		self.controller = None
		self.connection = None
		self.cursor = None
		self.create_table()

	def connect(self):
		self.connection = sqlite3.connect(database=USERS_DB)
		self.cursor = self.connection.cursor()

	def disconnect(self):
		self.connection.commit()
		self.connection.close()
		self.connection = None
		self.cursor = None

	def create_table(self):
		query = ""

		self.connect()
		self.cursor.execute(sql)
		self.disconnect()

	def set_controller(self, controller):
		self.controller = controller

	def login(self, username:str, password:str):
		password_hashed = sha.using(salt=SALT).hash(password).split("$")[-1]
		self.connect()
		password_saved = self.cursor.execute(
			"SELECT PASSWORD FROM users WHERE USERNAME = (?);", (username,)
		).fetchone()
		self.disconnect()
		return password_hashed == password_saved[0]

	def register(self, username:str, password:str):
		password_hashed = sha.using(salt=SALT).hash(password).split("$")[-1]
		self.connect()
		self.cursor.execute("INSERT INTO users VALUES(?, ?);", (username, password_hashed) )
		self.disconnect()

	def get_credentials(self):
		username = self.cursor.execute("SELECT username FROM users;").fetchone()
		password = self.cursor.execute("SELECT password FROM users;").fetchone()
		return (username, password)
