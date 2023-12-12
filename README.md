## Table of Contents

- [Goal](#goal)
- [Analysis](#analysis)
  - [Database](#database)
  - [API](#api)
- [Implementation Plan](#implementation_plan)



# Goal
Build a simple REST API using Django, which should allow users to perform the following actions:
- Create a new store
- Retrieve a single store by ID
- Retrieve a list of all stores
- Update an existing store (with all fields)
- Delete an existing store

# Analysis
According to the requirements, only one table will be created and added to the existing database that Django Framework offers.
And inorder to have an API out of this table, i am going to use the Django Serializer to transform data into JSON format.

## Database
One table `Store` is added to the Django default database, consists of the following `Id, Name, Address, Opening_hours`.
## API
In my case, it's necessary to transform the `Store` table data into a JSON data, and this will result in having  4  key/value pairs in each JSON list-item.
The following url /***/ will keep the JOSN form of data.

# Implementation Plan