from customtkinter import CTkFrame, CTkEntry, CTkButton
from User.view import View


class Login(CTkFrame):
	def __init__(self, master):
		super().__init__(master)

		self.entries = {
			"username": CTkEntry(master=self, placeholder_text="Username"),
			"password": CTkEntry(master=self, placeholder_text="Password"),
		}

		self.buttons = {
			"login": CTkButton(master=self, text="Login", command=self.login),
			"register": CTkButton(master=self, text="Register", command=self.register),
		}

		self.pack_items()

	def pack_items(self):
		for entry in self.entries.values():
			entry.pack()
		for button in self.buttons.values():
			button.pack()

	def login(self):
		pass

	def register(self):
		pass


if __name__ == "__main__":
	from customtkinter import CTk
	root = CTk()
	login = Login(root)
	login.pack()
	root.mainloop()
