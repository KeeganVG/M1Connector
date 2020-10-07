#!/usr/bin/python

"""Simple Connector to the MS-SQL Database that serves as the backend
    for M1

    Features:
    - Connect to DB
    - Run Query
"""

import pyodbc


class M1Connector:
    def __init__(self, host, db, uid, pwd, driver=None):
        """Create connection to M1 and expose functions

        Args:
            host(str): Path to machine running MSSQL
            db(str): db to connect to
            uid(str): username
            pwd(str): password
            driver(str): connection driver (default=None)

        """
        self.host = host
        self.db = db
        self.uid = uid
        self.pwd = pwd

        # jank?
        if driver is None:
            self.driver = "ODBC Driver 17 for SQL Server"
        else:
            self.driver = driver

        try:
            self._connect()
        except Exception as e:
            print(f"There was an exception while trying to connect.")
            print(str(e))

    def _connect(self):
        '''Make connection to db'''
        self.connection = pyodbc.connect(
            f'Driver={self.driver}'
            f';Server={self.host}'
            f';Database={self.db}'
            f';Trusted_connection=no'
            f';UID={self.uid}'
            f';PWD={self.pwd}'
        )
        self.cursor = self.connection.cursor()

    def execute(self, command):
        '''Pass command to db through connection. Does not commit'''
        self.cursor.execute(command)
 
    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

