from customtkinter import CTkFrame, CTkLabel, CTkButton

if __name__ == "__main__":
	from customtkinter import CTk


class Menu(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)

		self.controller = None

		self.collapse = True
		self.items = []

		self.set_items()
		self.set_config()
		self.pack_items()

	def set_controller(self, controller):
		self.controller = controller

	def set_config(self):
		for item in self.items:
			item.get("button").configure(
				text_color = "white",
				fg_color = "transparent",
				hover_color = "#990510",
				corner_radius=0,
				font = ("Open Sans ExtraBold", 24),
			)

	def set_items(self):
		items = (
			("Menu", "🚗", self.toggle_collapse),
			("Home", "🏠", lambda: self.show_page("home")),
			("Stock", "🔎", None),
			("About", "👥", lambda: self.show_page("about")),
		)
		for name, icon, command in items:
			self.create_item(name, icon, command)

	def create_item(self, name:str, icon:str, command):
		item = {
			"button": CTkButton(master=self, text=f"{icon}", command=command, width=5),
			"icon": icon,
			"name": name,
		}
		self.items.append(item)

	def pack_items(self):
		for item in self.items:
			item.get("button").pack(fill="both", ipadx=20, ipady=5)

	def toggle_collapse(self):
		if self.collapse:
			for item in self.items:
				item.get("button").configure(text=f"{item.get('icon')} {item.get('name')}")
		else:
			for item in self.items:
				item.get("button").configure(text=f"{item.get('icon')}")
		self.collapse = not self.collapse

	def show_page(self, name_page):
		self.controller.show_page(name_page)


if __name__ == "__main__":
	root = CTk()
	root.geometry("300x300")
	menu = Menu(root)
	menu.pack()
	root.mainloop()
