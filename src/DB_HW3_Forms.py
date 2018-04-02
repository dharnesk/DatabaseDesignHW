import os
import tkinter
import datetime
import time
import pyodbc


class ConfigInterface:
    """Class to configure connection to database"""
    
    def __init__(self, server='Miguepiwi-PC\Miguepiwi'):
        
        server = 'Miguepiwi-PC\Miguepiwi' 
        database = 'Reporting_developer' 
        cnxn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER='+server+';'
        r'DATABASE='+database+';'
        r'Trusted_Connection=yes;'
        r'QuotedID=Yes;'
        r'AnsiNPW=Yes;'
        )
        self.cursor = cnxn.cursor()
        


class ReportingDeveloperProcedures:
    def __init__(self, cursor):
        self.cursor = cursor
        
    def add_note(self, item_id, note):
        self.cursor.execute("INSERT INTO work.notes (item_id, note) VALUES(?,?)", 
            (item_id, note))

    def add_peer_review(self, item_id, approval, comment, reviewer = os.getlogin(), reviewed_datetime = datetime.datetime.now()):
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("INSERT INTO work.add_peer_review (item_id, approval, comment, reviewer, reviewed) VALUES(?,?,?,?,?)", 
            (item_id, approval, comment, reviewer, reviewed))

    def add_request_review(self, item_id, approval, comment, reviewer = os.getlogin(), reviewed_datetime = datetime.datetime.now()):
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("INSERT INTO work.add_request_review (item_id, approval, comment, reviewer, reviewed)VALUES(?,?,?,?,?)", 
            (item_id, approval, comment, reviewer, reviewed))

    def assign_item(self, item_id, assignee, assigner = os.getlogin(), assigned_datetime = datetime.datetime.now()):
        assigned = assigned_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("INSERT INTO work.assign_item (item_id, assignee, assigner, assigned) VALUES(?,?,?,?)",
                            (item_id, assignee, assigner, assigned))
        
def main():
    
    add_note(1, "My note")
