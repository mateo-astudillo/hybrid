from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkImage
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


class Menu(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None
		self.collapse = False
		self.widgets = {
			"home": {
				"button": None,
				"name": "Home",
				"image_path": ASSETS_PATH + "home.png",
				"function": lambda: self.show_page("home"),
			},
			"stock": {
				"button": None,
				"name": "Stock",
				"image_path": ASSETS_PATH + "stock.png",
				"function": lambda: self.show_page("stock"),
			},
			"about": {
				"button": None,
				"name": "About",
				"image_path": ASSETS_PATH + "about.png",
				"function": lambda: self.show_page("about"),
			},
		}

		self.set_items()
		# self.set_config()
		self.pack_items()

	def set_controller(self, controller):
		self.controller = controller

	def set_config(self):
		self.configure(fg_color=BACKGROUND)
		for widget in self.widgets.values():
			widget.get("button").configure(
				text_color = BLACK,
				fg_color = BACKGROUND,
				hover_color = WHITE,
				corner_radius = 0,
				font = ("Open Sans Light", 20),
			)

	def set_items(self):
		for widget in self.widgets.values():
			widget.update({
				"button": CTkButton(
					master = self,
					text = widget.get("name"),
					image = CTkImage(
						dark_image = Image.open( widget.get("image_path") ),
						size = (20,20)
					),
					command = widget.get("function"),
					anchor = "w",
					width = 100,
				)
			})

	def pack_items(self):
		for widget in self.widgets.values():
			widget.get("button").pack(fill="both", expand=False)

	def show_page(self, name_page):
		self.controller.show_page(name_page)


if __name__ == "__main__":
	root = CTk()
	root.geometry("300x300")
	menu = Menu(root)
	menu.pack()
	root.mainloop()
