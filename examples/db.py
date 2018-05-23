# import the main classes from the jsondb module. DB is the one
# that deals with database actions.
from jsondb import DB

# Create an database object.
jsondb = DB()

# Delete the existing database if it exists for reusing scripts.
jsondb.delete(force=True)

# Create the database.
jsondb.init()

# Create a type (table) named users
jsondb.has_type('users')

# Create another type named countries
jsondb.has_type('countries')
