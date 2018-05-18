# -*- coding: UTF-8 -*-


class DB:
    """
    jsondb database class
    """

    database_name = None

    def __init__(self, database_name):
        """
        create a jsondb database

        :param database_name: string
        """

        self.database_name = database_name
