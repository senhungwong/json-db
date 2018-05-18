from jsondb import DB

# create a database object having database name 'example_db' under example storage
jsondb = DB('example_db', 'example')

# create database called example_db under example folder
jsondb.init()

# create type
jsondb.create_type('user')
