# -*- coding: UTF-8 -*-
import uuid


def generate_identifier():
    """Generate an unique identifier.

    Returns:
        str: An unique identifier.
    """
    return str(uuid.uuid4())
