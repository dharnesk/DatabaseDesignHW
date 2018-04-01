
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
def on_connect_pressed(server_name, config_form):
    global s_name
    s_name = server_name
    config = ConfigInterface()
    connection = config.connect(server_name)
    label_success = tk.Label(config_form, text="Connection Successful")
    label_success.pack()
    connection.close()

def on_submit_report_request():
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

def on_submit_business_review(item_id, approval, reviewer, comment, reviewed):
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_pending_review():
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_assigned_input():
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_pending_development_input():
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_development_input():
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_peer_review_input():
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_update_status_input():
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_request_review_input():
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_add_note_input():
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_add_level_of_effort():
    config = ConfigInterface()
    connection = config.connect(s_name)
    connection.close()

def on_submit_add_developer():
    config = ConfigInterface()
    connection = config.connect(s_name)
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
        n.add(BusinessReviewInputForm(self), text="Business Review")
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
                           command=lambda: on_connect_pressed(e.get(), self))
        button.pack(pady=10)



class FormOne(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Report Request Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_report_request())
        button.pack(pady=10)

class FormTwo(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pending Review Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_pending_review())
        button.pack(pady=10)

class FormThree(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Assigned Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_assigned_input())
        button.pack(pady=10)


class FormFour(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pending Development Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_pending_development_input())
        button.pack(pady=10)

class FormFive(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Development Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_development_input())
        button.pack(pady=10)

class FormSix(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Peer Review Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_peer_review_input())
        button.pack(pady=10)

class BusinessReviewInputForm(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Business Review Input Form")
        label.pack()
        label2 = tk.Label(self, text="Item ID")
        label2.pack()
        item_id = tk.Entry(self)
        item_id.pack()
        item_id.focus_set()
        label3 = tk.Label(self, text="Approval")
        label3.pack()
        approval = tk.Entry(self)
        approval.pack()
        approval.focus_set()
        label4 = tk.Label(self, text="Reviewer")
        label4.pack()
        reviewer = tk.Entry(self)
        reviewer.pack()
        reviewer.focus_set()
        label5 = tk.Label(self, text="Comment")
        label5.pack()
        comment = tk.Entry(self)
        comment.pack()
        comment.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_business_review(item_id, approval, reviewer, comment, ""))
        button.pack(pady=10)




class FormEight(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Update Status Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_update_status_input())
        button.pack(pady=10)

class FormNine(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Request Review Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_request_review_input())
        button.pack(pady=10)

class FormTen(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Note Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_add_note_input())
        button.pack(pady=10)

class FormEleven(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Level of Effort Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_add_level_of_effort())
        button.pack(pady=10)

class FormTwelve(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add a Developer Input Form")
        label.pack()
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_add_developer())
        button.pack(pady=10)

def main():
    """
    Documentation is my passion.
    """
    appUI = AppUI()
    appUI.mainloop()

if __name__ == "__main__":
    main()