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