<p align="center"><img src="https://github.com/senhungwong/json-db/blob/master/docs/header.gif" width="55%"></p>

## Description

A lightweight NoSQL document database storage mechanism using JSON as the storing type. 

[Initial idea](docs/initial_idea.md).

## How To Use

Use the following command to see example demo, or go to `examples/*` to see the code.

```bash
$ python example <example>
```

```
<example>:
[database]   : To see database interactions
[model]      : To see how to insert rows and assign/update fields
[relations]  : To see how to add relation to a data
[index]      : To see how to index an attribute
[multithread]: To see how to perform a multi thread task
```

### Details

 - [DB](docs/db.md)

## Storage Structure

```
v1.0.0 file structure

storage/                            # root folder of all databases
└── database/
    ├── data/
    │   └── types/                  # a type (table)
    │       └── primary.json        # a record named using the primary key
    ├── schema/
    │   ├── identifiers.json        # stores all type name + type identifiers
    │   └── types-identifier/
    │       ├── information.json    # the type (table) information
    │       └── relations.json      # type relations with other types
    └── indices/
        └── types-identifier/
            ├── index.json
            └── attribute.json      # indexing file for a type attribute
```

## Problems

The encountered problems and solutions during building the module.

[Problems](docs/problems.md)
