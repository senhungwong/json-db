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

    # Create more users.
    guide(
        'Create more users.',
        [
            'user = User()',
            "user.__primary__ = 'senhung'",
            "user.email = '0x53656e@gmail.com'",
            'user.save()'
        ],
        show_instruction=show_instruction
    )
    user = User()
    user.__primary__ = 'senhung'
    user.email = '0x53656e@gmail.com'
    user.save()

    # Create index.
    guide(
        'Create index.',
        [
            "user = User('alex')",
            "user.index('email')"
        ],
        show_instruction=show_instruction
    )
    user = User('alex')
    user.index('email')