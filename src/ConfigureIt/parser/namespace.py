from types import ModuleType
from typing import Callable
from inspect import isclass

not_an_internal_variable = lambda x: not x.startswith('_')
not_a_module = lambda x: (not isinstance(x, ModuleType))
not_a_function = lambda x: not (not isclass(x) and callable(x))
not_a_singleton = lambda x: type(x) not in [int, list, dict, str, float]

def default_filter(x, y):
    return not_an_internal_variable(x) and not_a_module(y) and not_a_function(y)

class Namespace:
    """ A class that loads and filters the public elements of an imported module.

    The Namespace class is used to load and filter the public elements of an imported module. It provides a way to
    inspect and access functions, classes, and other non-singleton objects defined in the module.

    Parameters
    ----------
    package : module
        The imported module to load the namespace from
    filter : Callable, optional
        A filter function to selectively include elements in the namespace, by default default_filter

    Attributes
    ----------
    namespace : dict
        The dictionary that holds the filtered elements of the module's namespace.

    Methods
    -------
    __init__
        Initializes a Namespace object.

    Examples
    --------
    ```python
    import my_module

    ns = Namespace(my_module, filter = ... )
    ```
    """

    def __init__(self, package, filter:Callable = default_filter) -> None:
        """__init__ Initialize a Namespace object.

        This method loads and filters the public elements of the provided `package` module, populating the `namespace`
        dictionary with the filtered elements.

        Parameters
        ----------
        package : module
            The imported module to load the namespace from
        filter : Callable, optional
            A filter function to selectively include elements in the namespace, by default default_filter
        """
        self.namespace = {}
        for key, value in package.__dict__.items():
            # name = name_of_global_obj(key)
            if key is not None and not key.startswith('__'):
                if filter:
                    if not filter(key, value, ):
                        continue
                self.namespace [key] = value