# -*- coding: UTF-8 -*-
from ..FileManager.FileManager import FileManager


class Database(object):
    """An object of jsondb database which contains jsondb database interaction functions.

    Attributes:
        database_name (str)        : The jsondb database name of current object.
        file_manager  (FileManager): The file manager for current object.
    """

    def __init__(self, database_name, storage='jsondb'):
        """Create a jsondb database.

        Args:
            database_name (str): Set current instance to a specific database.
            storage       (str): The jsondb storage folder name for initializing FileManager.
        """

        self.database_name = database_name
        self.file_manager = FileManager(storage)

    def init(self):
        """Create a database.

        Create a folder in storage having the database as folder name as the database. Create a
        folder inside the database folder and name it data. Create a schema folder in database folder.

        The structure is like:

        project_root/
        └── storage/
            └── database_name/
                ├── data/
                └── schema/

        Returns:
            None
        """

        # create database folder
        success = self.file_manager.create_directory(self.database_name)
        if not success:
            exit("Database %s already exists." % self.database_name)

        # create data folder
        self.file_manager.create_directory(self.database_name + '/data')

        # create schema folder
        self.file_manager.create_directory(self.database_name + '/schema')

        print "Database %s created successfully." % self.database_name
