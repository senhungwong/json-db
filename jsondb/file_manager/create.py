# -*- coding: UTF-8 -*-
import json


def create_json_file(name, content={}):
    """
    create a json file under jsondb folder

    :param content: dict
    :param name: string
    :return: void
    """

    # open file
    with open('jsondb/' + name.rstrip('.json') + '.json', "w") as f:
        # write content
        f.write(json.dumps(content, ensure_ascii=False))
