from sqlite3 import connect, IntegrityError
from passlib.hash import sha256_crypt as sha
from dotenv import load_dotenv
from os import getenv

load_dotenv()
SALT = getenv("SALT")


class CarsDBManager:
	def __init__(self, path_db:str):
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

	def execute_select(self, query:str, values:tuple = ()) -> tuple:
		conection = connect(self.path_db)
		cursor = conection.cursor()
		result = cursor.execute(query, values).fetchone()
		conection.commit()
		conection.close()
		return result
		
	def create_tables(self):
		self.execute("DROP TABLE cars;") # dev
		queries = [
			"CREATE TABLE IF NOT EXISTS cars (\
			id int(8) PRIMARY KEY NOT NULL,\
			stock int(16) NOT NULL,\
			price float(16) NOT NULL,\
			id_brand int(8),\
			id_model int(8)\
			);",
			"CREATE TABLE IF NOT EXISTS car_brand (\
			id int(8) PRIMARY KEY NOT NULL,\
			brand varchar(63),\
			id_model int(8)\
			);",
			"CREATE TABLE IF NOT EXISTS car_model (\
			id int(8) PRIMARY KEY NOT NULL,\
			model varchar(63),\
			year int(16)\
			);",
			# "CREATE TABLE IF NOT EXISTS car_year (\
			# id int(8) PRIMARY KEY NOT NULL,\
			# year int(16),\
			# id_model int(16)\
			# );"
		]
		
		for query in queries:
			self.execute(query)

	def add_car(self, brand:str, model:str, year:int, stock:int, price:float = 0):
		# Brand
		self.execute_values(
			"INSERT INTO car_brand (brand) VALUES (?);", (brand, )
		)
		id_brand = self.execute_select(
			"SELECT id FROM car_brand WHERE brand = (?);",
			(brand, ) 
		)[0]

		# Model
		self.execute_values(
			"INSERT INTO car_model (id_brand, model, year) VALUES (?, ?, ?);",
			(id_brand, model, year)
		)
		id_model = self.execute_select(
			"SELECT id FROM car_model WHERE model = (?);", (model, )
		)[0]

		# Car
		self.execute_values(
			"INSERT INTO car (stock, price, id_brand, id_model)"
		)

			# "CREATE TABLE IF NOT EXISTS cars (\
			# id int(8) PRIMARY KEY NOT NULL,\
			# stock int(16) NOT NULL,\
			# price float(16) NOT NULL,\
			# id_brand int(8),\
			# id_model int(8),\
			# id_year int(8)\
			# );",

	def remove_car(self):
		pass

	def get_all(self):
		query = "SELECT * FROM cars;"
		return self.execute_select(query)

	def hash(self, password:str) -> str:
		return sha.using(rounds=1000, salt=SALT).hash(password).split("$")[-1]

if __name__ == "__main__":
	DATA_PATH = getenv("DATA_PATH", "./")
	dbm = CarsDBManager(DATA_PATH + "hybrid.db")
	dbm.create_tables()
	for item in dbm.get_all():
		print(item)

