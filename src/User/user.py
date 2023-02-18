from .Controller import Controller
from .Persistence import DBManager
from .View import Login, Register


class User:
	def __init__(self, master):
		self.login = Login(master)
		self.register = Register(master)

		self.login.pack()

	def login(self):
		return self.login.logged


if __name__ == "__main__":
	from customtkinter import CTk
