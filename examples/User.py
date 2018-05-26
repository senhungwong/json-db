from jsondb import Model


# Define a class for 'users' mapping.
class User(Model):
    __type__ = 'example.storage.database.users'  # set the type to 'users'
