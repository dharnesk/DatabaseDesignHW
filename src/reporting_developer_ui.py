"""
CS 4092 Database Design
Homework 3

Group 14:

Samuel Buzas
Saylee Dharne
Miguel Parra
Nicholas Roberts
Tomas Seymour

"""
import os
import tkinter
import datetime
import time
import pyodbc


class ConfigInterface:
    """ Class to configure connection to database"""
    
    def __init__(self, server='SAYLEE-PC\MSSQLSERVER01'):
        
        self.server = server
        database = 'Reporting_developer' 
        connection = pyodbc.connect(
            r'DRIVER={ODBC Driver 13 for SQL Server};'
            r'SERVER='+server+';'
            r'DATABASE='+database+';'
            r'Trusted_Connection=yes;'
            r'QuotedID=Yes;'
            r'AnsiNPW=Yes;'
            )
        self.cursor = connection.cursor()
    
    
class ReportingDeveloperUI:
    def __init__(self):
        # self.interface = self.configureConnectionForm()
        print("Placeholder")
    
    def configure_connection_form(self):
        print("")


class ReportingDeveloperProcedures:

    def __init__(self, cursor):
        self.cursor = cursor
    
    def view_all_rows(self, table_name):
        self.cursor.execute("select item_id from " + table_name + ";")
        table = self.cursor.fetchall()
        for row in self.cursor.columns(table=table_name):
            print(row.column_name)

    def add_business_review(self, item_id, approval,
                            reviewer, comment,
                            reviewed_datetime=datetime.datetime.now()):

        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into work.business_reviews "
                            "(item_id, approval,reviewer,comment,reviewed)"
                            "values(?,?,?,?,?)",
                            (item_id, approval, reviewer, comment, reviewed))
    
    def add_peer_review(self, item_id, approval,
                        comment, reviewer=os.getlogin(),
                        reviewed_datetime=datetime.datetime.now()):
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into work.peer_reviews "
                            "(item_id, approval,reviewer,comment,reviewed)"
                            "values(?,?,?,?,?)",
                            (item_id, approval, reviewer, comment, reviewed))

    def add_request_review(self, item_id, approval,
                           comment, reviewer=os.getlogin(),
                           reviewed_datetime=datetime.datetime.now()):
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into request_reviews "
                            "(item_id, approval,reviewer,comment,reviewed)"
                            "values(?,?,?,?,?)",
                            (item_id, approval, reviewer, comment, reviewed))

    def add_note(self, item_id, note):
        self.cursor.execute("insert into work.notes "
                            "(item_id, note)"
                            "values(?,?)",
                            (item_id, note))

    def add_level_of_effort(self, item_id, estimate,
                            developer=os.getlogin(),
                            added_datetime=datetime.datetime.now()):
        added = added_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into work.level_of_effort "
                            "(item_id, estimate,developer, added)"
                            "values(?,?,?,?)",
                            (item_id, estimate, developer, added))

    def add_developer(self, name, manager):
        self.cursor.execute("insert into work.developers "
                            "(id, name, manager) "
                            "values(default,?,?)",
                            (name, manager))


