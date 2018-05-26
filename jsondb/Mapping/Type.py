# -*- coding: UTF-8 -*-
from ..Database.JsonDatabase import JsonDatabase
from ..Services.path_builder import build_path
import time


class Type(object):
    def __init__(self, name, database_name='database', storage='storage', section='jsondb'):
        self.name = name
        self.db = JsonDatabase(database_name=database_name, storage=storage, section=section)
        self.identifier = self.get_identifiers()[self.name]

    def __str__(self):
        return self.name

    def get_data(self, primary):
        """Get row data from database.

        Args:
            primary (str): The name of the primary.json.

        Returns:
            dict: Data from .json file as a dict.
        """

        return self.db.read(
            build_path([
                'data', self.name
            ], primary + '.json')
        )

    def update_data(self, primary, content):
        """Update the existing data in database.

        Args:
            primary (str) : The name of the primary.json.
            content (dict): The content that would be written in the .json file.
        """

        self.db.write(
            build_path([
                'data', self.name
            ], primary + '.json'),
            content
        )

    def create_data(self, primary, content):
        """Create a data in database

        Args:
            primary (str) : The name of the primary.json.
            content (dict): The content that would be written in the .json file.
        """

        self.db.create(
            primary,
            build_path([
                'data', self.name
            ]),
            content
        )

    def get_identifiers(self):
        """Get the identifiers.

        Returns:
            str: The identifiers generated when create the type.
        """

        return self.db.read(build_path(['schema'], 'identifiers.json'))

    def get_hash(self, primary):
        """Get the hash value.

        Args:
            primary (str): The hash value of the primary.

        Returns:
            str: The hash value.
        """

        return self.db.get_hash(build_path(['data', self.name], primary + '.json'))

    def get_info(self):
        """Get current type info.

        Examples:
        {
            "data": {
                "alex": {
                    "created_at": 1526925316.419692,
                    "deleted_at": null,
                    "updated_at": 1526925316.419692
                }
            },
            "type": "users"
        }

        Returns:
            dict: Current type information.
        """

        return self.db.read(
            build_path([
                'schema', self.identifier
            ], 'information.json')
        )

    def get_target_info(self, target_identifier):
        """Get target type information.

        Args:
            target_identifier (str): The target type identifier.

        Returns:
            dict: Target type information.
        """

        return self.db.read(
            build_path([
                'schema', target_identifier
            ], 'information.json')
        )

    def insert_row(self, primary):
        """Insert a new row into the information.

        Args:
            primary (str) : The primary of the inserted row.
        """

        # get current info
        info = self.get_info()

        # check if data exists
        if primary in info['data']:
            raise ValueError  # the provided primary is already existing in information

        # insert row
        info['data'][primary] = {
            'created_at': time.time(),
            'updated_at': time.time(),
            'deleted_at': None
        }

        # write to database
        self.db.write(
            build_path([
                'schema', self.identifier
            ], 'information.json'),
            info
        )

    def get_relations(self):
        """Get all relation types' identifier.

        Returns:
            dict: All relation types' identifiers.
        """

        return self.db.read(
            build_path([
                'schema', self.identifier
            ], 'relations.json')
        )

    def insert_relation(self, relation, type, primary):
        """Create a new relation for current type.

        ValueError will be raised if the relation already exists or relation name
        occupied by other attributes.

        Args:
            relation (str): The relation name.
            type     (str): Related type name.
            primary  (str): The primary of the relation.
        """

        # get all relations
        relations = self.get_relations()

        # check if relation exists
        if relation in relations:
            raise ValueError  # the relation is already declared in relations.json

        # insert relation
        relations[relation] = self.db.read(build_path(['schema'], 'identifiers.json'))[type]

        # fetch type data
        data = self.get_data(primary)

        # check if relation name occupied
        if relation in data:
            raise ValueError  # the relation is already declared in primary.json

        # assign data relation with an empty column
        data[relation] = []

        # save schema to database
        self.db.write(
            build_path([
                'schema', self.identifier
            ], 'relations.json'),
            relations
        )

        # save data to database
        self.db.write(
            build_path([
                'data', self.name
            ], primary + '.json'),
            data
        )

    def get_target_data(self, target_type, target_primary):
        """Get target data.

        Args:
            target_type    (str): The target type.
            target_primary (str): The target primary.

        Returns:
            dict: The target primary data.
        """

        return self.db.read(
            build_path([
                'data', target_type
            ], target_primary + '.json')
        )
