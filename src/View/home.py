from customtkinter import CTkFrame, CTkLabel, CTkButton

if __name__ == "__main__":
	from customtkinter import CTk
else:
	from Controller import Controller


class Home(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		# Home page
		self.home_label = CTkLabel(master=self, text="Home Page ", width=100, height=30)
		self.home_label.pack(padx=50)

	def set_controller(self, controller):
		self.controller = controller

	def show_menu(self):
		self.pack()


if __name__ == "__main__":
	root = CTk()
	home = Home(root)
	home.pack()
	root.mainloop()
