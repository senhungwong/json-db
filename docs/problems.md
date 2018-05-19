# Problems

**Solved**

 - [Type name changing affecting relations](#type-name-changing-affecting-relations)
 - [Write overhead when table grows](#write-overhead-when-table-grows)

**Unsolved**

 -

## Type name changing affecting relations

<h3>Problem:</h3>

Change type name will result in changing all the relation representation related to the type.

<details>

<summary>Example</summary>

`data/users.json`

```json
{
    "users": {
        "alex": {
            "visited": [
                "country.canada"
            ]
        }
    }
}
```

`data/country.json`

```json
{
    "country": {
        "canada": {}
    }
}
```

By changing the `country` type to `countries` requires search in all other types for associated relations.

</details>

<h3>Solution:</h3>

Add an identifier to each type and assign relations using identifier.

<details>

<summary>Example</summary>

`data/users.json`

```json
{
    "users": {
        "alex": {
            "visited": [
                "canada"
            ]
        }
    },
    "identifier": "users-identifier-unique-str"
}
```

`data/country.json`

```json
{
    "country": {
        "canada": {}
    },
    "identifier": "countries-identifier-unique-str"
}
```

`schema/countries-identifier-unique-str.json`

```json
{
    "type": "country"
}
```

`schema/users-identifier-unique-str.json`

```json
{
    "type": "users",
    "relations": {
        "visited": "countries-identifier-unique-str"
    }
}
```

When search relations, first look into the schema file and see relations identifier.

Then go to the relations schema based on the identifier and get the relation type name.

Changing the type name now will not lead to a change in identifier which does not require 
a relationship representation change.

</details>

## Write overhead when table grows

<h3>Problem:</h3>

When one table grows, a small cell change will lead to re-write the whole `types.json` file.

<h3>Solution:</h3>

Convert `types.json` to a `types/` folder. Every row of data is stored in `types/primary.json`.

It increases the write speed (write only a small piece of table instead of copying & pasting all table data), 
and supports multiple writes in one table (two users can write to the table but different row at the same time). 

<details>

<summary>Example</summary>

`users/alex.json`

```json
{
    "email": "0x53656e@gmail.com"
}
```

Store existing rows in `schema/users-indentifier/users.json` as follow enable fast check if row exists and 
show all rows.

```json
{
    "alex": null
}
```

</details>
