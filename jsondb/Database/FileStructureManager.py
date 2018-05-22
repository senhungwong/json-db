# -*- coding: UTF-8 -*-
import os
import json
from ..Services.config import Config
from shutil import rmtree


class FileStructureManager(object):
    """Manage files in root directory.

    Attributes:
        storage (str): The name of the storage folder for jsondb.
    """

    def __init__(self, database='database', storage='storage', section='jsondb'):
        """Init FileManager with storage folder.

        Args:
            database (str): The database it will use.
            storage  (str): The storage folder for the databases.
            section  (str): The config section of database and storage stored in .jsondb.ini
        """

        self.database = Config.get(section, database)
        self.storage = Config.get(section, storage)

    def exists(self, path, in_storage=True):
        """Check if path exists.

        Args:
            path       (str) : The folder/file path that needs to be check.
            in_storage (bool): If is in storage, append storage folder at front.

        Returns:
            bool: True if the path exist, otherwise False.
        """

        if in_storage:
            path = self.storage + '/' + path

        if os.path.exists(path):
            return True

        return False

    def create_directory(self, directory, in_storage=True, check_dir=True):
        """Create a directory under storage folder.

        Args:
            directory  (str) : The path needs to be created
            in_storage (bool): If is in storage, append storage folder at front.
            check_dir  (bool): Check if dir exists

        Returns:
            bool: True if directory is created, otherwise False
        """

        if in_storage:
            directory = self.storage + '/' + directory

        # create directory if not exists
        if not check_dir or not self.exists(directory):
            os.makedirs(directory)
            return True

        return False

    def create_json_file(self, name, path=None, content=None, in_storage=True):
        """Create a json file under storage folder.

        The function validates the file name and also checks if path exists. The content would
        be written to the .json file with indentation 4 spaces and keys sorted.

        Args:
            name       (str) : The name of the file, you do not have to contain .json extension.
            path       (str) : The folder path of the file.
            content    (dict): the json content that needs to be inserted to the file.
            in_storage (bool): If is in storage, append storage folder at front.
        """

        # set content initial value
        if content is None:
            content = {}

        # build name with .json extension
        name = os.path.splitext(name)[0] + '.json'

        # validate name
        if name.find('/') != -1:
            raise ValueError("File name " + name + " cannot contain '/'.")

        # set path to just file name when path is not defined
        if path is None:
            path = name

        # check path existence and build file path
        elif self.exists(path, in_storage=in_storage):
            path = path.strip('/') + '/' + name

        # invalid path is not allowed
        else:
            raise IOError("Path " + path + " does not exists.")

        # check if file exists
        if self.exists(path, in_storage=in_storage):
            raise IOError("File " + path + " already exists.")

        # check if in storage
        if in_storage:
            path = self.storage + '/' + path

        # create .json file
        with open(path, "w") as f:
            # write content
            f.write(json.dumps(content, ensure_ascii=False, indent=4, sort_keys=True))

    def read(self, path, in_storage=True):
        """Read a .json file and parse it to dict.

        Args:
            path       (str) : The path to the file.
            in_storage (bool): If is in storage, append storage folder at front.

        Returns:
            dict: A dict that contains the JSON information.
        """

        # check if file exists
        if not self.exists(path, in_storage=in_storage):
            raise IOError('File " + path + " does not exist.')

        # check in storage
        if in_storage:
            path = self.storage + '/' + path

        # read file
        with open(path, 'r') as f:
            content = f.read()

        # convert to dict
        return json.loads(content)

    def write(self, path, content, in_storage=True):
        """Write a .json file with content.

        Args:
            path       (str) : The path to the file.
            content    (dict): The content that needs to be write to the file.
            in_storage (bool): If is in storage, append storage folder at front.
        """

        # check if file exists
        if not self.exists(path):
            raise IOError('File " + path + " does not exist.')

        # check in storage
        if in_storage:
            path = self.storage + '/' + path

        # write file
        with open(path, 'w') as f:
            f.write(json.dumps(content, ensure_ascii=False, indent=4, sort_keys=True))

    def remove(self, path, in_storage=True, ignore_errors=False):
        """Remove a folder and its sub-folders and files.

        Args:
            path          (str) : The path to the folder.
            in_storage    (bool): If the path is in storage.
            ignore_errors (bool): If true, will remove the folder in force mode.
        """

        if in_storage:
            path = self.storage + '/' + path

        rmtree(path, ignore_errors=ignore_errors)

    def get_hash(self, path, in_storage=True):
        """Get the hash value of a .json file.

        The function will check if the fast way gets the hash value. If not, read
        the whole file and find the hash value. Keep attributes name starts in
        lowercase will significantly improve the read speed.

        Args:
            path       (str) : The path to the folder.
            in_storage (bool): If the path is in storage.

        Returns:
            str: The hash value.
        """

        if in_storage:
            path = self.storage + '/' + path

        # initialize hash
        __hash__ = None

        # open file
        with open(path, 'r') as f:
            for i, line in enumerate(f):
                # get hash value in line 1
                if i == 1:
                    __hash__ = line.strip()[:-3]

        # check if file has line 1
        if not __hash__:
            return None

        # check if the line is hash
        if __hash__[1:9] != '__hash__':
            return self.read(path, in_storage=False)['__hash__']

        return json.loads('{' + __hash__ + '}')['__hash__']
