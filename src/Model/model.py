from passlib.hash import sha256_crypt as sha
from dotenv import load_dotenv
from .users import UsersManager
from .cars import CarsManager
import sqlite3
import os

load_dotenv()
SALT = os.getenv("SALT")
USERS_DB = os.getenv("USERS_DB")
CARS_DB = os.getenv("CARS_DB")

class Model:
	def __init__(self):
		self.users_manager = UsersManager()
		self.cars_manager = CarsManager()

	def set_controller(self, controller):
		self.cars_manager.set_controller(controller)
		self.users_manager.set_controller(controller)

	def init_db(self):
		sql = """
			CREATE TABLE Brand (
				id integer PRIMARY KEY AUTOINCREMENT,
				name varchar
			);

			CREATE TABLE Model (
				id integer PRIMARY KEY AUTOINCREMENT,
				name varchar,
				year integer,
				brand_id integer
			);

			CREATE TABLE User (
				id integer PRIMARY KEY AUTOINCREMENT,
				username varchar,
				password varchar,
				name varchar,
				surname varchar,
				credit float
			);

			CREATE TABLE Car (
				id integer PRIMARY KEY AUTOINCREMENT,
				model_id integer,
				status_id integer
			);

			CREATE TABLE Sale (
				car_id integer,
				user_id integer,
				paid_method_id integer,
				price float
			);

			CREATE TABLE Status (
				id integer PRIMARY KEY AUTOINCREMENT,
				name varchar
			);

			CREATE TABLE PaidMethod (
				id integer PRIMARY KEY AUTOINCREMENT,
				method varchar
			);
		"""
		print(sql)

if __name__ == "__main__":
	model = Model()
