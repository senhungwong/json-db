# -*- coding: UTF-8 -*-
from Type import Type


class Model(object):
    __hidden__ = {
        '__primary__',     # the primary key of the type
        '__type__',        # the type of the model
        '__hidden__',      # hidden its self
        '__created__',     # if the data is created
        '__identifier__',  # the type identifier
        '__hash__',        # the hash value in data
    }

    __type__ = None

    def __init__(self, primary=None):
        """Initialize object.

        If primary is not given, new type object is created. If primary is given,
        try to find the .json file in storage and assign attributes to the current
        object.

        Args:
            primary (str): If given, search data; otherwise create new object.
        """

        self.__primary__ = primary

        # parse type
        type_dir, temp = [], ''
        for char in self.__type__:
            if char != '.':
                temp += char
            else:
                type_dir.append(temp)
                temp = ''
        type_dir.append(temp)

        # validate
        type_length = len(type_dir)
        if type_length != 4 and type_length != 1:
            raise ValueError  # wrong type string

        # build type
        if type_length == 1:
            self.__type__ = Type(self.__type__)
        else:
            self.__type__ = Type(section=type_dir[0], storage=type_dir[1], database_name=type_dir[2], name=type_dir[3])

        # get identifier
        self.__identifier__ = self.__type__.identifier

        # create new object if primary is not given
        if primary is None:
            self.__created__ = False
            self.__hash__ = hash(str(self.attributes()))
            return

        # if the object exists
        self.__created__ = True

        # get hash value
        self.__hash__ = self.__type__.get_hash(self.__primary__)

        # update attributes from .json file
        self.__dict__.update(self.__type__.get_data(self.__primary__))

    def attributes(self):
        """Get all attributes in the object.

        Returns:
            dict: All attributes in the object.
        """

        return {
            attribute: value
            for attribute, value in self.__dict__.items()
            if attribute not in self.__hidden__
        }

    def save(self):
        """Save current object to .json file.

        If the row is not found in the folder, create one; otherwise update it.
        Also update schema rows.

        """

        # check if primary is set
        if not self.__primary__:
            raise NameError('Object __primary__ is not defined')

        attributes = self.attributes()
        old_attributes = self.__type__.get_data(self.__primary__) if self.__created__ else {}

        # create a new row in database
        if not self.__created__:
            self.__hash__ = hash(str(self.attributes()))
            attributes.update({'__hash__': self.__hash__})
            self.__type__.create_data(self.__primary__, attributes)
            self.__type__.insert_row(self.__primary__)
            self.__created__ = True

        # update existing row in database
        else:
            self.sync(force=False)
            self.__hash__ = hash(str(self.attributes()))
            attributes.update({'__hash__': self.__hash__})
            self.__type__.update_data(self.__primary__, attributes)

        for attribute in self.__type__.get_indices().keys():
            # pass if object does not have the attribute
            if attribute not in attributes:
                continue

            # check attribute been updated
            if attribute in old_attributes and attributes[attribute] != old_attributes[attribute]:
                self.__type__.remove_index(attribute, old_attributes[attribute], self.__primary__)

            # update attribute
            self.__type__.update_index(attribute, attributes[attribute], self.__primary__)

    def info(self):
        """Get current type information.

        Returns:
            dict: Current type information.
        """

        return self.__type__.get_info()

    def sync(self, force=True):
        """Sync the current object.

        Args:
            force (bool): If true, update the newest data to current object.
                New attributes will be kept, but updated attributes in current
                object are overwritten by the attributes in database. If false,
                will sync newly created attributes in the database, but keep
                all local changes.
        """

        if hash(str(self.attributes())) != self.__type__.get_hash(self.__primary__):
            db_data = self.__type__.get_data(self.__primary__)
            if force:
                self.__dict__.update(db_data)
            else:
                db_data.update(self.__dict__)
                self.__dict__ = db_data

    def has_relation(self, relation, type):
        """Create a relation for current type.

        Args:
            relation (str): The relation name.
            type     (str): Related type name.
        """

        self.__type__.insert_relation(relation, type, self.__primary__)
        self.__dict__.update({relation: []})

    def relations(self, relation):
        """Get a specific relation data.

        Args:
            relation (str): The relation name of the relation.

        Returns:
            dict: Dict of relation data.
        """

        # get identifier
        target_identifier = self.__type__.get_relations()[relation]

        # get type
        target_type = self.__type__.get_target_info(target_identifier)['type']

        # build relations dict
        relations = {}
        for target_primary in getattr(self, relation):
            relations[target_primary] = self.__type__.get_target_data(target_type, target_primary)

        return relations

    def index(self, attribute):
        """Create an index of an attribute.

        Args:
            attribute (str): Attribute that is going to be indexed.
        """

        # index attribute
        self.__type__.create_index(attribute)

    def lookup(self, attribute):
        """Look up a specific attribute's index.

        Args:
            attribute (str): The attribute name that is going to be looked up.

        Returns:
            dict: Indices of the attribute.
        """

        return self.__type__.lookup(attribute)

    def find(self, attribute, value, operator='=', build=True):
        """Look up and range search a value.

        Args:
            attribute (str) : The attribute name.
            value     (str) : The value that is going to be compared with.
            operator  (str) : The binary comparison operator.
            build     (bool): If result needs to be built or not.

        Returns:
            list: The list of data that matches the search requirement.
        """

        # if the attribute is indexed, use indexed find
        if self.__type__.is_indexed(attribute):
            primaries = self.__type__.indexed_find(attribute, value, operator=operator)
        # if attribute is not indexed, use non indexed find
        else:
            primaries = self.__type__.non_indexed_find(attribute, value, operator=operator)

        # if does not require parse, return the list
        if not build:
            return primaries

        # build data
        data = []

        # get all data in primaries
        for primary in primaries:
            data.append(self.__type__.get_data(primary))

        return data
