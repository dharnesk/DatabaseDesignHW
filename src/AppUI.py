
from __future__ import print_function
import datetime
import os
import pyodbc
import time

import tkinter as tk
from tkinter import ttk
from src.reporting_developer_interface import *

class AppUI(tk.Tk):
    def __init__(self, interface):
        tk.Tk.__init__(self)
        self.interface = interface
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        n = ttk.Notebook(container)
        n.add(ConfigurationPage(self, interface), text='Configuration')
        n.add(FormOne(self), text="Form One")
        n.add(FormTwo(self), text="Form Two")
        n.add(FormThree(self), text="Form Three")
        n.add(FormFour(self), text="Form Four")
        n.add(FormFive(self), text="Form Five")
        n.add(FormSix(self), text="Form Six")
        n.add(FormSeven(self), text="Form Seven")
        n.add(FormEight(self), text="Form Eight")
        n.add(FormNine(self), text="Form Nine")
        n.add(FormTen(self), text="Form Ten")
        n.add(FormEleven(self), text="Form Eleven")
        n.add(FormTwelve(self), text="Form Twelve")
        n.pack()


class ConfigurationPage(ttk.Frame):
    def __init__(self, parent, interface):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Configuration Page")
        label.pack()
        label2 = tk.Label(self, text="Server Name")
        label2.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        label3 = tk.Label(self, text="Driver")
        label3.pack()
        e2 = tk.Entry(self)
        e2.pack()
        e2.focus_set()
        button = tk.Button(self,
                           text="Connect",
                           fg="red",
                           command=lambda: interface.connect(e.get()))
        button.pack(pady=10)


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

class FormThree(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormFour(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormFive(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormSix(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormSeven(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormEight(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormNine(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormTen(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormEleven(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

class FormTwelve(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()

def main():
    """
    Documentation is my passion.
    """
    interface = ConfigInterface()
    appUI = AppUI(interface)
    procedures = ReportingDeveloperFormProcedures(interface.cursor)
    #procedures.view_all_rows('work.peer_reviews')
    # procedures.add_peer_review(1, 1, 'good')
    appUI.mainloop()

if __name__ == "__main__":
    main()