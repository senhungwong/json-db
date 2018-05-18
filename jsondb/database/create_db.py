# -*- coding: UTF-8 -*-
from ..FileManager.create import create_folder, create_json_file


def create_database(database_name):
    """
    create a database

    :param database_name: string
    :return: void
    """

    # create database folder
    if not create_folder(database_name):
        exit('Database ' + database_name + ' already exists')

    # create data folder
    create_folder(database_name + '/' + 'data')

    # create schema file
    create_json_file(database_name + '/schema', {"types": {}})
