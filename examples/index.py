from examples.model import model_guide
from User import User
from Country import Country
from examples import guide


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
            "user.index('age')",
            "print 'User email indices:', user.lookup('email')"
        ],
        show_instruction=show_instruction
    )
    user = User('alex')
    user.index('email')
    user.index('age')
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
