from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkImage, CTkLabel
from PIL import Image
from dotenv import load_dotenv
import os

if __name__ == "__main__":
	from customtkinter import CTk

load_dotenv()
ASSETS_PATH = os.getenv("ASSETS_PATH")

# Colors
BLACK = "#000000"
BACKGROUND = "#8D99AE"
WHITE = "#EDF2F4"
SECONDARY = "#EF233C"
PRIMARY = "#D90429"
PRIMARY_D = "#93021B"

class Login(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		logo = CTkImage( dark_image=Image.open(ASSETS_PATH + "logo.jpg"), size=(300, 150) )
		self.image = {
			"image": CTkLabel(master=self, image=logo, text = ""),
		}

		self.buttons = {
			"login": CTkButton(master=self, text="Login", command=self.login),
			"register": CTkButton(master=self, text="Register", command=self.register),
		}

		self.entries = {
			"username": CTkEntry(master=self, placeholder_text="Username"),
			"password": CTkEntry(master=self, placeholder_text="Password", show="*")
		}

		self.set_config()
		self.pack_widgets()

	def set_controller(self, controller):
		self.controller = controller

	def set_config(self):
		for entry in self.entries.values():
			entry.configure(
				text_color = BLACK,
				fg_color = WHITE,
				placeholder_text_color = BLACK,
				corner_radius = 27,
				border_width = 0,
				justify = "center",
				font = ("Open Sans ExtraBold", 14),
			)

		for button in self.buttons.values():
			button.configure(
				corner_radius = 27,
				border_width = 0,
				text_color_disabled = "black"
			)

		self.buttons.get("login").configure(
			text_color = BLACK,
			fg_color = PRIMARY,
			hover_color = SECONDARY,
			font = ("Open Sans ExtraBold", 14),
		)

		self.buttons.get("register").configure(
			text_color = WHITE,
			fg_color = BLACK,
			hover_color = SECONDARY,
			font = ("Open Sans Light", 14),
		)

	def pack_widgets(self):
		self.image.get("image").pack()
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