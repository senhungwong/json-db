from jsondb import DB, Model

# create a database object
jsondb = DB()

# create database under storage folder
jsondb.init()

# create type
jsondb.create_type('user')


# create user model
class User(Model):
    """User type model.

    Attributes:
        email (str): The email address of user.
    """

    type = 'users'


# find user who has primary 'alex'
user = User('alex')

# get user's email
print user.email
