class CarsManager():
	def __init__(self):
		super().__init__()

		self.controller = None

		# CREATE TABLE "Cars" (
		#	"ID" INTEGER NOT NULL,
		#	"BRAND" TEXT,
		#	"MODEL" TEXT,
		#	"YEAR" INTEGER,
		#	"STOCK" INTEGER,
		#	PRIMARY KEY("ID" AUTOINCREMENT),
		# )

	def set_controller(self, controller):
		self.controller = controller

