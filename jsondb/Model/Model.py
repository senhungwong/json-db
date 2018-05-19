# -*- coding: UTF-8 -*-
from ..FileManager.FileManager import FileManager
from .. import CONFIG


class Model(object):
    storage = CONFIG.get('jsondb', 'storage')

    database = CONFIG.get('jsondb', 'database')

    type = None

    def __init__(self, primary=None):
        """Initialize object.

        If primary is not given, new type object is created. If primary is given,
        try to find the .json file in storage and assign attributes to the current
        object.

        Args:
            primary (str): If given, search data; otherwise create new object.
        """

        # init file manager
        self.file_manager = FileManager(self.storage)

        # create new object if primary is not given
        if primary is None:
            self.data = {}
            self.__primary__ = None
            return

        # model should have basic storing information
        if not self.storage or not self.database or not self.type:
            exit('Model %s/%s/%s should be declared in class.' % (self.storage, self.database, self.type))

        # make path
        path = self.database + '/data/' + self.type + '/' + primary + '.json'

        # check if path exists
        if not self.file_manager.exists(path):
            exit('Path %s is not found.' % path)

        # set current object primary
        self.__primary__ = primary

        # set attributes from .json file
        self.data = self.file_manager.read(path)

    def save(self):
        """Save current object to .json file.

        If the row is not found in the folder, create one; otherwise update it.
        Also update schema rows.

        """

        # get path
        path = self.database + '/data/' + self.type + '/'

        # if row is not found
        if not self.file_manager.exists(path + self.__primary__ + '.json'):
            # create .json
            self.file_manager.create_json_file(self.__primary__, path, self.data)

        # if row is found
        else:
            self.file_manager.write(path + self.__primary__ + '.json', self.data)

    def add_relation(self):
        pass
