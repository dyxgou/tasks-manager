import sqlite3


class Connection:
    __connection: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self) -> None:
        self.__connection = sqlite3.connect("database.db")
        self.cursor = self.__connection.cursor()

    def commit(self):
        self.__connection.commit()
