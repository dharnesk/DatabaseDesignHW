"""
Application UI
This Module handles the application's User Interface.
This is done using mutiple forms in a Tkinter Notebook.
"""
from __future__ import print_function
import datetime
import os
import pyodbc
import time

import tkinter as tk
from tkinter import ttk
from src.reporting_developer_interface import *

#We can change this,but this does work. Simply add functions to establish a connection for each form
#and perform whatever work needs to be done for that forms input/data

CONNECT_ATTEMPT = 0
def on_connect_pressed(server_name, label_success, label_failed, driver, parent):
    """
    Attempts to make a connection to the supplied DB server
    """
    global CONNECT_ATTEMPT
    parent.set_server_name(server_name)
    config = ConfigInterface()
    try:
        label_failed.pack_forget()
        if server_name != "" and CONNECT_ATTEMPT == 0:
            connection = config.connect(server_name, driver)
            label_success.pack()
            CONNECT_ATTEMPT += 1
            connection.close()
    except:
        CONNECT_ATTEMPT = 0
        label_success.pack_forget()
        label_failed.pack()

#TODO
def on_submit_report_request(parent, name, requester, department, priority, purpose, requirements, work_type):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.report_request_form_procedure(name, requester, department, priority, purpose, requirements, work_type)
    connection.close()

def on_submit_business_review(item_id, approval, reviewer, comment, parent):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.business_review_form_procedure(item_id, approval, reviewer, comment)
    connection.close()
#TODO
def on_submit_pending_review(parent, item_id, approval, comment, reviewer):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.pending_review_form_procedure(item_id, approval, comment, reviewer)
    connection.close()

def on_submit_assigned_input(parent, item_id, assignee, assigner):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.assign_form_procedure(item_id, assignee, assigner)
    connection.close()


def on_submit_pending_development_input(parent, item_id, estimate, comment, reviewer):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.pending_development_form_procedure(item_id, estimate, comment, reviewer)
    connection.close()


def on_submit_add_developer(parent, name, manager):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.add_developer_form_procedure(name, manager)
    connection.close()

def on_submit_peer_review_input(parent, item_id, approval, comment):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.peer_review_form_procedure(item_id, approval, comment)
    connection.close()

#TODO
def on_submit_update_status_input(parent, item_id, next_status):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.update_status_form_procedure(item_id, next_status)
    connection.close()

def on_submit_request_review_input(item_id, approval, comment, parent):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.request_review_form_procedure(item_id, approval, comment)
    connection.close()

def on_submit_add_note_input(item_id, note, parent):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.add_note_form_procedure(item_id, note)
    connection.close()

def on_submit_add_level_of_effort(parent, item_id, estimate, developer):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.add_level_of_effort_form_procedure(item_id, estimate, developer)
    connection.close()

def on_submit_development_input(item_id, parent):
    config = ConfigInterface()
    connection = config.connect(parent.get_server_name())
    procedures = ReportingDeveloperFormProcedures(connection.cursor())
    procedures.development_form_procedure(item_id)
    connection.close()


class AppUI(tk.Tk):
    """
    Documentation is my Dream.
    """
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.server_name = ""
        self.winfo_toplevel().title("Reporting Developer GUI")

        # Initialize the Notebook and all of its Forms
        notebook = ttk.Notebook(container)
        notebook.add(ConfigurationPage(self), text='Configuration')
        notebook.add(FormOne(self), text="Report Request")
        notebook.add(FormTwo(self), text="Pending Review")
        notebook.add(FormThree(self), text="Assigned Input")
        notebook.add(FormFour(self), text="Pending Development")
        notebook.add(FormFive(self), text="Add Developer")
        notebook.add(FormSix(self), text="Peer Review")
        notebook.add(BusinessReviewInputForm(self), text="Business Review")
        notebook.add(FormEight(self), text="Update Status")
        notebook.add(FormNine(self), text="Request Review")
        notebook.add(FormTen(self), text="Add Note")
        notebook.add(FormEleven(self), text="Level of Effort")
        notebook.add(FormTwelve(self), text="Development Input")
        notebook.pack()

    def set_server_name(self, server_name):
        """
        Get Server Name
        """
        self.server_name = server_name

    def get_server_name(self):
        """
        Set Server Name
        """
        return self.server_name


class ConfigurationPage(ttk.Frame):
    """
    Documentation is my Dream.
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Configuration Page")
        label.pack(pady=10)

        label2 = tk.Label(self, text="Server Name")
        label2.pack()

        e = tk.Entry(self)
        e.pack()
        e.focus_set()

        label3 = tk.Label(self, text="Driver")
        label3.pack()

        e2 = tk.Entry(self)
        e2.insert(0, 'ODBC Driver 13 for SQL Server')
        e2.pack()
        e2.focus_set()

        label_success = tk.Label(self, text="Connection Successful")
        label_failed = tk.Label(self, text="Connection Failed")
        button = tk.Button(self,
                           text="Connect",
                           fg="red",
                           command=lambda: on_connect_pressed(e.get(),
                                                              label_success,
                                                              label_failed, e2.get(),
                                                              parent)
                          )
        button.pack(pady=10)


#TODO: Me
class FormOne(ttk.Frame):
    """
    :param int item_id:
    :param bool approval:
    :param char comment:
    :param date reviewed on:
    :param char reviewer:
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)  #name, requester, department, priority, purpose, requirements, work_type
        #Form Title
        label = tk.Label(self, text="Report Request Input Form")
        label.pack(pady=10)
        # Item ID
        label2 = tk.Label(self, text="Name")
        label2.pack()
        name = tk.Entry(self)
        name.pack()
        name.focus_set()

        # Approval
        label3 = tk.Label(self, text="Requester")
        label3.pack()
        requester = tk.Entry(self)
        requester.pack()
        requester.focus_set()

        #Comment
        label4 = tk.Label(self, text="Department")
        label4.pack()
        department = tk.Entry(self)
        department.pack()
        department.focus_set()

        label5 = tk.Label(self, text="Priority")
        label5.pack()
        priority = tk.Entry(self)
        priority.pack()
        priority.focus_set()

        label6 = tk.Label(self, text="Purpose")
        label6.pack()
        purpose = tk.Entry(self)
        purpose.pack()
        purpose.focus_set()

        label7 = tk.Label(self, text="Requirements")
        label7.pack()
        requirements = tk.Entry(self)
        requirements.pack()
        requirements.focus_set()

        label18 = tk.Label(self, text="Work Type")
        label18.pack()
        work_type = tk.Entry(self)
        work_type.pack()
        work_type.focus_set()

#        #entry_date
#        label5 = tk.Label(self, text="Review Date")
#        label5.pack()
#        entry_date = tk.Entry(self)
#        entry_date.pack()
#        entry_date.focus_set()

        # Reviewer
        label6 = tk.Label(self, text="Reviewer")
        label6.pack()
        reviewer = tk.Entry(self)
        reviewer.pack()
        reviewer.focus_set()
        # Submit Button
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_report_request(parent, name.get(), requester.get(),
                                                                    department.get(), priority.get(),
                                                                    purpose.get(), requirements.get(), work_type.get()))

        button.pack(pady=10)

#TODO: me tooo
class FormTwo(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pending Review Input Form")
        label.pack()

        label1 = tk.Label(self, text="Item ID")
        label1.pack()

        item_id = tk.Entry(self)
        item_id.pack()
        item_id.focus_set()

        label2 = tk.Label(self, text="Approval 0/1")
        label2.pack()

        approval = tk.Entry(self)
        approval.pack()
        approval.focus_set()

        label3 = tk.Label(self, text="Comment")
        label3.pack()

        comment = tk.Entry(self)
        comment.pack()
        comment.focus_set()

        label4 = tk.Label(self, text="Reviewer")
        label4.pack()

        reviewer = tk.Entry(self)
        reviewer.pack()
        reviewer.focus_set()

        # Submit Button
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_pending_review(parent, item_id.get(),
                                                                    approval.get(), comment.get(), reviewer.get())
                          )
        button.pack(pady=10)

class FormThree(ttk.Frame):
    """
    :param int item_id
    :param char assigned
    :param char assigner
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        #Form Title
        label1 = tk.Label(self, text="Assigned Input Form")
        label1.pack()
        label2 = tk.Label(self, text="Report ID")
        label2.pack()
        item_id = tk.Entry(self)
        item_id.pack()
        item_id.focus_set()
        # Asignee
        label3 = tk.Label(self, text="Assignee")
        label3.pack()
        assignee = tk.Entry(self)
        assignee.pack()
        assignee.focus_set()
        # Asignee
        label5 = tk.Label(self, text="Assigner")
        label5.pack()
        assigner = tk.Entry(self)
        assigner.pack()
        assigner.focus_set()
        # Submit Button
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_assigned_input(parent, item_id.get(),
                                                                    assignee.get(), assigner.get()))

        button.pack(pady=10)

#TODO: MEEEEEEEE
class FormFour(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Pending Development Input Form")
        label.pack()

        label2 = tk.Label(self, text="Item ID")
        label2.pack()

        item_id = tk.Entry(self)
        item_id.pack()
        item_id.focus_set()

        label3 = tk.Label(self, text="Estimate")
        label3.pack()

        estimate = tk.Entry(self)
        estimate.pack()
        estimate.focus_set()

        label4 = tk.Label(self, text="Comment")
        label4.pack()

        comment = tk.Entry(self)
        comment.pack()
        comment.focus_set()

        label5 = tk.Label(self, text="Reviewer")
        label5.pack()

        reviewer = tk.Entry(self)
        reviewer.pack()
        reviewer.focus_set()


        #Submit Button
        button = tk.Button(self,
                           text="Submit",
                       fg="red",
                           command=lambda: on_submit_pending_development_input(parent, item_id.get(),
                                                                               estimate.get(), comment.get(), reviewer.get())
                          )
        button.pack(pady=10)



class FormFive(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Add Developer Input Form")
        label.pack(pady=10)

        label2 = tk.Label(self, text="Name")
        label2.pack()
        name = tk.Entry(self)
        name.pack()
        name.focus_set()

        label3 = tk.Label(self, text="Manager")
        label3.pack()
        manager = tk.Entry(self)
        manager.pack()
        manager.focus_set()

        #Submit Button
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_add_developer(parent, name.get(), manager.get())
                          )
        button.pack(pady=10)

class FormSix(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Peer Review Input Form")
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

        label5 = tk.Label(self, text="Comment")
        label5.pack()

        comment = tk.Entry(self)
        comment.pack()
        comment.focus_set()

        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_peer_review_input(parent, item_id.get(), approval.get(), comment.get())
                          )
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

        #Submit button
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_business_review(item_id.get(), approval.get(), reviewer.get(), comment.get(), parent)
                          )
        button.pack(pady=10)



#TODO: Me
class FormEight(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Update Status Input Form")
        label.pack()

        label2 = tk.Label(self, text="item ID")
        label2.pack()

        item_id = tk.Entry(self)
        item_id.pack()
        item_id.focus_set()

        label3 = tk.Label(self, text="Next Status (Complete/Closed)")
        label3.pack()

        next_status = tk.Entry(self)
        next_status.pack()
        next_status.focus_set()

        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_update_status_input(parent, item_id.get(), next_status.get()))
        button.pack(pady=10)

class FormNine(ttk.Frame):
    """
    :param int item_id:
        forigen key
    :param bool approval:
    :param string comment:
        No limit
    :param datetime reviewed:
        Defualt = current time, nullable
    :param string reviewer:
        30 character limit,
        default = current user, nullable
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Request Review Input Form")  #item_id, approval, comment, reviewer
        label.pack()

        label2 = tk.Label(self, text="Item ID")
        label2.pack()

        item_id = tk.Entry(self)
        item_id.pack()
        item_id.focus_set()

        label3 = tk.Label(self, text="Approval 1/0")
        label3.pack()

        approval = tk.Entry(self)
        approval.pack()
        approval.focus_set()

        label5 = tk.Label(self, text="Comment")
        label5.pack()

        comment = tk.Entry(self)
        comment.pack()
        comment.focus_set()


        # Submit Button
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_request_review_input(item_id.get(), approval.get(),
                                                            comment.get(), parent))
        button.pack(pady=10)

class FormTen(ttk.Frame):
    """
    :param int item_id:
    :param string comment: No limit
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Note Input Form")
        label.pack(pady=10)

        label2 = tk.Label(self, text="Item ID")
        label2.pack()

        item_id = tk.Entry(self)
        item_id.pack()
        item_id.focus_set()

        label3 = tk.Label(self, text="Note")
        label3.pack()

        note = tk.Entry(self)
        note.pack()
        note.focus_set()

        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_add_note_input(item_id.get(), note.get(), parent))
        button.pack(pady=10)

class FormEleven(ttk.Frame):
    """
    :param int item_id:
    :param int estimate: Work hour estimate 8h = 1 day 40h=1w
    :param datetime add_date:
        Can be null
        When the level_of_effort was added, default = CurrTime
    :param string developer:
        Can be null
        30 characters, restricted
        default = username of person
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="Add Level of Effort Input Form")
        label1.pack(pady=10)
        # Item_ID Entry
        label1 = tk.Label(self, text="Request ID Number")
        label1.pack()
        item_id = tk.Entry(self)
        item_id.pack()
        item_id.focus_set()

        # Estimate Entry
        label2 = tk.Label(self, text="Effort Estimate")
        label2.pack()
        estimate = tk.Entry(self)
        estimate.pack()
        estimate.focus_set()

        # Developer Entry
        label4 = tk.Label(self, text="Developer")
        label4.pack()
        developer = tk.Entry(self)
        developer.pack()
        developer.focus_set()

        # Submit Button
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_add_level_of_effort(parent, item_id.get(),
                                                                         estimate.get(),
                                                                         developer.get()
                                                                        )
                          )

        button.pack(pady=10)

class FormTwelve(ttk.Frame):
    """
    TODO: Needs Params
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Development Input Form")
        label.pack()

        label2 = tk.Label(self, text="Item ID")
        label2.pack()

        item_id = tk.Entry(self)
        item_id.pack()
        item_id.focus_set()

        #Submit Button
        button = tk.Button(self,
                           text="Submit",
                           fg="red",
                           command=lambda: on_submit_development_input(item_id.get(), parent)
                          )
        button.pack(pady=10)

def main():
    """
    Documentation is my passion.
    """
    appUI = AppUI()
    appUI.mainloop()

if __name__ == "__main__":
    main()