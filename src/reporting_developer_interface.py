from __future__ import print_function
import datetime
import os
import pyodbc
import time

from src.AppUI import *


class ConfigInterface:
    """ Class to configure connection to database"""
    def __init__(self):
        self.database = 'Reporting_developer'
        self.connection = ""

    def connect(self, server_name):
        self.connection = pyodbc.connect(
            r'DRIVER={ODBC Driver 13 for SQL Server};'
            r'SERVER=' + server_name + ';'
            r'DATABASE=' + self.database + ';'
            r'Trusted_Connection=yes;'
            r'QuotedID=Yes;'
            r'AnsiNPW=Yes;'
        )
        return self.connection

class ReportingDeveloperFormProcedures:
    """
    Documentation is my passion
    """

    def __init__(self, cursor):
        self.cursor = cursor
        self.helper = ReportingDeveloperHelperFunctions(cursor)

    def set_cursor(self, cursor):
        self.cursor = cursor

    def get_cursor(self):
        return self.cursor

    def configuration_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def report_request_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def pending_review_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def assign_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def pending_development_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def development_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def peer_review_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def business_review_form_procedure(self, item_id, approval,
                                       reviewer, comment,
                                       reviewed_datetime):
        """
        Documentation is my passion.
        """
        self.helper.add_business_review(item_id, approval,
                                        reviewer, comment,
                                        reviewed_datetime)
        print("")

    def update_status_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def request_review_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def add_note_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def add_level_of_effort_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")

    def add_developer_form_procedure(self):
        """
        Documentation is my passion.
        """
        print("")


class ReportingDeveloperHelperFunctions:
    """Class to add stored procedures and other helpful functions """
    def __init__(self, cursor):
        self.cursor = cursor

    def view_all_rows(self, table_name):
        """
        function for testing
        :param table_name: Name of table for query
        :return: all items in table
        """
        self.cursor.execute("select item_id from " + table_name + ";")
        table = self.cursor.fetchall()
        for row in self.cursor.columns(table=table_name):
            print(row.column_name)

    def add_business_review(self, item_id, approval,
                            reviewer, comment,
                            reviewed_datetime=datetime.datetime.now()):
        """
        Documentation is my passion.
        """
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into work.business_reviews "
                            "(item_id, approval,reviewer,comment,reviewed)"
                            "values(?,?,?,?,?)",
                            (item_id, approval, reviewer, comment, reviewed))

    def add_peer_review(self, item_id, approval,
                        comment, reviewer=os.getlogin(),
                        reviewed_datetime=datetime.datetime.now()):
        """
        Documentation is my passion.
        """
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into work.peer_reviews "
                            "(item_id, approval,reviewer,comment,reviewed)"
                            "values(?,?,?,?,?)",
                            (item_id, approval, reviewer, comment, reviewed))

    def add_request_review(self, item_id, approval,
                           comment, reviewer=os.getlogin(),
                           reviewed_datetime=datetime.datetime.now()):
        """
        Documentation is my passion.
        """
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into request_reviews "
                            "(item_id, approval,reviewer,comment,reviewed)"
                            "values(?,?,?,?,?)",
                            (item_id, approval, reviewer, comment, reviewed))

    def add_note(self, item_id, note):
        """
        Documentation is my passion.
        """
        self.cursor.execute("insert into work.notes "
                            "(item_id, note)"
                            "values(?,?)",
                            (item_id, note))

    def add_level_of_effort(self, item_id, estimate,
                            developer=os.getlogin(),
                            added_datetime=datetime.datetime.now()):
        """
        Documentation is my passion.
        """
        added = added_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into work.level_of_effort "
                            "(item_id, estimate,developer, added)"
                            "values(?,?,?,?)",
                            (item_id, estimate, developer, added))

    def add_developer(self, name, manager):
        """
        Documentation is my passion.
        """
        self.cursor.execute("insert into work.developers "
                            "(id, name, manager) "
                            "values(default,?,?)",
                            (name, manager))


