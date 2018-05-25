# -*- coding: UTF-8 -*-
from FileStructureManager import FileStructureManager
from ..Services.path_builder import build_path
from ..Services.identifier_generater import generate_identifier
from ..Services.pluralization import get_singular_plural


class JsonDatabase(object):
    """An object of jsondb database which contains jsondb database interaction functions.

    Attributes:
        database_name (str)        : The jsondb database name of current object.
        file_manager  (FileManager): The file manager for current object.
    """

    def __init__(self, database_name='database', storage='storage', section='jsondb'):
        """Create a jsondb database.

        Args:
            database_name (str): Set current instance to a specific database.
            storage       (str): The jsondb storage folder name for initializing FileManager.
            section       (str): The section name of the configurations (the one wrapped in []).
        """

        self.database_name = database_name
        self.file_manager = FileStructureManager(database=database_name, storage=storage, section=section)

    def init(self):
        """Create a database.

        Create a folder in storage having the database as folder name as the database. Create a
        folder inside the database folder and name it data. Create a schema folder in database folder.

        The structure is like:

        storage/
        └── database/
            ├── data/
            ├── schema/
            │   └── identifiers.json
            └── indices/
        """

        # storage/
        if not self.file_manager.exists(build_path(['/'])):
            self.file_manager.create_directory(build_path(['/']))

        # storage/database/
        success = self.file_manager.create_directory(build_path([self.database_name]))
        if not success:
            raise IOError("Database " + self.database_name + " already exists.")

        # storage/database/data
        self.file_manager.create_directory(build_path([self.database_name, 'data']))

        # storage/database/schema
        self.file_manager.create_directory(build_path([self.database_name, 'schema']))

        # storage/database/schema/identifiers.json
        self.file_manager.create_json_file('identifiers', self.database_name + '/schema', {})

        # storage/database/indices
        self.file_manager.create_directory(build_path([self.database_name, 'indices']))

        print "Database %s created successfully." % self.database_name

    def has_type(self, type_name, if_not_exists=True, pluralize=True):
        """Create a type.

        The function will make the type name to plural and lowercase for standardizing type names.
        Set pluralize to False if you want to create type based on the input. Create data/types.json
        and schema/identifier.json files in the database. The identifier is the unique key for each
        type which is used in handling type name changing.

        storage/
        └── database/
            ├── data/
            │   └── types/
            │       └── primary.json
            ├── schema/
            │   ├── identifiers.json
            │   └── types-identifier/
            │       ├── information.json
            │       └── relations.json
            └── indices/
                └── types-identifier/
                    └── attribute.json

        Args:
            type_name     (str) : The type name. Will be set to plural and lowercase if pluralize is True.
            if_not_exists (bool): Skip if the type already exists.
            pluralize     (bool): Standardize type names to plural and lowercase.
        """

        identifier = generate_identifier()

        # set the actual type name
        if pluralize:
            _, type_name = get_singular_plural(type_name.lower())

        # build type path
        type_path = build_path([self.database_name, 'data', type_name])

        # create database/data/types/ folder
        self.file_manager.create_directory(type_path, check_dir=False)

        # build schema path
        schema_path = build_path([self.database_name, 'schema', identifier])

        # create database/schema/identifier/ folder
        self.file_manager.create_directory(schema_path, check_dir=False)

        # create database/schema/identifier/information.json
        self.file_manager.create_json_file(
            'information', schema_path, {
                "type": type_name,
                "data": {}
            }
        )

        # create database/schema/identifier/relations.json
        self.file_manager.create_json_file(
            'relations', schema_path, {}
        )

        # update database/schema/identifiers.json
        identifiers_path = build_path([self.database_name, 'schema'], 'identifiers.json')
        content = self.file_manager.read(identifiers_path)
        content[type_name] = identifier
        self.file_manager.write(identifiers_path, content)

        print "Type %s created successfully." % type_name

    def read(self, path):
        """Read specific file in database.

        Attributes:
            path (str): The path to .json file (excluding storage/database).

        Returns:
            dict: The content in dict format.
        """

        return self.file_manager.read(self.database_name + '/' + path)

    def write(self, path, content):
        """Write to a .json file in database.

        Args:
            path    (str) : The path to .json file (excluding storage/database).
            content (dict): The content that is going to be written in .json file.
        """

        self.file_manager.write(self.database_name + '/' + path, content)

    def create(self, name, path, content):
        """Create a .json file in database.

        Args:
            name    (str) : The name of the .json file.
            path    (str) : The path of the .json file.
            content (dict): The content that is going to be written in .json file.
        """

        self.file_manager.create_json_file(name, self.database_name + '/' + path, content)

    def delete(self, force=False):
        """Delete current database.

        Args:
            force (bool): If true, will remove the folder in force mode.
        """

        self.file_manager.remove(
            build_path([self.database_name]),
            ignore_errors=force
        )

        print "Database %s is deleted." % self.database_name

    def get_hash(self, path):
        """Get the hash value.

        Args:
            path (str): The file path.

        Returns:
            str: The hash value.
        """

        return self.file_manager.get_hash(self.database_name + '/' + path)
