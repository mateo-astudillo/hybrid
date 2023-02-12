from customtkinter import CTkFrame, CTkLabel, CTkImage
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
STATIC_PATH = os.getenv("STATIC_PATH")
ASSETS_PATH = os.getenv("ASSETS_PATH")


class About():
	def __init__(self):

		logo = CTkImage(dark_image=Image.open(ASSETS_PATH + "logo.jpg"), size=(300, 150))
		self.widgets = {
			"image": CTkLabel(master=self, text="", image=logo),
		}

		#self.set_config()
		def set_config(self):
			self.widgets.get("title").configure(
				font = ("Open Sans Light", 20),
			)
			self.widgets.get("text").configure(
				font = ("Open Sans Light", 16),
				justify = "center",
			)
