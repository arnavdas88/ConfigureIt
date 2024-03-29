.. ConfigureIt documentation master file, created by
   sphinx-quickstart on Fri Jun  9 18:45:37 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

***************************************
Welcome to ConfigureIt's documentation!
***************************************

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`Example`


Introduction
============

ConfigureIt is a powerful Python package designed to simplify
configuration management for industry-grade software applications. It
allows you to easily load and parse configuration files in YAML, TOML,
or JSON format, and automatically create the corresponding objects in
memory. With ConfigureIt, you can effortlessly manage and customize the
configuration of your software, making it highly adaptable to different
environments and deployment scenarios.

Key Features
------------

-  Supports YAML, TOML, and JSON configuration file formats.
-  Automatically creates objects in memory based on the configuration
   file.
-  Simplifies the process of configuring complex software systems.
-  Provides a flexible and intuitive API for easy integration.
-  Promotes code maintainability and separation of configuration from
   implementation.

Installation
------------

You can install ConfigureIt using pip:

.. code:: shell

   $ pip install git+https://github.com/arnavdas88/ConfigureIt

-----




*****
Usage
*****

Using ConfigureIt is straightforward. Here’s an example demonstrating
how to load a configuration file and create objects based on the
configuration:

.. code:: python

   import database
   from ConfigureIt.parser import Parser

   config_file = "database.yml"

   # Create a Parser instance with the configuration file
   syslog = Parser(filename=config_file)

   # Load the 'database' module and create objects based on the configuration
   syslog(module=database) # Mapping the configuration file to the database module

   # Access and use the created objects
   syslog.Database.serve()

In the above example, we import the necessary modules and define the
path to the configuration file (``database.yml``). We then create an
instance of the ``Parser`` class, passing the filename of the
configuration file as a parameter.

Next, we use the ``syslog`` instance to load the ``database`` module and
create objects based on the configuration defined in the file. The
objects are created and stored in memory, ready for use.

Finally, we can access and utilize the created objects, such as calling
the ``serve()`` method on the Database object.


Configuration File
==================

The configuration file (e.g., ``database.yml``) follows the syntax of
the chosen format (YAML, TOML, or JSON) and defines the necessary
settings for your software. Here’s an example of a YAML configuration
file for the ``database`` module:

.. code:: yaml

   Database:
     admin:
       username: AdminUser
       password: MyRandomDummyPassword
     shards: 128
     page_size: 1024
     read_heads: 6
     write_heads: 24
     sequential_write: true

In this example, we define the configuration settings for the
``Database`` object. The admin parameter is further nested to include
the ``username`` and ``password`` properties.

