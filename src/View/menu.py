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
		self.configure(bg_color="transparent")
		for item in self.items:
			item.get("button").configure(
				fg_color = "#D9D9D9",
				text_color = "#C92C37",
				corner_radius=0,
				font = ("Open Sans Light", 24),
				hover_color = "#C92C37",
			)
			btn = item.get("name")
			item.get("button").bind("<Enter>",lambda event,arg = btn: self.hover(event,arg))
			item.get("button").bind("<Leave>",lambda event,arg = btn: self.hover(event,arg))

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
			item.get("button").pack(fill="both",ipady=20)

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

	def hover(self,event,arg):
		for item in self.items:
			if item["name"] == arg:
				# if event.widget.winfo_class() == "Label": De esta forma conseguimos el widget que triggerea al evento. es otra forma
				if event.type == "7":
					print(event.type)
					item["button"].configure(fg_color="#C92C37",text_color="black")
				else:
					item["button"].configure(fg_color="#D9D9D9", text_color="#C92C37")

if __name__ == "__main__":
	root = CTk()
	root.geometry("300x300")
	menu = Menu(root)
	menu.pack()
	root.mainloop()
