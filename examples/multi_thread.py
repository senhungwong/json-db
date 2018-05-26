from db import db_guide
from User import User
from examples import guide


def multithread_guide(show_instruction=True):
    # Initialize database.
    guide(
        'Initialize database. See more using `$ python example database.`',
        None,
        start=True,
        show_instruction=show_instruction
    )
    db_guide(show_instruction=False)

    # Create an user in thread 1.
    guide(
        'Create an user in thread 1.',
        [
            'user_t1 = User()',
            "user_t1.__primary__ = 'alex'",
            'user_t1.age = 20',
            'user_t1.save()',
            'print "Thread 1 attributes: ", user_t1.attributes()'
        ],
        show_instruction=show_instruction
    )
    user_t1 = User()
    user_t1.__primary__ = 'alex'
    user_t1.age = 20
    user_t1.save()
    if show_instruction:
        print "Thread 1 attributes: ", user_t1.attributes()

    # Get the user just created in thread 2.
    guide(
        'Get the user just created in thread 2.',
        [
            "user_t2 = User('alex')",
            'print "Thread 2 attributes: ", user_t2.attributes()'
        ],
        show_instruction=show_instruction
    )
    user_t2 = User('alex')
    if show_instruction:
        print "Thread 2 attributes: ", user_t2.attributes()

    # Update thread 1 user.
    guide(
        'Update thread 1 user.',
        [
            'user_t1.age = 21',
            'user_t1.save()',
            'print "Thread 1 updated attributes: ", user_t1.attributes()'
        ],
        show_instruction=show_instruction
    )
    user_t1.age = 21
    user_t1.save()
    if show_instruction:
        print "Thread 1 updated attributes: ", user_t1.attributes()

    # Check thread 2 attributes.
    guide(
        'Check thread 2 attributes. It should not be updated because the local copy is not been updated after thread 1 '
        'saving.',
        'print "Thread 2 current attributes: ", user_t2.attributes()',
        show_instruction=show_instruction
    )
    if show_instruction:
        print "Thread 2 current attributes: ", user_t2.attributes()

    # Sync thread 2 manually.
    guide(
        'Sync thread 2 manually.',
        [
            'user_t2.sync()',
            'print "Thread 2 attributes after sync: ", user_t2.attributes()'
        ],
        show_instruction=show_instruction
    )
    user_t2.sync()
    if show_instruction:
        print "Thread 2 attributes after sync: ", user_t2.attributes()

    # Update thread 1 again.
    guide(
        'Update thread 1 again.',
        [
            "user_t1.email = '0x53656e@gmail.com'",
            'user_t1.save()',
            'print "Thread 1 attributes: ", user_t1.attributes()'
        ],
        show_instruction=show_instruction
    )
    user_t1.email = '0x53656e@gmail.com'
    user_t1.save()
    if show_instruction:
        print "Thread 1 attributes: ", user_t1.attributes()

    # Save action will sync before saving to database.
    guide(
        'Save action will sync before saving to database.',
        [
            'print "Thread 2 attributes before modify and save: ", user_t2.attributes()',
            'user_t2.age = 50',
            'user_t2.save()',
            'print "Thread 2 attributes after modify and save: ", user_t2.attributes()'
        ],
        show_instruction=show_instruction
    )
    if show_instruction:
        print "Thread 2 attributes before modify and save: ", user_t2.attributes()
    user_t2.age = 50
    user_t2.save()
    if show_instruction:
        print "Thread 2 attributes after modify and save: ", user_t2.attributes()
