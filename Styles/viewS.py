#colors
BLACK = "#000000"
BACKGROUND = "#8D99AE"
WHITE = "#EDF2F4"
SECONDARY = "#EF233C"
PRIMARY = "#D90429"

class ViewS():
	def __init__(self):
		#self.set_config()

		def set_config(self):
			for page in self.pages.values():
				page.configure(fg_color=BLACK, bg_color=BLACK)

		def show_menu(self):
			# self.pages.get("menu").set_config() #!Poner esto en show_menu()
			pass

		def error(self, message,buttons):
			#message_error =   CTkLabel( #!Agregar a message error las propiedades text_color y fg_color
				# text_color = SECONDARY,
				# fg_color = BLACK,
			#)
			pass