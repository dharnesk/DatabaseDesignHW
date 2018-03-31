
from __future__ import print_function
import datetime
import os
import pyodbc
import time

import tkinter as tk
from tkinter import ttk
from src.reporting_developer_interface import *

#We can change this, but this does work. Simply add functions to establish a connection for each form
#and perform whatever work needs to be done for that forms input/data
s_name = "empty"
def connect_pressed(server_name):
    global s_name
    s_name = server_name
    config = ConfigInterface()
    connection = config.connect(server_name)
    connection.close()

def form_one_connect():
    config = ConfigInterface()
    connection = config.connect(s_name)
    cursor = connection.cursor()
    #do stuff related to form one
    #procedures = ReportingDeveloperFormProcedures(cursor)
    #procedures.helper.add_peer_review(1, 1, "")
    sql_command = ("SELECT status, added_by, added, row_version FROM work.statuses")
    cursor.execute(sql_command)
    results = cursor.fetchone() #test
    connection.close()


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
    def __init__(self, parent):
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
                           command=lambda: connect_pressed(e.get()))
        button.pack(pady=10)



class FormOne(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form One")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: form_one_connect())
        button.pack(pady=10)

class FormTwo(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)

class FormThree(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)


class FormFour(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)

class FormFive(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)

class FormSix(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)

class FormSeven(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)


class FormEight(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)

class FormNine(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)

class FormTen(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)

class FormEleven(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)

class FormTwelve(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form Two")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda:"")
        button.pack(pady=10)

def main():
    """
    Documentation is my passion.
    """
    appUI = AppUI()
    appUI.mainloop()

if __name__ == "__main__":
    main()