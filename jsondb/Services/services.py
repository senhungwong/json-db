# -*- coding: UTF-8 -*-
import uuid
from pattern.en import pluralize, singularize


def generate_identifier():
    return uuid.uuid4()


def get_singular_plural(noun):
    """Get the singular and plural form of a noun.

    Args:
        noun (str): A word that needs to be parsed.

    Returns:
        str: The singular form of the noun.
        str: The plural form of the noun.
    """
    singular = singularize(noun)
    if noun is not singular:
        return singular, noun
    else:
        return singular, pluralize(noun)
