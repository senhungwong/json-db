# -*- coding: UTF-8 -*-
from ..FileManager.FileManager import FileManager
from ..Services.services import generate_identifier, get_singular_plural


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

    def create_type(self, type_name, if_not_exists=True, pluralize=True):
        """Create a type.

        The function will make the type name to plural and lowercase for standardizing type names.
        Set pluralize to False if you want to create type based on the input. Create data/types.json
        and schema/identifier.json files in the database. The identifier is the unique key for each
        type which is used in handling type name changing.

        database_name/
        ├── data/
        │   └── types.json
        └── schema/
            └── identifier.json

        Args:
            type_name     (str) : The type name. Will be set to plural and lowercase if pluralize is True.
            if_not_exists (bool): Skip if the type already exists.
            pluralize     (bool): Standardize type names to plural and lowercase.

        Returns:
            None
        """

        identifier = generate_identifier()

        # set the actual type name
        if pluralize:
            _, type_name = get_singular_plural(type_name.lower())

        # create data/type.json
        success, message = self.file_manager.create_json_file(
            type_name, self.database_name + '/data', {
                "data": {},
                "identifier": str(identifier)
            }
        )

        if not success:
            if if_not_exists:
                return
            exit(message)

        # create schema/identifier.json
        success, message = self.file_manager.create_json_file(
            str(identifier), self.database_name + '/schema', {
                "type": type_name
            }
        )

        if not success:
            exit(message)

        print "Type %s created successfully." % type_name
