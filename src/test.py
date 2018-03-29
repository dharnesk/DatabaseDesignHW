
import tkinter as tk
from tkinter import ttk


class AppUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        n = ttk.Notebook(container)
        n.add(ConfigurationPage(self), text='Configuration')
        n.add(FormOne(self), text="Form One")
        n.add(FormTwo(self), text="Form Two")
        n.pack()


class ConfigurationPage(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Configuration Page")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormOne(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form One")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormTwo(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()


app = AppUI()
app.mainloop()

