import sqlite3
import bcrypt

PATH_DB = "data.db"

class Model:
	def __init__(self):
		self.connection = sqlite3.connect(database=":memory:")
		self.cursor = self.connection.cursor()
		self.cursor.execute("CREATE TABLE tokens ( username varchar(50), password varchar(64) );")

		self.controller = None

	def set_controller(self, controller):
		self.controller = controller

	def login(self, username:str, password:str):
		salt = bcrypt.gensalt()
		hash = bcrypt.hashpw(password.encode("utf-8"), salt)
		self.cursor.execute("INSERT INTO tokens VALUES(?, ?);", (username, hash) )

	def get_credentials(self):
		username = self.cursor.execute("SELECT username FROM tokens;").fetchone()
		password = self.cursor.execute("SELECT password FROM tokens;").fetchone()
		return (username, password)
		
