# -*- coding: UTF-8 -*-
from pattern.en import pluralize, singularize


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
