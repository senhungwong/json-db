# import the main classes from the jsondb module. DB is the one
# that deals with database actions.
from jsondb import DB
from examples import guide


def db_guide(show_instruction=True):
    # Create an database object.
    guide(
        'Create a database object.',
        'jsondb = DB()',
        start=True,
        show_instruction=show_instruction
    )
    jsondb = DB()

    # Delete the existing database if it exists for reusing scripts.
    guide(
        'Delete the existing database if it exists for reusing scripts.',
        'jsondb.delete(force=True)',
        show_instruction=show_instruction
    )
    jsondb.delete(force=True)

    # Create the database.
    guide(
        'Create the database.',
        'jsondb.init()',
        show_instruction=show_instruction
    )
    jsondb.init()

    # Create a type (table) named users.
    guide(
        'Create a type (table) named users.',
        "jsondb.has_type('users')",
        show_instruction=show_instruction
    )
    jsondb.has_type('users')

    # Create another type named countries.
    guide(
        'Create another type named countries.',
        "jsondb.has_type('countries')",
        show_instruction=show_instruction
    )
    jsondb.has_type('countries')
