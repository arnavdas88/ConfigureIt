from typing import List, Mapping, AnyStr, Any

def get_object( configuration:Mapping, mapping:Mapping[str, object], ) -> Any:
    """Builds and returns an object based on the provided configuration and mapping dictionaries.

    The `get_object` function takes a dictionary called `configuration` and a dictionary called `mapping`. It uses the
    `configuration` dictionary to load the names of variables and builds the object by mapping the variable names to
    their corresponding classes defined in the `mapping` dictionary.

    Parameters
    ----------
    configuration : Mapping
        A dictionary mapping of parameter attributes to be passed to the class constructor/function. It can contain
        nested attributes, in order to pass objects instead of native data types.

        Example
        -------
        A mapping of `{"param_a": 5, "param_b": "HI"}` will create a class like
        ```python
        class(
            param_a = 5,
            param_b = "HI"
        )
        ```

        A mapping of `{"param_a": {"Param": {"param_a": 23}}, "param_b": "HI",}` will create a class like
        ```python
        class(
            param_a = DummyParam(param_a = 23),
            param_b = "HI"
        )
        ```
    mapping : Mapping[str, object]
        A dictionary mapping of names associated with their classes.

        Example
        -------
        A mapping `{"Dummy": DummyClass, "Param": DummyParam}` will let the "Dummy" key of the `configuration` map to the
        `DummyClass()` class, and the "Param" key to the `DummyParam()` class.


    Returns
    -------
    The constructed object based on the provided configuration.

    Example
    -------
    To create a `DummyClass` class object, equivalent to `DummyClass(param_a = 5, param_b = "HI")`, the `get_object`
    will look like as follows,
    ```python
    >>> get_object(
            configuration = (
                "Dummy",
                {"param_a": 5, "param_b": "HI"}
            ),
            mapping={
                "Dummy": DummyClass
            }
        )
    <DummyClass object at 0x7f7d4c82c310>
    ```
    """
    object_type, keyword_arguments = configuration
    object_class = mapping[object_type]

    # argument_mapping
    kwargs = keyword_arguments if keyword_arguments else {}
    # proposition = create_class_proposition(object_class, kwargs.keys())
    for key, value in kwargs.items():
        if type(value) is dict:
            object = [ get_object((k, v), mapping ) for k, v in value.items() ]
            if len(object):
                kwargs[key] = object[0]
        elif key in mapping:
            kwargs[key] = mapping[key][value]()

    return object_class(**kwargs)

from enum import Enum, StrEnum

class AttributeType(StrEnum):
    Constructor = "CONST"
    Function = "DEF"

def create_class_proposition(object_class, keys):
    proposition = {
        AttributeType.Constructor: [],
        AttributeType.Function: []
    }
    for (_type_, _key_) in segregate_class_attribute_types(object_class, keys):
        proposition[_type_].append(_key_)

    return proposition

def segregate_class_attribute_types(object_class, keys):
    constructor_parameters = object_class.__init__.__annotations__
    function_definitions = [ def_name for def_name in dir(object_class) if not def_name.startswith("__") ]

    constructor = {}
    function = {}

    for key in keys:
        if key in constructor_parameters:
            yield ( AttributeType.Constructor, key )
        elif key in function_definitions:
            yield (AttributeType.Function, key)
