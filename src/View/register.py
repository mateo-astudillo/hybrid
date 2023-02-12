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


class Register(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		logo = CTkImage( dark_image=Image.open(ASSETS_PATH + "logo.jpg"), size=(300, 150) )
		self.image = {
			"image": CTkLabel(master=self, image=logo, text = ""),
		}

		self.buttons = {
			"register": CTkButton(master=self, text="Register", command=self.register),
			"cancel": CTkButton(master=self, text="Cancel", command=self.cancel),
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
				text_color_disabled = PRIMARY_D
			)

		self.buttons.get("register").configure(
			text_color = BLACK,
			fg_color = PRIMARY,
			hover_color = SECONDARY,
			font = ("Open Sans ExtraBold", 14),
		)

		self.buttons.get("cancel").configure(
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

	def register(self):
		username = self.entries.get("username")
		password = self.get("password")
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
