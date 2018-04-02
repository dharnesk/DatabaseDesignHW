    def update_status(self, status, item_id):
        self.cursor.execute("update work.statuses set status = ? where item_id = ?;", (status, item_id))
