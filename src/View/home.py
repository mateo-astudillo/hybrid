from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkImage
from PIL import Image
if __name__ == "__main__":
	from customtkinter import CTk


class Home(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None
		# Home page
		self.home_label = CTkLabel(
			master=self, text="Home Page ",
			width=100, height=30,
			fg_color="transparent"
		)
		self.home_label.pack(padx=50, pady=20)
		self.credentials_label = CTkLabel(master=self, text="Credentials")
		self.credentials_label.pack(padx=10)

	def set_controller(self, controller):
		self.controller = controller

	def show_menu(self):
		self.pack()


if __name__ == "__main__":
	root = CTk()
	home = Home(root)
	home.pack()
	root.mainloop()
