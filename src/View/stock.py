from customtkinter import CTkFrame
from View.Stock.filter import Filter
from View.Stock.table import Table

if __name__ == "__main__":
    from customtkinter import CTk


class Stock(CTkFrame):
    def __init__(self,master = None):
        super().__init__(master)
        self.controller = None

        self.frames ={
            "filter" : Filter(self),
            "table" : Table(self)
        }
        self.show_frames()

    def set_controller(self, controller):
        self.controller = controller

    def show_frames(self):
        self.frames.get("filter").pack(side="right", fill="y")
        self.frames.get("table").pack(side="left",fill="both", expand=True)

if __name__ == "__main__":
    root = CTk()
    stock = Stock(root)
    stock.pack()
    root.mainloop()
