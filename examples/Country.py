from jsondb import Model


# Define a class for 'countries' mapping.
class Country(Model):
    __type__ = 'example.storage.database.countries'  # set the type to 'countries'
