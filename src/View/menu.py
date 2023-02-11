from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkImage
from PIL import Image
from dotenv import load_dotenv
import os

if __name__ == "__main__":
	from customtkinter import CTk

load_dotenv()
ASSETS_PATH = os.getenv("ASSETS_PATH")


class Menu(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		self.collapse = True
		self.widgets = {
			"menu": {
				"button": None,
				"name": "menu",
				"icon": CTkImage( dark_image=Image.open(ASSETS_PATH + "menu.png"), size=(20,20)),
				"function": self.toggle_collapse
			},
			"home": {
				"button": None,
				"name": "Home",
				"icon": CTkImage( dark_image=Image.open(ASSETS_PATH + "home.png"), size=(20,20) ),
				"function": lambda: self.show_page("home")
			},
			"stock": {
				"button": None,
				"name": "Stock",
				"icon": CTkImage( dark_image=Image.open(ASSETS_PATH + "stock.png"), size=(20,20) ),
				"function": lambda: self.show_page("stock")
			},
			"about": {
				"button": None,
				"name": "About",
				"icon": CTkImage( dark_image=Image.open(ASSETS_PATH + "about.png"), size=(20,20) ),
				"function": lambda: self.show_page("about")
			},
		}

		self.set_items()
		self.set_config()
		self.pack_items()

	def set_controller(self, controller):
		self.controller = controller

	def set_config(self):
		for widget in self.widgets.values():
			widget.get("button").configure(
				# width = 20,
				
				fg_color = "white",
				hover_color = "gray",
				corner_radius=0,
				font = ("Open Sans Light", 24),
				compound = "left",
				anchor = "w"
			)

	def set_items(self):
		for widget in self.widgets.values():
			widget.update( {
				"button": CTkButton(
					master = self,
					image = widget.get("icon"),
					text = "",
					command = widget.get("function")
				)
			} )


	def pack_items(self):
		for widget in self.widgets.values():
			widget.get("button").pack(fill="both", ipady=5)

	def toggle_collapse(self):
		if self.collapse:
			for widget in self.widgets.values():
				widget.get("button").configure(text=widget.get("name"))
		else:
			for widget in self.widgets.values():
				widget.get("button").configure(text="")
		self.collapse = not self.collapse

	def show_page(self, name_page):
		self.controller.show_page(name_page)


if __name__ == "__main__":
	root = CTk()
	root.geometry("300x300")
	menu = Menu(root)
	menu.pack()
	root.mainloop()
