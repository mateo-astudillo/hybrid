from customtkinter import CTkFrame, CTkLabel, CTkButton

if __name__ == "__main__":
	from customtkinter import CTk


class Menu(CTkFrame):
	def __init__(self, master=None):
		super().__init__(master)
		self.configure(width=300, height=700)

		self.controller = None

		self.collapse = True
		self.menu_items = []
		self.menu_labels = []

		self.set_items()
		self.pack_menu_items()

	def set_controller(self, controller):
		self.controller = controller

	def set_items(self):
		items = [
			("Menu", "🚗", self.toggle_menu_collapse),
			("Home", "🏠", lambda: self.show_page("home") ),
			("Stock", "🔎", None),
			("About", "👥", lambda: self.show_page("about")),
		]
		for name, icon, comm in items:
			self.create_menu_item(name, icon, comm)

	def create_menu_item(self, name:str, icon:str, comm):
		frm = CTkFrame(master=self)
		i = CTkButton(master=frm, text=icon, command=comm, width=10)
		n = CTkButton(master=frm, text=name, command=comm)
		i.pack(padx=10, pady=5, side="left")
		self.menu_labels.append(n)
		self.menu_items.append(frm)

	def pack_menu_items(self):
		for item in self.menu_items:
			item.pack(padx=10, pady=10)

	def toggle_menu_collapse(self):
		if self.collapse:
			for label in self.menu_labels:
				label.pack(padx=10, pady=5, side="right")
		else:
			for label in self.menu_labels:
				label.pack_forget()
		self.collapse = not self.collapse

	def show_page(self, name_page):
		self.controller.show_page(name_page)


if __name__ == "__main__":
	root = CTk()
	menu = Menu(root)
	menu.pack()
	root.mainloop()
