# -*- coding: UTF-8 -*-
import os
import json
from .. import CONFIG


class FileManager(object):
    """Manage files in root directory.

    Attributes:
        storage (str): The name of the storage folder for jsondb.
    """

    def __init__(self, storage=CONFIG.get('jsondb', 'storage')):
        """Init FileManager with storage folder.

        Args:
            storage (str): The storage folder for the databases.
        """

        self.storage = storage

        if not os.path.exists(self.storage):
            os.makedirs(self.storage)

    def exists(self, path):
        """Check if path exists.

        Args:
            path (str): The folder/file path that needs to be check (excluding storage folder).

        Returns:
            bool: True if the path exist, otherwise False.
        """

        if os.path.exists(self.storage + '/' + path):
            return True

        return False

    def create_json_file(self, name, path=None, content=None):
        """Create a json file under storage folder.

        The function validates the file name and also checks if path exists. The content would
        be written to the .json file with indentation 4 spaces and keys sorted.

        Args:
            name    (str) : The name of the file, you do not have to contain .json extension.
            path    (str) : The folder path of the file.
            content (dict): the json content that needs to be inserted to the file.

        Returns:
            bool: True if file created successfully, otherwise False.
            str : The error message if failed to create file or success message if file created.
        """

        # set content initial value
        if content is None:
            content = {}

        # build name with .json extension
        name = os.path.splitext(name)[0] + '.json'

        # validate name
        if name.find('/') != -1:
            return False, "File name %s cannot contain '/'." % name

        # set path to just file name when path is not defined
        if path is None:
            path = name

        # check path existence and build file path
        elif self.exists(path):
            path = path.strip('/') + '/' + name

        # invalid path is not allowed
        else:
            return False, "Path %s does not exists." % path

        # check if file exists
        if self.exists(path):
            return False, "File %s already exists." % path

        # create .json file
        with open(self.storage + '/' + path, "w") as f:
            # write content
            f.write(json.dumps(content, ensure_ascii=False, indent=4, sort_keys=True))

        return True, "File %s successfully created." % path

    def create_directory(self, directory):
        """Create a directory under storage folder.

        Args:
            directory (str): The path needs to be created

        Returns:
            bool: True if directory is created, otherwise False
        """

        # create directory if not exists
        if not self.exists(directory):
            os.makedirs(self.storage + '/' + directory)
            return True

        return False

    def read(self, path):
        """Read a .json file and parse it to dict.

        Args:
            path (str): The path to the file.

        Returns:
            dict: A dict that contains the JSON information.
        """

        # check if file exists
        if not self.exists(path):
            return None

        # read file
        with open(self.storage + '/' + path, 'r') as f:
            content = f.read()

        # convert to dict
        return json.loads(content)

    def write(self, path, content):
        """Write a .json file with content.

        Args:
            path    (str) : The path to the file.
            content (dict): The content that needs to be write to the file.

        Returns:
            bool: True if file is successfully written, otherwise False.
        """

        # check if file exists
        if not self.exists(path):
            return False

        # write file
        with open(self.storage + '/' + path, 'w') as f:
            f.write(json.dumps(content, ensure_ascii=False, indent=4, sort_keys=True))

        return True
