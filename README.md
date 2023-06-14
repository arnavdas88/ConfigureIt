# ConfigureIt: Automatic Configuration Management for Python
![GitHub repo size](https://img.shields.io/github/repo-size/arnavdas88/ConfigureIt)
[![License](https://img.shields.io/github/license/arnavdas88/ConfigureIt)](https://github.com/arnavdas88/ConfigureIt/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


ConfigureIt is a powerful Python package designed to simplify configuration management for industry-grade software applications. It allows you to easily load and parse configuration files in YAML, TOML, or JSON format, and automatically create the corresponding objects in memory. With ConfigureIt, you can effortlessly manage and customize the configuration of your software, making it highly adaptable to different environments and deployment scenarios.

## Key Features

- Supports YAML, TOML, and JSON configuration file formats.
- Automatically creates objects in memory based on the configuration file.
- Simplifies the process of configuring complex software systems.
- Provides a flexible and intuitive API for easy integration.
- Promotes code maintainability and separation of configuration from implementation.

## Installation

You can install ConfigureIt using pip:

```shell
$ pip install git+https://github.com/arnavdas88/ConfigureIt
```

## Usage

Using ConfigureIt is straightforward. Here's an example demonstrating how to load a configuration file and create objects based on the configuration:

```python
import database
from ConfigureIt.parser import Parser

config_file = "database.yml"

# Create a Parser instance with the configuration file
syslog = Parser(filename=config_file)

# Load the 'database' module and create objects based on the configuration
syslog(module=database) # Mapping the configuration file to the database module

# Access and use the created objects
syslog.Database.serve()
```

In the above example, we import the necessary modules and define the path to the configuration file (`database.yml`). We then create an instance of the `Parser` class, passing the filename of the configuration file as a parameter.

Next, we use the `syslog` instance to load the `database` module and create objects based on the configuration defined in the file. The objects are created and stored in memory, ready for use.

Finally, we can access and utilize the created objects, such as calling the `serve()` method on the Database object.
## Configuration File

The configuration file (e.g., `database.yml`) follows the syntax of the chosen format (YAML, TOML, or JSON) and defines the necessary settings for your software. Here's an example of a YAML configuration file for the `database` module:

```yaml
Database:
  admin:
    username: AdminUser
    password: MyRandomDummyPassword
  shards: 128
  page_size: 1024
  read_heads: 6
  write_heads: 24
  sequential_write: true
```

In this example, we define the configuration settings for the `Database` object. The admin parameter is further nested to include the `username` and `password` properties.

## Contributing

Contributions are welcome! If you encounter any issues, have suggestions, or would like to contribute to the project, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

ConfigureIt is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

This package was inspired by the need for efficient and flexible configuration management in modern software development. We would like to thank the open-source community for their invaluable contributions and support.

## Contact

If you have any questions, suggestions, or feedback, please don't hesitate to reach out to our team at arnav.das88@gmail.com .