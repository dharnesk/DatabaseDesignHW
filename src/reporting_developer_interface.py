import datetime
import pyodbc


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
        connection.autocommit = True

        self.cursor = connection.cursor()


class ReportingDeveloperFormProcedures:

    def __init__(self, cursor):
        self.cursor = cursor
        self.helper = ReportingDeveloperHelperFunctions(cursor)

    def configuration_form_procedure(self):
        print("")

    def report_request_form_procedure(self, name, requester, department, priority, purpose, requirements, work_type):
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
        self.helper.add_item(name, requester, department, priority, purpose, requirements, work_type)

    def pending_review_form_procedure(self, item_id, approval, comment, reviewed, reviewer):
        """
        :param item_id: int fk item id
        :param approval: int 0 or 1 for approval
        :param comment: text for comment
        :param reviewed: datetime of when reviewed
        :param reviewer: fk varchar(30) username of reviewer
        :return: none
        """
        self.helper.add_request_review(item_id, approval, comment, reviewed, reviewer)

    def assign_form_procedure(self, item_id, assignee, assigner=None, assigned=datetime.datetime.now()):
        """
        :param item_id: fk int item id
        :param assignee: fk varchar(30) username of assignee
        :param assigned: datetime of when assigned
        :param assigner: fk varchar(30) username of assigner
        :return: none
        """
        self.helper.assign_item(item_id, assignee, assigned, assigner)
        self.helper.update_status(item_id, 'Assigned')

    def pending_development_form_procedure(self, item_id, estimate, comment, reviewer, est_delivery=None,
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
        self.helper.add_developer_review(item_id, estimate, comment, reviewer, est_delivery, added)
        self.helper.update_status(item_id, 'Pending Development')

    def development_form_procedure(self, item_id):
        """
        :param item_id: fk int from work.items column
        :return: none
        """
        self.helper.update_status(item_id, 'Development')

    def peer_review_form_procedure(self, item_id, approval, comment, reviewer=None, reviewed=datetime.datetime.now(),):
        """
        :param item_id: fk int item id
        :param approval: int 0 or 1
        :param comment: text for comment
        :param reviewed: datetime when reviewed
        :param reviewer: fk fk varchar(30) reviewer username
        :return: none
        """
        self.helper.add_peer_review(item_id, approval, comment, reviewed, reviewer)
        self.helper.update_status(item_id, 'Peer Review')

    def business_review_form_procedure(self, item_id, approval,
                                       reviewer, comment,
                                       reviewed_datetime):
        """
        :param item_id: fk int from work.items column
        :param approval: 0 or 1 integer
        :param reviewer: string name of reviewer
        :param comment: string comment
        :param reviewed: datetime of when reviewed
        :return: none
        """
        self.helper.update_status(item_id, 'Business Review')
        self.helper.add_business_review(item_id, approval, reviewer, comment, reviewed_datetime)

    def update_status_form_procedure(self, item_id, next_status):
        """
        :param item_id: fk int from work.items column
        :param next_status: next status
        :return: none
        """
        # NEXT Status can be Closed or On Hold
        self.helper.update_status(item_id, next_status)

    def request_review_form_procedure(self, item_id, approval, comment, reviewed=datetime.datetime.now()):
        """
        :param item_id: int fk item id
        :param approval: int 0 or 1 approval
        :param comment: text with comments
        :param reviewed: datetime of when reviewed
        :return: none
        """
        self.helper.change_review_pending_request(item_id, approval, comment, reviewed)
        self.helper.update_status(item_id, 'Request Reviewed')

    def add_note_form_procedure(self, item_id, note):
        """
        :param item_id: int fk item id
        :param note: text for note
        :return: none
        """
        self.helper.add_note(item_id, note)

    def add_level_of_effort_form_procedure(self, item_id, estimate, developer=None, added=datetime.datetime.now()):
        """
        :param item_id: fk int from work.items column
        :param estimate: int estimated number of hours
        :param added: datetime of when level of effort was added
        :param developer: string(30 characters) username
        :return: none
        """
        self.helper.add_level_of_effort(item_id, estimate, added, developer)

    def add_developer_form_procedure(self, name, manager):
        """
        :param name: varchar(128) name of developer
        :param manager: varchar(100) name of manager
        :return: none
        """
        self.helper.add_developer(name, manager)


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

    def add_request_review(self, item_id, approval, comment, reviewed=datetime.datetime.now(), reviewer=None):
        """
        :param item_id: fk int item id
        :param approval: int 0 or 1 for approval
        :param comment: text for comment
        :param reviewed: datetime of when reviewed
        :param reviewer: fk varchar(30) username of reviewer
        :return: none
        """
        reviewed = reviewed.strftime('%Y-%m-%d %H:%M:%S')
        if reviewer is None:
            reviewer = self.get_truncated_username()
        self.cursor.execute("""INSERT INTO work.request_reviews (item_id, approval, comment, reviewer, reviewed)
                            VALUES('{}','{}','{}','{}','{}')""".format
                            (item_id, approval, comment, reviewer, reviewed))

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
        self.cursor.execute("""insert into work.developer_review 
                            (item_id, estimate, comment, reviewer, added, est_delivery) 
                            values('{}','{}','{}','{}','{}','{}')""". format(
                            item_id, estimate, comment, reviewer, added, est_delivery))

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
        reviewed = reviewed.strftime('%Y-%m-%d %H:%M:%S')
        if reviewer is None:
            reviewer = self.get_truncated_username()
        self.cursor.execute("""INSERT INTO work.peer_reviews (item_id, approval, comment, reviewer, reviewed) 
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

    def change_review_pending_request(self, item_id, approval, comment, reviewed=datetime.datetime.now()):
        """
        :param item_id: int fk item id
        :param approval: int 0 or 1 approval
        :param comment: text with comments
        :param reviewed: datetime of when reviewed
        :return: none
        """
        reviewed = reviewed.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("""update work.request_reviews
                            Set approval = '{}', comment = '{}', reviewed = '{}'
                            where item_id = '{}'""".format
                            (approval, comment, reviewed, item_id))

    def add_developer(self, name, manager):
        """
        :param name: varchar(128) name of developer
        :param manager: varchar(100) name of manager
        :return: none
        """
        added_by = self.get_truncated_username()
        self.cursor.execute("""insert into work.developers (id,name,manager, added_by) 
                               values ('{}', '{}', '{}', '{}')""".format
                            (added_by, name, manager, added_by))

    def update_status(self, item_id, next_status):
        """
        :param item_id: int fk item id
        :param next_status: varchar(60) fk of next status
        :return: none
        """
        # Get current status of item
        self.cursor.execute("select [status] from work.items where id = '{}'".format(item_id))
        status = self.cursor.fetchall()[0][0]

        # Check if status change exists
        if not self.get_status_exists(status, next_status):
            raise Exception('Changes not applied: ' + next_status + ' is not a valid state following ' + status +
                            '.  See work.status_precedence for valid status advancements.')

        # Get date of last status
        last_status_date = self.get_last_status_date(item_id)

        # Raise exception if trying to update_status without proper updates
        if status == 'Pending Review' and not self.is_request_reviewed(item_id, last_status_date):
            raise Exception('Changes not applied: Request has not been reviewed since set to pending status.')

        if status == 'Request Reviewed' and not self.is_developer_assigned(item_id, last_status_date):
            raise Exception('Changes not applied: Developer has not been assigned.')

        if status == 'Assigned' and not self.is_level_of_effort_assigned(item_id, last_status_date):
            raise Exception('Changes not applied: Level of effort has not been assigned.')

        if status == 'Peer Review' and next_status == 'Business Review' and not self.is_work_peer_reviewed(
                item_id, last_status_date):
            raise Exception('Changes not applied: No approved peer review after work item last set to Peer Review ' +
                            'status.')
        if status == 'Business Review' and next_status == 'Complete' and not self.is_business_review_completed(
                item_id, last_status_date):
            raise Exception('Changes not applied: No approved business review after work item last set to Business ' +
                            'Review status.')

        # Log status
        self.cursor.execute("""insert into work.status_changes 
                            (item_id, previous_status, new_status, added_by) 
                            values ('{}', '{}','{}', '{}');""".format(
                            item_id, status, next_status, self.get_truncated_username()))
        # Set current status
        self.cursor.execute("""update work.items 
                            set status = '{}'
                            where id = '{}';""".format(
                            next_status, item_id))

    # Functions for update_status
    def entry_exists(self, statement):
        self.cursor.execute(statement)
        try:
            exists = self.cursor.fetchall()[0][0]
        except IndexError:
            return False
        return exists is not None

    def get_status_exists(self, status, next_status):
        self.cursor.execute("""(select * from work.status_precedence 
                            where status = '{}' and next_status = '{}')""".format
                            (status, next_status))
        try:
            exists = self.cursor.fetchall()[0][0]
            return True
        except IndexError:
            return False

    def get_last_status_date(self, item_id):
        self.cursor.execute("select max(added) from work.status_changes where item_id = '{}'".format(item_id))
        last_status_update = self.cursor.fetchall()[0][0]
        if last_status_update is None:
            self.cursor.execute("select requested from work.items where id = '{}'".format(item_id))
            last_status_update = self.cursor.fetchall()[0][0]
        return last_status_update

    def is_request_reviewed(self, item_id, last_status_date):
        statement = """select * from work.request_reviews 
                    where item_id = '{}' and approval = 1 and reviewed > '{}'""".format(
                    item_id, last_status_date)
        return self.entry_exists(statement)

    def is_developer_assigned(self, item_id, last_status_date):
        statement = """select * from work.assignments 
                    where item_id = '{}' and assigned > '{}'""".format(
                    item_id, last_status_date)
        return self.entry_exists(statement)

    def is_level_of_effort_assigned(self, item_id, last_status_date):
        statement = """select * from work.developer_review 
                    where item_id = '{}' and added > '{}'""".format(
                    item_id, last_status_date)
        return self.entry_exists(statement)

    def is_work_peer_reviewed(self, item_id, last_status_date):
        statement = """select * from work.peer_reviews 
                    where item_id = '{}' and approval = 1 and reviewed > '{}'""".format(
                    item_id, last_status_date)
        return self.entry_exists(statement)

    def is_business_review_completed(self, item_id, last_status_date):
        statement = """select * from work.business_reviews 
                    where item_id = '{}' and approval = 1 and reviewed > '{}'""".format(
                    item_id, last_status_date)
        return self.entry_exists(statement)


def main():
    interface = ConfigInterface()

    procedures = ReportingDeveloperHelperFunctions(interface.cursor)
    # procedures.update_status(2010, 'Closed')
    # To test:

    # Successfully tested:
    # Testing add_item
    # procedures.add_item("name5", "Saylee Dharne", "IT", "High", "Testing", "Test function add_item", "Analysis")

    # Testing add_business_review
    # procedures.add_business_review(2010, 1, "Saylee Dharne", "Testing")

    # Testing add_developer_review
    # procedures.add_developer_review(2010, 22, "Testing", '',)
    # test_est_delivery = datetime.datetime.now() + datetime.timedelta(days=27)
    # procedures.add_developer_review(2010, 22, "Testing", '', test_est_delivery)
    # procedures.add_developer_review(2010, 22, "Testing", '')
    # procedures.add_developer_review(2010, 22, "Testing", "")

    # Testing add_level_of_effort
    # procedures.add_level_of_effort(2010, 22,)
    # test_added = datetime.datetime.now() - datetime.timedelta(days=2)
    # procedures.add_level_of_effort(2022, 22, test_added)

    # Testing add_note
    # procedures.add_note(2010, "Test note")

    # Testing add_peer_review
    # procedures.add_peer_review(2010, 0, "Test comment", datetime.datetime.now(), None)

    # Testing add_request_review
    # procedures.add_request_review(2010, 0, "Test Comment", datetime.datetime.now(), None)

    # Testing assign_item
    # procedures.assign_item(2010, procedures.get_truncated_username(), datetime.datetime.now(), None)

    # Testing review_request
    # procedures.review_request(2010)

    # Testing update_status

    # Failed tests:


if __name__ == "__main__":
    main()
