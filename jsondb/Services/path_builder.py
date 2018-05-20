# -*- coding: UTF-8 -*-


def build_path(directories, file_name=None):
    """Build a path string.

    Args:
        directories (list): The directories that is going to be joined in forming a path.
        file_name   (str) : The file name if is building a path to a file.

    Returns:
        str: The path to the folder or file.
    """

    directory = "/".join([directory.strip('/') for directory in directories])

    if file_name:
        directory += '/' + file_name

    return directory
