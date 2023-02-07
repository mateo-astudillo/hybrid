from customtkinter import CTkFrame, CTkLabel, CTkButton
from time import sleep

if __name__ == "__main__":
	from customtkinter import CTk


class Home(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		self.text = CTkLabel(master=self, text="Home", bg_color="blue", width=200)
		self.text.pack(padx=30, pady=30)

	def set_controller(self, controller):
		self.controller = controller


if __name__ == "__main__":
	root = CTk()
	home = Home(root)
	home.pack()
	root.mainloop()
