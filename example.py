from jsondb import DB, Model

# create a database object having database name 'example_db' under example storage
jsondb = DB('example_db', 'example')

# create database called example_db under example folder
jsondb.init()

# create type
jsondb.create_type('user')


# create user model
class User(Model):
    """User type model.

    Attributes:
        email (str): The email address of user.
    """

    storage = 'example'
    database = 'example_db'
    type = 'users'


# find user who has primary 'alex'
user = User('alex')

# get user's email
print user.email
