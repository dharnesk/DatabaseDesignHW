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
        self.connection.autocommit = True
        return self.connection

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

    def get_truncated_username(self):
        """
        :return: truncated system user name string
        """
        self.cursor.execute('SELECT SUSER_SNAME()')
        return (self.cursor.fetchall()[0][0])[0:30]

    def add_business_review(self, item_id, approval, reviewer, comment, reviewed=datetime.datetime.now()):
        """
        :param item_id: fk int from work.items column
        :param approval: 0 or 1 integer
        :param reviewer: string name of reviewer
        :param comment: string comment
        :param reviewed: datetime of when reviewed
        :return: none
        """
        added_by = self.get_truncated_username()
        reviewed = reviewed.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("""insert into work.business_reviews 
                            (item_id, approval,reviewer,comment,reviewed, added_by) 
                            values('{}','{}','{}','{}','{}','{}') """.format(
                            item_id, approval, reviewer, comment, reviewed, added_by))

    def add_level_of_effort(self, item_id, estimate, added=datetime.datetime.now(), developer=None):
        """
        :param item_id: fk int from work.items column
        :param estimate: int estimated number of hours
        :param added: datetime of when level of effort was added
        :param developer: string(30 characters) username
        :return: none
        """
        if developer is None:
            developer = self.get_truncated_username()
        added = added.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("""insert into work.level_of_effort
                            (item_id, estimate,developer, added)
                            values('{}','{}','{}','{}')""".format(
                            item_id, estimate, developer, added))

    def add_developer_review(self, item_id, estimate, comment, reviewer, est_delivery=None,
                             added=datetime.datetime.now()):
        """
        :param item_id: fk int from work.items column
        :param estimate: int estimated number of hours
        :param comment: text for comments
        :param reviewer: name of reviewer
        :param est_delivery: datetime estimated delivery time
        :param added: datetime added
        :return: none
        """
        if est_delivery is None:
            est_delivery = datetime.datetime.now() + datetime.timedelta(days=14)
        if not est_delivery or est_delivery < datetime.datetime.now():
            est_delivery = 'NULL'
        else:
            est_delivery = est_delivery.strftime('%Y-%m-%d')
        if not reviewer:
            reviewer = self.get_truncated_username()
        added = added.strftime('%Y-%m-%d %H:%M:%S')
        print(est_delivery)
        self.cursor.execute("""insert into work.developer_review 
                            (item_id, estimate, comment, reviewer, added, est_delivery) 
                            values('{}','{}','{}','{}','{}','{}')""". format(
                            item_id, estimate, comment, reviewer, added, est_delivery))

    def add_item(self, name, requester, department, priority, purpose, requirements, work_type):
        """
        :param name: string name of item
        :param requester: name of item requester
        :param department: department of request
        :param priority: priority
        :param purpose: text about purpose of item
        :param requirements: text about requirements
        :param work_type: fk type of work
        :return: none
        """
        added_by = self.get_truncated_username()
        requested = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("""insert into work.items (name, requested, added_by, requestor, department, priority, 
                            purpose,requirements, type, request_location)
                            values ('{}','{}', '{}', '{}','{}','{}','{}','{}', '{}', '{}')""".format(
                            name, requested, added_by,  requester, department, priority,
                            purpose, requirements, work_type, 'Internal'))

    def add_note(self, item_id, note):
        """
        :param item_id: fk int item id
        :param note: text for note
        :return: none
        """
        added_by = self.get_truncated_username()
        self.cursor.execute("""INSERT INTO work.notes (item_id, note, added_by) VALUES('{}','{}', '{}')""".format(
                            item_id, note, added_by))

    def add_peer_review(self, item_id, approval, comment, reviewed=datetime.datetime.now(), reviewer=None):
        """
        :param item_id: fk int item id
        :param approval: int 0 or 1
        :param comment: text for comment
        :param reviewed: datetime when reviewed
        :param reviewer: fk fk varchar(30) reviewer username
        :return: none
        """

        reviewed = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if reviewer is None:
            reviewer = self.get_truncated_username()
        self.cursor.execute("""INSERT INTO work.peer_reviews (item_id, approval, comment, reviewer, reviewed) 
                            VALUES('{}','{}','{}','{}','{}')""".format
                            (item_id, approval, comment, reviewer, reviewed))

    def add_request_review(self, item_id, approval, comment, reviewed=datetime.datetime.now(), reviewer=None):
        """
        :param item_id: fk int item id
        :param approval: int 0 or 1 for approval
        :param comment: text for comment
        :param reviewed: datetime of when reviewed
        :param reviewer: fk varchar(30) username of reviewer
        :return:
        """
        reviewed = reviewed.strftime('%Y-%m-%d %H:%M:%S')
        if reviewer is None:
            reviewer = self.get_truncated_username()
        self.cursor.execute("""INSERT INTO work.request_reviews (item_id, approval, comment, reviewer, reviewed)
                            VALUES('{}','{}','{}','{}','{}')""".format
                            (item_id, approval, comment, reviewer, reviewed))

    def assign_item(self, item_id, assignee, assigned=datetime.datetime.now(), assigner=None):
        """
        :param item_id: fk int item id
        :param assignee: fk varchar(30) username of assignee
        :param assigned: datetime of when assigned
        :param assigner: fk varchar(30) username of assigner
        :return:
        """
        if assigner is None:
            assigner = self.get_truncated_username()
        assigned = assigned.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("""INSERT INTO work.assignments 
                            (item_id, assignee, assigner, assigned)
                            VALUES('{}','{}','{}','{}')""".format
                            (item_id, assignee, assigner, assigned))


