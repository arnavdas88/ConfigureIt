from typing import Any
from .yaml_parser import ParseYAML
from .utils import get_object
from .namespace import Namespace

from enum import Enum, StrEnum

class ConfigType(Enum):
    JSON = "json"
    YAML = "yaml"
    TOML = "toml"

class Parser:
    """ A class that parses the entire namespace of a given module.

    The Parser class provides functionality to parse the namespace of a module, allowing inspection and manipulation of
    its attributes, classes, functions, and variables.

    Parameters
    ----------
    filename : str, optional
        The filename of the configuration file to use, by default "config.yml"
    filetype : ConfigType, optional
        The type of configuration file parser to use, by default ConfigType.YAML

    Attributes
    ----------
    filename : str
        The filename of the configuration file
    filetype : ConfigType
        The type of configuration file parser

    Methods
    -------
    __init__
        Initializes a Parser object.
    __call__
        Parses the namespace of a module.

    Examples
    --------
    ```python
    prsr = Parser(filename="sample.yml")
    prsr(module=sample_class)
    ```
    """
    def __init__(self, filename = "config.yml", filetype:ConfigType=ConfigType.YAML) -> None:
        """Initialize a Parser object.

        Parameters
        ----------
        filename : str, optional
            The filename of the configuration file to use, by default "config.yml"
        filetype : ConfigType, optional
            The type of configuration file parser to use, by default ConfigType.YAML
        """
        self.filename = filename
        self.filetype = filetype

    def __call__(self, module, custom_mapping = {}) -> None:
        """__call__ Parse the namespace of a module.

        This method parses the namespace of a given module and allows inspection and manipulation of its attributes,
        classes, functions, and variables.

        Parameters
        ----------
        module : module
            The module to parse.
        custom_mapping : dict, optional
            A custom mapping to use for attribute name translations, by default {}
        """
        config = ParseYAML(self.filename)
        ns = Namespace(module, )
        for key, value in config.to_dict.items():
            self.__setattr__(
                key,
                get_object(
                        configuration = (key, value),
                        mapping={ **ns.namespace, **custom_mapping },
                    )
            )

