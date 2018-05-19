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
            self.__dict__ = {}
            return

        # model should have basic storing information
        if not self.storage or not self.database or not self.type:
            exit('Model %s/%s/%s should be declared in class.' % (self.storage, self.database, self.type))

        # make path
        path = self.database + '/data/' + self.type + '/' + primary + '.json'

        # check if path exists
        if not self.file_manager.exists(path):
            exit('Path %s is not found.' % path)

        # set attributes from .json file
        self.__dict__ = self.file_manager.read(path)

        # set current object primary
        self.primary = primary

    def save(self):
        pass

    def add_relation(self):
        pass
