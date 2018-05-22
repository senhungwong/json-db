# DB

## Module

```python
from jsondb import DB
```

## Initialize DB Object

Create a database object for handling all the database actions.
Database configuration can be set in .jsondb.ini file. [storage]
name is the root directory name of the database. [database] is the
default database name. You can also create multiple databases by
first setting a new variable in .jsondb.ini. Then create the
database object using DB(database_name=your_db_variable) and then
perform actions on that object.

```python
jsondb = DB()
```
### Parameters

```
database_name (str): Set current instance to a specific database. Default 'database'
storage       (str): The jsondb storage folder name for initializing FileManager. Default 'storage'
section       (str): The section name of the configurations (the one wrapped in []). Default 'jsondb'
```

## Create Database

The init function creates database under the storage folder. If
the database already exists, there will be an error informing
the database existence.

```python
jsondb.init()
```

## Delete

The delete function removes database if it exists. It is used
here so that this script can be called multiple times since every
time the old database will be removed, then there's no database
already exists error when creating the database.

```python
jsondb.delete()
```

## Create Types

Create a type (table) named users. The has_type function will
automatically convert singular to plural noun so all types follow
the same naming convention. You can force it to set the input name
as a type by using .has_type('typename', , pluralize=False)

```python
jsondb.has_type('type_name')
```
