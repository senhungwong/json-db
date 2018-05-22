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


# Create an user in thread 1.
user_t1 = User()
user_t1.__primary__ = 'alex'
user_t1.age = 20
user_t1.save()
print "Thread 1 attributes: ", user_t1.attributes()

# Get the user with name in thread 2.
user_t2 = User('alex')

# Update thread 1 user.
user_t1.age = 21
user_t1.save()
print "Thread 1 updated attributes: ", user_t1.attributes()

# Check thread 2 attributes.
print "Thread 2 current attributes: ", user_t2.attributes()

# Sync thread 2
user_t2.sync()
print "Thread 2 attributes after sync: ", user_t2.attributes()

# Add thread 1 age again
user_t1.age += 1
user_t1.save()
print "Thread 1 age add 1: ", user_t1.attributes()

# Sync using save
user_t2.age = 50
user_t2.save()
print "Thread 2 sync before save: ", user_t2.attributes()
