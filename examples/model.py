from db import db_guide
from User import User
from examples import guide


def model_guide(show_instruction=True):
    # Initialize database.
    guide(
        'Initialize database. See more using `$ python example database.`',
        None,
        start=True,
        show_instruction=show_instruction
    )
    db_guide(show_instruction=False)

    # Create a new user object (a new row).
    guide(
        'Create a new user object (a new row).',
        'user = User()',
        show_instruction=show_instruction
    )
    user = User()

    # Set the primary (primary key) to 'alex'.
    guide(
        "Set the primary (primary key) to 'alex'.",
        "user.__primary__ = 'alex'",
        show_instruction=show_instruction
    )
    user.__primary__ = 'alex'

    # Create an email field for 'alex'.
    guide(
        "Create an email field for 'alex'.",
        "user.email = '0x53656e@gmail.com'",
        show_instruction=show_instruction
    )
    user.email = '0x53656e@gmail.com'

    # Save the user model to database (a new row is been created).
    guide(
        'Save the user model to database (a new row is been created).',
        'user.save()',
        show_instruction=show_instruction
    )
    user.save()

    # See user's attributes.
    guide(
        "See user's attributes.",
        "print 'User attributes: ', user.attributes()",
        show_instruction=show_instruction
    )
    print 'User attributes: ', user.attributes()

    # Change users' email to something else.
    guide(
        "Change users' email to something else.",
        "user.email = 'other@gmail.com'",
        show_instruction=show_instruction
    )
    user.email = 'other@gmail.com'

    # Save user model to database (the row is been updated).
    guide(
        'Save user model to database (the row is been updated).',
        'user.save()',
        show_instruction=show_instruction
    )
    user.save()

    # See changed attributes.
    guide(
        'See changed attributes.',
        "print 'Changed attributes: ', user.attributes()",
        show_instruction=show_instruction
    )
    print 'Changed attributes: ', user.attributes()

    # See all users' information.
    guide(
        "See all users' information.",
        "print 'User information: ', user.info()",
        show_instruction=show_instruction
    )
    print 'User information: ', user.info()
