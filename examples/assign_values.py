import db
from User import User

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
