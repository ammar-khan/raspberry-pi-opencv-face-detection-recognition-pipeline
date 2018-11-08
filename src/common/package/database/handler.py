##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
##

import sqlite3
from src.common.package.config import application as config_app


##
# Handler class
# This class will handle database operations.
##
class Handler:

    def __init__(self):
        self.database_connection = None
        return None

    ##
    # Static method create_connection()
    ##
    @staticmethod
    def create_connection():
        return sqlite3.connect(config_app.DATABASE_NAME)

    ##
    # Class method create_table()
    ##
    @classmethod
    def create_table(cls):
        cls.database_connection = cls.create_connection()
        cursor = cls.database_connection.cursor()

        sql_query = '''
        DROP TABLE IF EXISTS detections;
        CREATE TABLE detections (
                   id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                   desc TEXT
        );
        '''
        cursor.executescript(sql_query)

        cls.database_connection.commit()

    ##
    # Class method execute_query()
    #
    # @param sql_query SQL query string
    # @param parameters SQL query parameters
    # @param begin_transaction Boolean to start transaction (need to commit later)
    #
    # @return cursor
    ##
    @classmethod
    def execute_query(cls, sql_query, parameters=None, commit_changes=True):
        cls.database_connection = cls.create_connection()
        cursor = cls.database_connection.cursor()

        cursor.execute(sql_query, parameters)

        if commit_changes:
            cls.database_connection.commit()

        return cursor

    ##
    # Class method commit()
    ##
    @classmethod
    def commit(cls):
        if cls.database_connection:
            cls.database_connection.commit()

    ##
    # Class method close_connection()
    ##
    @classmethod
    def close_connection(cls):
        if cls.database_connection:
            cls.database_connection.close()
            cls.database_connection = None
