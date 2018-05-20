# -*- coding: UTF-8 -*-
from ..Database.JsonDatabase import JsonDatabase
from ..Services.path_builder import build_path


class Type(object):
    def __init__(self, name, database_name='database', storage='storage', section='jsondb'):
        self.name = name
        self.db = JsonDatabase(database_name=database_name, storage=storage, section=section)

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
