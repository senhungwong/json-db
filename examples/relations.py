from examples.model import model_guide
from User import User
from Country import Country
from examples import guide


def relation_guide(show_instruction=True):
    # Create an user node for relation instruction.
    guide(
        'Create an user node for relation instruction. See more using `$ python example model`',
        start=True,
        show_instruction=show_instruction
    )
    model_guide(show_instruction=False)

    # Create a country.
    guide(
        'Create a country.',
        [
            'country = Country()',
            "country.__primary__ = 'Canada'",
            'country.save()'
        ],
        show_instruction=show_instruction
    )
    country = Country()
    country.__primary__ = 'Canada'
    country.continent = 'North America'
    country.save()

    # Get user object created from model tutorial.
    guide(
        'Get user object created from model tutorial.',
        "user = User('alex')",
        show_instruction=show_instruction
    )
    user = User('alex')

    # Create a relation in user.
    guide(
        'Create a relation in user.',
        "user.has_relation('visited_countries', 'countries')",
        show_instruction=show_instruction
    )
    user.has_relation('visited_countries', 'countries')

    # Assign a country to user.
    guide(
        'Assign a country to user.',
        [
            'user.visited_countries.append(country.__primary__)',
            'user.save()',
            'print "User visited countries: ", user.visited_countries'
        ],
        show_instruction=show_instruction
    )
    user.visited_countries.append(country.__primary__)
    user.save()
    print "User visited countries: ", user.visited_countries

    # Get all visited countries as a list.
    guide(
        'Get all visited countries as a list.',
        'print "User visited countries as a list:", user.visited_countries',
        show_instruction=show_instruction
    )
    print "User visited countries as a list:", user.visited_countries

    # Get all visited countries data.
    guide(
        'Get all visited countries data.',
        "print 'User visited countries data:', user.relations('visited_countries')",
        show_instruction=show_instruction
    )
    print 'User visited countries data:', user.relations('visited_countries')
