# -*- coding: UTF-8 -*-
import json, os


def create_json_file(name, content={}):
    """
    create a json file under jsondb folder

    :param content: dict
    :param name: string
    :return: bool
    """

    # get file path
    path = 'jsondb/' + name.rstrip('.json') + '.json'

    # check if file exists
    if os.path.exists(path):
        return False

    # open file
    with open(path, "w") as f:
        # write content
        f.write(json.dumps(content, ensure_ascii=False, indent=4, sort_keys=True))

    return True


def create_folder(directory):
    """
    create a folder

    :param directory: string
    :return: bool
    """

    # create directory if not exists
    if not os.path.exists('jsondb/' + directory):
        os.makedirs('jsondb/' + directory)

        return True

    return False
