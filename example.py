from jsondb import DB, Model

# create a database object
jsondb = DB()

# create database under storage folder
jsondb.init()

# create type
jsondb.create_type('user')


# create user model
class User(Model):
    type = 'users'


# create a new user
user = User()
user.__primary__ = 'alex'
user.data['email'] = '0x53656e@gmail.com'
user.save()

# find user who has primary 'alex'
user = User('alex')

# update user's location
user.data['location'] = 'Vancouver'
user.save()
