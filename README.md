
- [Goal](#goal)
- [Analysis](#analysis)
  - [Database](#database)
  - [API](#api)
- [Implementation Plan](#implementation-plan)
- [Test scenario](#test-scenario)
- [Validation](#validation)
- [Development](#development)


# Goal
Build a simple REST API using Django, which should allow users to perform the following actions:
- Create a new store
- Retrieve a single store by ID
- Retrieve a list of all stores
- Update an existing store (with all fields)
- Delete an existing store

# Analysis
According to the requirements, only one table will be created and added to the existing database that Django Framework offers.
And inorder to have an API out of this table, i am going to use the Django Serializer to transform model data into JSON format.

## Database
One table is added to the Django default database, named `Store`, consists of the following fields `Id, Name, Address, Opening_hours`.

## API
In my case, it's necessary to transform the `Store` table data into a JSON data, and this will result in having  4  key/value pairs in each JSON list-item.
The following url /***/ will keep the JOSN form of data.

# Implementation Plan
1. Set the environment, create .venv file, install the following libraries ().
2. Create django project, name it `storeAPI`.
3. create new model in models.py , name it  `Store`, add the following fields (Id, Name, Address, Opening_hours).
4. define a serializer method in serializers.py.
5. define the following views in the views.py (consider error catch).
6. Add the following urls in the urls.py (views , not found ...etc)
7. Add the `storeAPI` project to the list of apps in settings.py.
8. Secure the API with Django Rest Framework's TokenAuthentication
9. Define a method to filter the list **********
10. Define a method to consider paging in case of long list of items.
11. Consume the `storeAPI`

# Test scenario
1. Run the server, and add the resulted link to the list of Allowed_urls in the settings.py
2. With the use of Postman, do the following tests using the following link
    - choose GET, as a result all items will be listed in JSON format.
    - choose GET and add `/<int>` : `the int must be an existing ID`  to the end of the same url, as a result only the mean item details will be displayed.
    - choose PUT, enter key/value pairs for the following `Name, Address, Opening_hours`, as a result the new item will be added to the list and displayed as well with a new ID.
    - choose DELETE, and add `/<int>` : `the int must be an existing`  to the end of the same url, the mean item should be no more exist in the list.
3. Try to add random ending to the url, not found message will be displayed.


# Validation
- Testing against python files has been perfomed using Python Linter, the following are the results.....(TO DO )

# Development

## Clone
Changes made to a cloned repository will affect the original one.

- Navigate to the main page of the repostitory (this could be a forked instance)
- Click on the **Code** dropdown menu above the list of files
- Choose a method to copy the URL for the repository: either via **HTTPS**, by using an **SSH key**, or by using **GitHub CLI**
- In your work environment, open Git Bash and change current directory to target location for cloned repository
- Type ``git clone`` followed by the copied URL and press enter **Enter**

## Fork

Any changes made to a forked repository do not affect the original repository.

- Log into GitHub and click on repository to download ([FoodTrack_Assessment](https://github.com/Nazek-Altayeb/FoodTrack_Assessment))
- Click the **Fork** buttonin the top right-hand corner
- Select a different owner if necessary
- Click **Create Fork**
- The repo is now in your chosen account and can be cloned or changed:

# Aknowledgement

- I programmed the project my self.
- I benefit from my recent experience in programming backend using Django REST Framework.