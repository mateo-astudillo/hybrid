from sqlite3 import connect, IntegrityError
from passlib.hash import sha256_crypt as sha

SALT="paco"


class DBManager:
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

	def execute_values(self, query:str, values:tuple) -> bool:
		try: 
			conection = connect(self.path_db)
			cursor = conection.cursor()
			cursor.execute(query, values)
			conection.commit()
			conection.close()
		except IntegrityError:
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
		query = "CREATE TABLE IF NOT EXISTS users (\
			username varchar(64) UNIQUE,\
			password varchar(64)\
		);"
		self.execute(query)

	def register(self, username:str, password:str):
		query = "INSERT INTO users VALUES (?, ?);"
		password_hashed = self.hash(password)
		return self.execute_values( query, (username, password_hashed) )

	def login(self, username:str, password:str) -> bool:
		query = "SELECT * FROM users WHERE username = (?) and password = (?)"
		password_hashed = self.hash(password)
		result = self.execute_select( query, (username, password_hashed) )
		return result is not None

	def remove(self, username:str) -> bool:
		query = "DELETE FROM users WHERE username = (?)"
		return self.execute(query, username)

	def change_password(self, username:str, password:str) -> bool:
		password_hashed = self.hash(password)
		query = "UPDATE users SET password = (?) WHERE username = (?);"
		return self.execute_values( query, (password_hashed, username) )

	def change_username(self, username:str, new_username:str) -> bool:
		query = "UPDATE users SET username = (?) WHERE username = (?);"
		return self.execute_values( query, (new_username, username) )

	def hash(self, password:str) -> str:
		return sha.using(rounds=1000, salt=SALT).hash(password).split("$")[-1]


class User:
	def __init__(self):
		self.logged = False
		self.username = None
		self.password = None

	def set_username(self, username:str) -> bool:
		pattern = "[AZa-z0-9]"
		if not match(pattern, username): 
			return False
		self.username = username
		return True

	def set_password(self, password:str) -> bool:
		pattern = "[AZa-z0-9]"
		if not match(pattern, password): 
			return False
		self.password = password
		return True


if __name__ == "__main__":
	print("DBManager")
	dbm = DBManager("users.db")
	dbm.create_table()

