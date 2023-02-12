from customtkinter import CTkImage, CTkLabel
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
ASSETS_PATH = os.getenv("ASSETS_PATH")
# Colors
BLACK = "#000000"
BACKGROUND = "#8D99AE"
WHITE = "#EDF2F4"
SECONDARY = "#EF233C"
PRIMARY = "#D90429"
PRIMARY_D = "#93021B"

class loginS():
	def __init__(self):
		logo = CTkImage( dark_image=Image.open(ASSETS_PATH + "logo.jpg"), size=(300, 150) )
		self.image = {
					"image": CTkLabel(master=self, image=logo, text = "")
			}
		self.set_config()
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