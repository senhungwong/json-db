# import the main classes from the jsondb module. DB is the one
# that deals with database actions. Model is the one interacts
# with data.
from jsondb import DB, Model

# Create an database object.
jsondb = DB()

# Delete the existing database if it exists.
jsondb.delete(force=True)

# Create the database.
jsondb.init()

# Create a type (table) named users
jsondb.has_type('users')


# Define a class for 'users' mapping.
class User(Model):
    __type__ = 'users'  # set the type to 'users'


# Create a new user object (a new row).
user = User()

# Set the primary (primary key) to 'alex'.
user.__primary__ = 'alex'

# Create an email field for 'alex'.
user.email = '0x53656e@gmail.com'

# Save the user model to database (a new row is been created).
user.save()

# See user's attributes.
print 'User attributes: ', user.attributes()

# Change users' email to something else.
user.email = 'other@gmail.com'

# Save user model to database (the row is been updated).
user.save()

# See changed attributes.
print 'Changed attributes: ', user.attributes()

# See all users' information.
print 'User information: ', user.info()
