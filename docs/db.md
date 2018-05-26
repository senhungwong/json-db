# DB

## Module

```python
from jsondb import DB
```

## Initialize DB Object

Create a database object for handling all the database actions.
Database configuration can be set in .jsondb.ini file. **storage**
name is the root directory name of the database. **database** is the
default database name. You can also create multiple databases by
first setting a new variable in .jsondb.ini. Then create the
database object using `DB(database_name=your_db_variable)` and then
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

### Structure

```
storage/
└── database/
    ├── data/
    ├── schema/
    │   └── identifiers.json
    └── indices/
```

## Delete

The delete function removes database if it exists.

```python
jsondb.delete()
```

### Parameters

```
force (bool): If true, will remove the folder in force mode.
```

## Create Types

Create a type (table). The has_type function will
automatically convert singular to plural noun so all types follow
the same naming convention. You can force it to set the input name
as a type by using `has_type('typename', , pluralize=False)`

```python
jsondb.has_type('type_name')
```

### Parameters

```
type_name     (str) : The type name. Will be set to plural and lowercase if pluralize is True.
if_not_exists (bool): Skip if the type already exists.
pluralize     (bool): Standardize type names to plural and lowercase.
```

### Structure

```
storage/
└── database/
    ├── data/
    │   └── types/
    │       └── primary.json
    ├── schema/
    │   ├── identifiers.json
    │   └── types-identifier/
    │       ├── information.json
    │       └── relations.json
    └── indices/
        └── types-identifier/
            ├── index.json
            └── attribute.json
```

## Read

`read(path)`

```
Read specific file in database.

Attributes:
    path (str): The path to .json file (excluding storage/database).

Returns:
    dict: The content in dict format.
```

## Create

`create(name, path, content)`

```
Create a .json file in database.

Args:
    name    (str) : The name of the .json file.
    path    (str) : The path of the .json file.
    content (dict): The content that is going to be written in .json file.
```

## Write

`write(path, content)`

```
Write to a .json file in database.

Args:
    path    (str) : The path to .json file (excluding storage/database).
    content (dict): The content that is going to be written in .json file.
```

## Get Hash

`get_hash(path)`

```
Get the hash value.

Args:
    path (str): The file path.

Returns:
    str: The hash value.
```
