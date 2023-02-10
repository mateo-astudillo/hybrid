from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkTextbox
from PIL import Image
from dotenv import load_dotenv
import os

if __name__ == "__main__":
	from customtkinter import CTk

load_dotenv()
PATH_LOGO = os.getenv("PATH_LOGO")
PATH_INFO = os.getenv("PATH_INFO")


class About(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		logo = CTkImage(dark_image=Image.open(PATH_LOGO), size=(300, 150))
		self.widgets = {
			"image": CTkLabel(master=self, text="", image=logo),
			"title": CTkLabel(master=self, text="About Us"),
			"text": CTkLabel(master=self, text=self.get_info()),
		}

		self.set_config()
		self.pack_widgets()

	def set_controller(self, controller):
		self.controller = controller

	def set_config(self):
		self.widgets.get("title").configure(
			font = ("Open Sans Light", 20),
		)
		self.widgets.get("text").configure(
			font = ("Open Sans Light", 16),
			justify = "center",
		)

	def get_info(self):
		with open(PATH_INFO, "r") as f:
			return f.read()

	def pack_widgets(self):
		for widget in self.widgets.values():
			widget.pack(ipadx=10, ipady=10)


if __name__ == "__main__":
	root = CTk()
	about = About(root)
	about.pack()
	root.mainloop()
