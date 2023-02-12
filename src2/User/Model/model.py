# import sqlite3
from sqlite3 import connect, IntegrityError
from passlib.hash import sha256_crypt as sha

SALT="paco"


class Model:
	def __init__(self, path_db=":memory:"):
		self.path_db = path_db

	def execute(self, query:str):
		try:
			conection = connect(self.path_db)
			cursor = conection.cursor()
			cursor.execute(query)
			conection.commit()
			conection.close()
		except:
			return False
		return True

	def execute_insert(self, query:str, values:tuple) -> bool:
		try: 
			conection = connect(self.path_db)
			cursor = conection.cursor()
			cursor.execute(query, values)
			conection.commit()
			conection.close()
		except IntegrityError as ex:
			print(str(ex))
			print(" username already exist")
			return False
		except Exception as ex:
			print(ex)
			return False
		return True

	def execute_select(self, query:str, values:tuple) -> tuple:
		conection = connect(self.path_db)
		cursor = conection.cursor()
		result = cursor.execute(query, values).fetchall()
		conection.commit()
		conection.close()
		return result
		
	def create_table(self):
		query = "DROP TABLE IF EXISTS users;" ### EXPERIMENTAL
		self.execute(query)
		query = "CREATE TABLE IF NOT EXISTS users (\
			username varchar(64) UNIQUE,\
			password varchar(64)\
		);"
		self.execute(query)

	def register(self, username:str, password:str):
		# try: 
		query = "INSERT INTO users VALUES (?, ?);"
		password_hashed = self.hash(password)
		# print("len = ", len(password_hashed), " : ", password_hashed)
		res = self.execute_insert( query, (username, password_hashed) )
		# except Exception:
		# 	print(Exception)
		# 	return False
		return res

	def login(self, username:str, password:str) -> bool:
		query = "SELECT * FROM users WHERE username = (?) and password = (?)"
		password_hashed = self.hash(password)
		# print("len = ", len(password_hashed), " : ", password_hashed)
		result = self.execute_select( query, (username, password_hashed) )
		return result is not None

	def get_all(self):
		query = "SELECT * FROM users;"
		return self.execute_select(query, ())

	def remove(self, username:str) -> bool:
		query = "DELETE FROM users WHERE username = (?)"
		self.execute(query, username)
		pass

	def update(self, username:str = None, password:str = None) -> bool:
		pass

	def hash(self, password:str) -> str:
		return sha.using(rounds=1000, salt=SALT).hash(password).split("$")[-1]


if __name__ == "__main__":
	from user import User
	model = Model("user.db")
	model.create_table()
	while True:
		option = input(" 0 - Exit\n 1 - Login\n 2 - Register\n 3 - Delete account\n 4 - Show all\n > ")
		user = User()
		if not user.set_username(input(" Username: ")):
			print(" Invalid username")
			continue
		if not user.set_password(input(" Password: ")):
			print(" Invalid password")
			continue
		if int(option) == 0:
			break
		elif int(option) == 1:
			if model.login(user.username, user.password):
				print(" logged")
			else:
				print(" not logged")
		elif int(option) == 2:
			model.register(user.username, user.password)
		elif int(option) == 3:
			if user.logged:
				model.remove(user.username, user.password)
		elif int(option) == 4:
			print(model.get_all())
		else:
			print(" Error")

