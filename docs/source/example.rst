.. _Example:

Example
=======

Let's explore an example of how to use the package with a Database class.

A Database Example
------------------

In this example, a Database object named `syslog` is created with specific parameter values.
The :code:`admin` parameter is initialized with custom :code:`AdminCredentials` values,
and other parameters are set accordingly. Finally, the serve method of the `syslog` object
is called to start serving the database on a specified `host` and `port`.

Here we will assume that some the the functions like :code:`generate_password()`
are already defined. Let's consider a use case where you have an application code for a database,
that looks like,

.. code:: python

    class AdminCredentials:
        def __init__(self, username: str = "admin", password: str = None):
            self.username = username
            self.password = password if password else generate_password(12)


.. code:: python

    class Database:
        def __init__(self,
                    admin: AdminCredentials = AdminCredentials(),

                    shards: int = 512,
                    page_size: int = 4096,

                    read_heads: int = 12,
                    write_heads: int = 12,

                    l1cache: int = 128,
                    l2cache: int = 128,

                    backup: int = 24 * 7,

                    sequential_write: bool = False
                    ):
            # Here goes the code for the database constructor.
            ...
            ...

        def serve(self, host = "127.0.0.1", port = 8000):
            # Here goes the code for the server listener.
            ...
            ...

Here is an example of manually configuring the Database class using the provided parameters:

.. code:: python

    from database import Database, AdminCredentials

    syslog = Database(
        admin = AdminCredentials(
            username="AdminUser",
            password="MyRandomDummyPassword"
        ),
        shards = 128,
        page_size = 1024,
        read_heads = 6,
        write_heads=24,
        sequential_write = True
    )

    syslog.serve(
        host = "127.0.0.1",
        port=4444
    )

To simplify the configuration process, the package provides a :code:`Parser` class that
automatically loads the configuration from a YAML / TOML / JSON file and creates the
corresponding objects.

Here's an example of using :code:`Parser` to configure the Database class:

.. code:: yaml

    Database:
        admin:
            AdminCredentials:
                username: AdminUser
                password: MyRandomDummyPassword
        shards: 128
        page_size: 1024
        read_heads: 6
        write_heads: 24
        sequential_write: true

.. code:: python

    import database
    from ConfigureIt.parser import Parser

    config_file = "database.yml"

    syslog = Parser(filename=config_file)
    syslog( module=database, )

    syslog.Database.serve(
        host = "127.0.0.1",
        port=4444
    )

By utilizing the :code:`Parser` class, developers can easily maintain and modify
configuration settings in a separate YAML file, reducing the need to modify code
directly. This approach enhances code maintainability and facilitates customization
for different environments or deployments.