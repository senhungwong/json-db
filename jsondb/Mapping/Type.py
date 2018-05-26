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

        # update updated_at
        info = self.get_info()
        info['data'][primary]['updated_at'] = time.time()
        self.db.write(
            build_path([
                'schema', self.identifier
            ], 'information.json'),
            info
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

    def get_indices(self):
        """Get self indices.

        Returns:
            dict: Indices and its hashes.
        """

        return self.db.read(
            build_path([
                'indices', self.identifier
            ], 'index.json')
        )

    def create_index(self, attribute):
        """Create an index of an attribute.

        Args:
            attribute (str): An attribute that is going to be indexed.
        """

        attribute_index = {}

        # loop through all data
        for primary in self.get_info()['data'].keys():
            # get required attribute value
            data = self.get_data(primary)[attribute]

            # check if already have the value
            if data not in attribute_index:
                attribute_index[data] = {primary: None}
            else:
                attribute_index[data][primary] = None

        # create attribute file
        self.db.create(
            attribute,
            build_path(['indices', self.identifier]),
            attribute_index
        )

        # update index file
        indices = self.get_indices()
        indices[attribute] = hash(str(attribute_index))
        self.db.write(build_path(['indices', self.identifier], 'index.json'), indices)

    def is_indexed(self, attribute):
        """Check if an attribute is indexed.

        Args:
            attribute (str): Attribute name.

        Returns:
            bool: The attribute is indexed or not.
        """

        return attribute in self.get_indices()

    def lookup(self, attribute):
        """See attribute indices.

        Args:
            attribute (str): Attribute name.

        Returns:
            dict: Attribute indices.
        """

        return self.db.read(
            build_path([
                'indices', self.identifier
            ], attribute + '.json')
        )

    def update_index(self, attribute, value, primary):
        """Update an index.

        Args:
            attribute (str): Attribute name.
            value     (str): Attribute value.
            primary   (str): Attribute primary.
        """

        # get indices
        index = self.lookup(attribute)

        # add index
        if value not in index:
            index[value] = {}
        index[value][primary] = None

        # store
        self.db.write(
            build_path([
                'indices', self.identifier
            ], attribute + '.json'),
            index
        )

    def remove_index(self, attribute, value, primary):
        """Remove an attribute value in an index.

        Args:
            attribute (str): The attribute.
            value     (str): The value.
            primary   (str): The primary.
        """

        # get indices
        index = self.lookup(attribute)

        # remove index
        del index[value][primary]

        # remove value if it contains nothing
        if not index[value]:
            del index[value]

        # store
        self.db.write(
            build_path([
                'indices', self.identifier
            ], attribute + '.json'),
            index
        )
