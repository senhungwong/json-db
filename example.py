from jsondb import DB, Model

# create a database object
jsondb = DB()

# remove database if exist for testing
jsondb.delete(force=True)

# create database under storage folder
jsondb.init()

# create type
jsondb.create_type('user')


# create user model
class User(Model):
    __type__ = 'users'


user = User()
user.__primary__ = 'alex'
user.email = 'alexwongsenhung@gmail.com'
user.save()

print user.attributes()
user.email = 'something else'
user.save()

print user.info()
