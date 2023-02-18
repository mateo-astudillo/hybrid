from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkImage, CTkLabel


class Login(CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.view = master

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
		entries = list(self.entries.values())
		buttons = list(self.buttons.values())

		for widget in entries + buttons:
			widget.pack(padx=10, pady=10, ipadx=10, ipady=10)

	def login(self):
		username = self.entries.get("username")
		password = self.entries.get("password")
		self.controller.login(username.get(), password.get())
		self.clear_entries()

	def clear_entries(self):
		for entry in self.entries.values():
			entry.delete(0,"end")

	def register(self):
		# self.controller.show_page("register")
		self.view.pack_forget()
		self.view.register.pack()


class Register(CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.view = master

		self.buttons = {
			"register": CTkButton(master=self, text="Register", command=self.register),
			"cancel": CTkButton(master=self, text="Cancel", command=self.cancel)
	    }

		self.entries = {
			"username": CTkEntry(master=self, placeholder_text="Username"),
			"password": CTkEntry(master=self, placeholder_text="Password", show="*")
		}

		self.pack_widgets()

	def set_controller(self, controller):
		self.controller = controller

	def pack_widgets(self):
		entries = list(self.entries.values())
		buttons = list(self.buttons.values())

		for widget in entries + buttons:
			widget.pack(padx=10, pady=10, ipadx=10, ipady=10)

	def register(self):
		username = self.entries.get("username")
		password = self.entries.get("password")

		# self.controller.register(username.get(), password.get())
		self.clear_entries()
		self.pack_forget()
		self.view.login.pack()

	def clear_entries(self):
		for entry in self.entries.values():
			entry.delete(0,"end")

	def cancel(self):
		self.pack_forget()
		self.view.login.pack()


if __name__ == "__main__":
	from customtkinter import CTk
	root = CTk()
	page = UserPage(root)
	page.pack()
	root.mainloop()
