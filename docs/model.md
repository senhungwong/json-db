# Model

## Module

```python
from jsondb import Model
```

## Build Model

Create a class and extend it with `Model`. The `__type__` field is required.

```python
class User(Model):
    __type__ = 'users'
```

## Init

### Create New Row

```
Initialize object.

If primary is not given, new type object is created. If primary is given,
try to find the .json file in storage and assign attributes to the current
object.

Args:
    primary (str): If given, search data; otherwise create new object.
```

Create an object without specifying any args will create a new data object.
Use `save()` when finished building the object to save it into database.

```python
user = User()
```

### Get a Row

Specifying the primary to get the row and build it as an object.

```python
user = User('alex')
```

## Get All Attributes

`attributes()`

```
Get all attributes in the object.

Returns:
    dict: All attributes in the object.
```

## Save

`save()`

```
Save current object to .json file.

If the row is not found in the folder, create one; otherwise update it.
Also update schema rows.
```

## Info

`info()`

```
Get current type information.

Returns:
    dict: Current type information.
```

## Sync

`sync(force=True)`

```
Sync the current object.

Args:
    force (bool): If true, update the newest data to current object.
        New attributes will be kept, but updated attributes in current
        object are overwritten by the attributes in database. If false,
        will sync newly created attributes in the database, but keep
        all local changes.
```

## Create New Relation

`has_relation(relation, type)`

```
Create a relation for current type.

Args:
    relation (str): The relation name.
    type     (str): Related type name.
```

## Get Relations

`relations(relation)`

```
Get a specific relation data.

Args:
    relation (str): The relation name of the relation.
    
Returns:
    dict: Dict of relation data.
```

## Index An Attribute

`index(attribute)`

```
Create an index of an attribute.

Args:
    attribute (str): Attribute that is going to be indexed.
```

## Lookup An Attribute

`lookup(attribute)`

```
Look up a specific attribute's index.

Args:
    attribute (str): The attribute name that is going to be looked up.
    
Returns:
    dict: Indices of the attribute.
```

## Find and Range Search

`find(attribute, value, operator='=', build=True)`

```
Look up and range search a value.

Args:
    attribute (str) : The attribute name.
    value     (str) : The value that is going to be compared with.
    operator  (str) : The binary comparison operator.
    build     (bool): If result needs to be built or not.
    
Returns:
    list: The list of data that matches the search requirement.
```
