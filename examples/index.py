from examples.model import model_guide
from User import User
from examples import guide
import time
import random


def index_guide(show_instruction=True):
    # Create an user node for relation instruction.
    guide(
        'Create an user node for relation instruction. See more using `$ python example model`',
        start=True,
        show_instruction=show_instruction
    )
    model_guide(show_instruction=False)

    # Create index.
    guide(
        'Create index.',
        [
            "user = User('alex')",
            "user.index('email')",
            "print 'User email indices:', user.lookup('email')"
        ],
        show_instruction=show_instruction
    )
    user = User('alex')
    user.index('email')
    if show_instruction:
        print 'User email indices:', user.lookup('email')

    # Add age field for range search demo.
    guide(
        'Add age field for range search demo.',
        [
            'user.age = 20',
            'user.save()'
        ],
        show_instruction=show_instruction
    )
    user.age = 20
    user.save()

    # Create more users.
    guide(
        'Create more users.',
        [
            'user = User()',
            "user.__primary__ = 'senhung'",
            "user.email = '0x53656e@gmail.com'",
            'user.age = 21',
            'user.save()',
            "print 'User email indices:', user.lookup('email')"
        ],
        show_instruction=show_instruction
    )
    user = User()
    user.__primary__ = 'senhung'
    user.email = '0x53656e@gmail.com'
    user.age = 21
    user.save()
    if show_instruction:
        print 'User email indices:', user.lookup('email')

    # Update indexed attribute.
    guide(
        'Update indexed attribute.',
        [
            "user.email = 'other@gmail.com'",
            'user.save()',
            "print 'User email indices:', user.lookup('email')"
        ],
        show_instruction=show_instruction
    )
    user.email = 'other@gmail.com'
    user.save()
    if show_instruction:
        print 'User email indices:', user.lookup('email')

    # Find list of users who has email 'other@gmail.com'.
    guide(
        "Find list of users who has email 'other@gmail.com'.",
        [
            "print 'Using lookup method:', user.lookup('email')['other@gmail.com'].keys()",
            "print 'Using find method:', user.find('email', 'other@gmail.com', build=False)"
        ],
        show_instruction=show_instruction
    )
    if show_instruction:
        print 'Using lookup method:', user.lookup('email')['other@gmail.com'].keys()
        print 'Using find method:', user.find('email', 'other@gmail.com', build=False)

    # Insert 50 random users.
    guide(
        'Insert 50 random users.',
        [
            'for i in xrange(50):',
            '   user_factory = User()',
            "   user_factory.__primary__ = 'user-' + str(i)",
            '   user_factory.age = random.randint(15, 25)',
            '   user_factory.save()'
        ],
        show_instruction=show_instruction
    )
    for i in xrange(50):
        user_factory = User()
        user_factory.__primary__ = 'user-' + str(i)
        user_factory.age = random.randint(15, 25)
        user_factory.save()

    # Find user who has age larger than 20 without indexed.
    guide(
        "Find user who has age larger than 20 without indexed.",
        [
            'start_time = time.time()',
            "print 'User range search without indexed:', user.find('age', 20, operator='>', build=False)",
            "print 'User range search without indexed time spend:', time.time() - start_time, 's'"
        ],
        show_instruction=show_instruction
    )
    if show_instruction:
        start_time = time.time()
        print 'User range search without indexed:', user.find('age', 20, operator='>', build=False)
        print 'User range search without indexed time spend:', time.time() - start_time, 's'

    # Find user who has age larger than 20 after indexed.
    guide(
        "Find user who has age larger than 20 after indexed.",
        [
            "user.index('age')",
            'start_time = time.time()',
            "print 'User range search after indexed:', user.find('age', 20, operator='>', build=False)",
            "print 'User range search after indexed time spend:', time.time() - start_time, 's'"
        ],
        show_instruction=show_instruction
    )
    user.index('age')
    if show_instruction:
        start_time = time.time()
        print 'User range search after indexed:', user.find('age', 20, operator='>', build=False)
        print 'User range search after indexed time spend:', time.time() - start_time, 's'
