# -*- coding: UTF-8 -*-
from Type import Type


class Model(object):
    __hidden__ = {
        '__primary__',  # the primary key of the type
        '__type__',     # the type of the model
        '__hidden__',   # hidden its self
        '__created__'   # if the data is created
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
        self.__type__ = Type(self.__type__)

        # create new object if primary is not given
        if primary is None:
            self.__created__ = False
            return

        # if the object exists
        self.__created__ = True

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

        # create a new row in database
        if not self.__created__:
            self.__type__.create_data(self.__primary__, self.attributes())
            self.__created__ = True

        # update existing row in database
        else:
            self.__type__.update_data(self.__primary__, self.attributes())
