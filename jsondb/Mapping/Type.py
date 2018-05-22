# -*- coding: UTF-8 -*-
from ..Database.JsonDatabase import JsonDatabase
from ..Services.path_builder import build_path
import time


class Type(object):
    def __init__(self, name, database_name='database', storage='storage', section='jsondb'):
        self.name = name
        self.db = JsonDatabase(database_name=database_name, storage=storage, section=section)
        self.identifier = self.get_identifier()

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

    def get_identifier(self):
        """Get the identifier of current type.

        Returns:
            str: The identifier generated when create the type.
        """

        return self.db.read(build_path(['schema'], 'identifiers.json'))[self.name]

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
