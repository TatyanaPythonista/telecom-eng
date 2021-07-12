import sqlite3 as database


class DataBaseRecoder:

    def __init__(self, number_of_participant, link_id, time_for_db, number_of_group,
                 table_name='tracker', db_name='tracker_database.db'):
        self.db_name = db_name
        self.table_name = table_name
        self.number_of_participant = number_of_participant
        self.link_id = link_id
        self.time_for_db = time_for_db
        self.number_of_group = number_of_group

    def create_db(self):
        with database.connect(self.db_name) as connection:
            cursor = connection.cursor()

            cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (number_of_participant TEXT NOT NULL, "
                           f"link_id TEXT NOT NULL, time TEXT NOT NULL, number_of_group TEXT NOT NULL)")

    def delete_table(self):
        with database.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {self.table_name}")

    def add_data(self):
        with database.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO {self.table_name} VALUES ('{self.number_of_participant}', "
                           f"'{self.link_id}', '{self.time_for_db}', '{self.number_of_group}')")
