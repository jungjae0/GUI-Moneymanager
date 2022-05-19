import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Example")
        self.geometry('300x300')

        self.notebook = ttk.Notebook(self)

        self.Frame1 = Frame1(self.notebook)
        self.Frame2 = Frame2(self.notebook)

        self.notebook.add(self.Frame1, text='Frame1')
        self.notebook.add(self.Frame2, text='Frame2')

        self.notebook.pack()

class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelA = ttk.Label(self, text = "This is on Frame One")
        self.labelA.grid(column=1, row=1)

class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelB = ttk.Label(self, text = "This is on Frame Two")
        self.labelB.grid(column=1, row=1)

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()