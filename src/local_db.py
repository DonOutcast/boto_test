import sqlite3


class Database:

    def __init__(self, path_to_db="database.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        connection.set_trace_callback(logger)

        data = None

        if commit:
            connection.commit()

        if fetchone:
            data = cursor.fetchone()

        if fetchall:
            data = cursor.fetchall()

        connection.close()

        return data


def logger(statement):
    print(f"{statement}")
