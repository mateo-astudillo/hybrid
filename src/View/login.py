from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkImage, CTkLabel
from PIL import Image
from dotenv import load_dotenv
import os

if __name__ == "__main__":
	from customtkinter import CTk

load_dotenv()
PATH_LOGO = os.getenv("PATH_LOGO")

class Login(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		logo = CTkImage( dark_image=Image.open(PATH_LOGO), size=(300, 150) )
		self.image = CTkLabel(master=self, image=logo, text = "")


		self.entrys = {
			"username": CTkEntry(master=self, placeholder_text="Username"),
			"password": CTkEntry(master=self, placeholder_text="Password", show="*"),
		}
	
		#! Buttons
		self.login_button = CTkButton(
			master = self,
			text = "Login",
			text_color = "black",
			fg_color = "#C92C37",
			hover_color = "#990510",
			font = ("Open Sans ExtraBold", 14),
			command = self.login,
		)

		self.register_button = CTkButton(
			master = self,
			text = "Register",
			text_color = "#fff",
			fg_color = "black",
			hover_color = "#C92C37",
			font = ("Open Sans Light", 14),
			command = self.register,
		)

		self.set_config()

		self.widgets = [
			self.login_button,
			self.register_button,
		]

		self.pack_widgets()

	def set_controller(self, controller):
		self.controller = controller

	def set_config(self):
		self.configure(fg_color="black")

		for entry in self.entrys.values():
			entry.configure(
				corner_radius=27,
				border_width=0,
				placeholder_text_color="black",
				text_color="black",
				fg_color="#fff",
				justify="center",
				font=("Open Sans ExtraBold", 14),
			)

		for button in [self.login_button, self.register_button]:
			button.configure(
				corner_radius=27,
				border_width=0,
			)

	def pack_widgets(self):
		self.image.pack()
		for entry in self.entrys.values():
			entry.pack(padx=7, pady=15, ipadx=20)
		for button in self.widgets:
			button.pack(padx=7, pady=15, ipadx=20)


	def login(self):
		username = self.entrys.get("username")
		password = self.entrys.get("password")
		self.controller.login(username.get(), password.get())

	def register(self):
		pass


if __name__ == "__main__":
	root = CTk()
	login = Login(root)
	login.pack()
	root.mainloop()
