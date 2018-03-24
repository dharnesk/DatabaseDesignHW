import datetime
import os
import pyodbc
import time


class ConfigInterface:
    """ Class to configure connection to database"""

    def __init__(self, server='SAYLEE-PC\MSSQLSERVER01'):
        self.server = server
        database = 'Reporting_developer'
        connection = pyodbc.connect(
            r'DRIVER={ODBC Driver 13 for SQL Server};'
            r'SERVER=' + server + ';'
            r'DATABASE=' + database + ';'
            r'Trusted_Connection=yes;'
            r'QuotedID=Yes;'
            r'AnsiNPW=Yes;'
        )
        self.cursor = connection.cursor()


class ReportingDeveloperFormProcedures:

    def __init__(self, cursor):
        self.cursor = cursor
        self.helper = ReportingDeveloperHelperFunctions(cursor)

    def configuration_form_procedure(self):
        print("")

    def report_request_form_procedure(self):
        print("")

    def pending_review_form_procedure(self):
        print("")

    def assign_form_procedure(self):
        print("")

    def pending_development_form_procedure(self):
        print("")

    def development_form_procedure(self):
        print("")

    def peer_review_form_procedure(self):
        print("")

    def business_review_form_procedure(self, item_id, approval,
                                       reviewer, comment,
                                       reviewed_datetime):
        self.helper.add_business_review(item_id, approval,
                                            reviewer, comment,
                                            reviewed_datetime)
        print("")

    def update_status_form_procedure(self):
        print("")

    def request_review_form_procedure(self):
        print("")

    def add_note_form_procedure(self):
        print("")

    def add_level_of_effort_form_procedure(self):
        print("")

    def add_developer_form_procedure(self):
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


def main():
    interface = ConfigInterface()
    procedures = ReportingDeveloperProcedures(interface.cursor)
    procedures.view_all_rows('work.peer_reviews')
    # procedures.add_peer_review(1, 1, 'good')


if __name__ == "__main__":
    main()
