from customtkinter import CTkFrame, CTkEntry, CTkButton

if __name__ == "__main__":
	from customtkinter import CTk


class Register(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		self.buttons = {
			"register": CTkButton(master=self, text="Register", command=self.register),
			"cancel": CTkButton(master=self, text="Cancel", command=self.cancel),
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
			widget.pack(padx=7, pady=15, ipadx=20)

	def register(self):
		username = self.entries.get("username")
		password = self.entries.get("password")
		self.controller.register(username.get(), password.get())
		self.clear_entries()

	def clear_entries(self):
		for entry in self.entries.values():
			entry.delete(0,"end")

	def cancel(self):
		self.controller.show_page("login")
		pass



if __name__ == "__main__":
	root = CTk()
	register = Register(root)
	register.pack()
	root.mainloop()
