    def update_status(self, status, added_by, row_version, item_id):
        self.cursor.execute("update work.statuses set status = ?, added_by = ?, added = getdate(), row_version = ? where item_id = ?;", (status, added_by, row_version, item_id))
