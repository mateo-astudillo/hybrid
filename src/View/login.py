from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkImage, CTkLabel
from PIL import Image
from dotenv import load_dotenv
import os

if __name__ == "__main__":
	from customtkinter import CTk

load_dotenv()
ASSETS_PATH = os.getenv("ASSETS_PATH")



class Login(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		self.buttons = {
			"login": CTkButton(master=self, text="Login", command=self.login),
			"register": CTkButton(master=self, text="Register", command=self.register),
		}

		self.entries = {
			"username": CTkEntry(master=self, placeholder_text="Username"),
			"password": CTkEntry(master=self, placeholder_text="Password", show="*")
		}
		self.pack_widgets()

	def set_controller(self, controller):
		self.controller = controller

	def pack_widgets(self):
		# self.image.get("image").pack()
		entries = list(self.entries.values())
		buttons = list(self.buttons.values())

		for widget in entries + buttons:
			widget.pack(padx=7, pady=15, ipadx=20)

	def login(self):
		username = self.entries.get("username")
		password = self.entries.get("password")
		self.controller.login(username.get(), password.get())
		self.clear_entries()

	def clear_entries(self):
		for entry in self.entries.values():
			entry.delete(0,"end")

	def register(self):
		self.controller.show_page("register")



if __name__ == "__main__":
	root = CTk()
	login = Login(root)
	login.pack()
	root.mainloop()