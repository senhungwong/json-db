# JSONDB

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
[assign]     : To see how to insert rows and assign/update fields
[relations]  : To see how to add relation to a data
[multithread]: To see how to perform a multi thread task
```

### Details

 - [DB](docs/db.md)

## Storage Structure

```
v1.0.0 file structure

storage/
└── database/
    ├── data/
    │   ├── types-1/
    │   │   ├── primary-1.json
    │   │   └── primary-2.json
    │   └── types-2/
    │       ├── primary-1.json
    │       └── primary-2.json
    ├── schema/
    │   ├── identifiers.json
    │   ├── types-1-identifier/
    │   │   ├── information.json
    │   │   └── relations.json
    │   └── types-2-identifier/
    │       ├── information.json
    │       └── relations.json
    └── indices/
        ├── types-1-identifier/
        │   ├── attribute-1.json
        │   └── attribute-2.json
        └── types-2-identifier/
            ├── attribute-1.json
            └── attribute-2.json
```

## Problems

The encountered problems and solutions during building the module.

[Problems](docs/problems.md)
