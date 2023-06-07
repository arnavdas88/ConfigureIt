from src.ConfigureIt.parser import Parser
# from src.ConfigureIt.parser.yaml_parser import ParseYAML
# from src.ConfigureIt.parser.utils import get_object
# from src.ConfigureIt.parser.namespace import Namespace


import sample_class
from sample_class import DummyClass, DummyParam

# parse_yaml = ParseYAML("config.yml")

# obj = get_object(
#             configuration = (
#                 "Dummy",
#                 {"param_a": {"Param": {"param_a": 23}}, "param_b": "HI",}
#             ),
#             mapping={
#                 "Dummy": DummyClass,
#                 "Param": DummyParam
#             },
#         )

# obj.print()

# ns = Namespace(sample_class, )

prsr = Parser(filename="sample.yml")
prsr( module=sample_class, )

prsr.DummyClass.print()
pass