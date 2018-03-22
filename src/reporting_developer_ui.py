"""
CS 4092 Database Design
Homework 3:

Saylee Dharne
"""
import os
import tkinter
import datetime
import time
import pyodbc


class ConfigInterface:
    """ Class to configure connection to database"""
    
    def __init__(self, server='SAYLEE-PC\MSSQLSERVER01'):
        
        server = 'SAYLEE-PC\MSSQLSERVER01' 
        database = 'Reporting_developer' 
        cnxn = pyodbc.connect(
        r'DRIVER={ODBC Driver 13 for SQL Server};'
        r'SERVER='+server+';'
        r'DATABASE='+database+';'
        r'Trusted_Connection=yes;'
        r'QuotedID=Yes;'
        r'AnsiNPW=Yes;'
        )
        self.cursor = cnxn.cursor()
    
    
class ReportingDeveloperUI:
    def __init__(self):
        self.interface = configureConnectionForm()
        
    
    def configureConnectionForm(self):
        print()
    
        

class ReportingDeveloperProcedures:
    def __init__(self, cursor):
        self.cursor = cursor
    
    def view_all_rows(self, tablename):
        self.cursor.execute("select item_id from "+tablename+";")
        table = self.cursor.fetchall()
        for row in self.cursor.columns(table=tablename):
            print (row.column_name)

            

    def add_business_review(self, item_id, approval, reviewer, comment, reviewed_datetime = datetime.datetime.now()):
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into work.business_reviews (item_id, approval,reviewer,comment,reviewed)values(?,?,?,?,?)", 
            (item_id, approval, reviewer, comment, reviewed))
    
    def add_peer_review(self, item_id, approval, comment, reviewer= os.getlogin(), reviewed_datetime = datetime.datetime.now()):
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into work.peer_reviews (item_id, approval,reviewer,comment,reviewed)values(?,?,?,?,?)", 
            (item_id, approval, reviewer, comment, reviewed))

    def update_status(self):
        
        status
        """looooooooooooooooooooooooooong
        declare
        @status varchar(60),
        @last_status_date datetime2;

    set @status = (select [status] from work.items where id = @item_id);
    

    --Check validity of status change
    if not exists (select * from work.status_precedence where status = @status and next_status = @next_status) 
    begin
        declare @err varchar(255) = 'Changes not applied: ' + @next_status + ' is not a valid state following ' + @status + '.  See work.status_precedence for valid status advancements.';
        raiserror(@err,0,-1);
        return -1;
    end
    
    --Get date time of last status update
    set @last_status_date = isnull(
        (   select max(added) 
            from work.status_changes 
            where item_id = @item_id
        ),
        (   select requested
            from work.items
            where id = @item_id
        ));

    --If request has not been reviewed.
    if @status = 'Pending Review' and not exists (select * from work.request_reviews where item_id = @item_id and approval = 1 and reviewed > @last_status_date)
    begin
        raiserror(N'Changes not applied: Request has not been reviewed since set to pending status.',0,-1);
        return -1;
    end

    --If developer has not been assigned.
    if @status = 'Request Reviewed' and not exists (select * from work.assignments where item_id = @item_id and assigned > @last_status_date)
    begin
        raiserror(N'Changes not applied: Developer has not been assigned.',0,-1);
        return -1;
    end

    --If level of effort is not assigned.
    if @status = 'Assigned' and not exists (select * from work.developer_review where item_id = @item_id and added > @last_status_date)
    begin
        raiserror(N'Changes not applied: Level of effort has not been assigned.',0,-1);
        return -1;
    end

    --If work hasn't been peer reviewed.
    if @status = 'Peer Review' and @next_status = 'Business Review' and not exists (select * from work.peer_reviews where item_id = @item_id and approval = 1 and reviewed > @last_status_date)
    begin
        raiserror(N'Changes not applied: No approved peer review after work item last set to Peer Review status.',0,-1);
        return -1;
    end

    --If work hasn't completed business review.
    if @status = 'Business Review' and @next_status = 'Complete' and not exists (select * from work.business_reviews where item_id = @item_id and approval = 1 and reviewed > @last_status_date)
    begin
        raiserror(N'Changes not applied: No approved business review after work item last set to Business Review status.',0,-1);
        return -1;
    end
        
    --Log status.
    insert into work.status_changes (
        item_id,
        previous_status,
        new_status
    ) values (
        @item_id,
        @status,
        @next_status
    );

    --Set current status.
    update work.items set status = @next_status
    where id = @item_id;

    return 0;
end;
GO
        
        """

    def add_request_review(self, item_id, approval, comment, reviewer= os.getlogin(), reviewed_datetime = datetime.datetime.now()):
        reviewed = reviewed_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into request_reviews (item_id, approval,reviewer,comment,reviewed)values(?,?,?,?,?)", 
            (item_id, approval, reviewer, comment, reviewed))

    def add_note(self, item_id, note):
        self.cursor.execute("insert into work.notes (item_id, note)values(?,?)", 
            (item_id, note))

    def add_level_of_effort(self, item_id, estimate, developer= os.getlogin(), added_datetime=datetime.datetime.now()):
        added = added_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("insert into work.level_of_effort (item_id, estimate,develeoper, added)values(?,?,?,?)", 
            (item_id, estimate, develeoper, added))

    def add_developer(self, name, manager):
        self.cursor.execute("insert into work.developers (id, name, manager) values(default,?,?)", 
            (name, manager))
    
    
"""
# Stored procedures not in question
    
    def add_developer_review -> add development request???
        
    
    def add_item -> add report request????
    
    def add_item_xml -> add pending review???
    
    def assign_item  -> add assigned input form???
    
        
        
#Procedures I think I need to add
    def add_report_request()
    
    def add_pending_review()
    
    def add_assigned input form
    
    def add_pending_development input form

    def add_development Input form
    
"""


def main():
    interface = ConfigInterface()
    procedures = ReportingDeveloperProcedures(interface.cursor)
    procedures.view_all_rows('work.peer_reviews')
    procedures.add_peer_review(1, 1, 'good')

if __name__ == "__main__":
    main()


