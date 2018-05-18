# JSON DB

## Description

A lightweight NoSQL document database storage mechanism using JSON as the storing type. This is just an idea of a 
way to store data. The database language and DBMS are **NOT** implemented. However, a simple Python example is 
built for demonstrating.

## Basic Idea

Store data in JSON format which is easy to read and compatible for almost all programming languages that supports 
JSON. 

## Database

Database is stored in a folder which has JSON files like `<type>.json`, `schema.json`, ...

## Type

Types (tables) and their properties are stored in `<type>.json`. 

<details>

<summary>Example</summary>

```json
{
    "users": {
        "alex": {
            "birth_year": 1996
        }
    }
}
```

</details>

## Relation

Relations are stored in `<type>.json` under the type object

<details>

<summary>Example</summary>

```json
{
    "users": {
        "alex": {
            "birth_year": 1996,
            "visited": ["canada"]
        }
    }    
}
```

```json
{
    "countries": {
        "canada": {}
    }
}
```

</details>

## Schema

Schema is stored in `schema.json` which specifies types' (table) primary key, ...

Note: compound primary key is not supported, use id instead

<details>

<summary>Example</summary>

```json
{
    "types": {
        "users_uuid": {
            "_type": "users",
            "birth_year": {
                "_datatype": "int"
            },
            "relations": {
                "visited": "countries_uuid"
            }
        },
        "countries_uuid": {
            "_type": "countries"
        }
    }
}
```

</details>

## Accessing

### Read

Reading the data is simple:

```pseudo
/* Get user */
User alex = users.alex;

/* Get property */
int birth_year = alex.birth_year;

/* Get visited countries */
String[] country_names = alex.visited;
```

### Write

```pseudo
/* Get user */
User alex = users.alex

/* Change properties */
alex.birth_year = 1995;
alex.gender = "male";
```

ISSUE: Multiple users write in one database will cause problem
