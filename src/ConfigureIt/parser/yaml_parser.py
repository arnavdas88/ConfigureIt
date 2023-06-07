from .utils import get_object
from .namespace import Namespace

import warnings
import yaml

class ParseYAML():
    def __init__(self, file="config.yaml") -> None:
        self.file = file

    @property
    def to_dict(self, ):
        with open(self.file, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                warnings.warn(exc)
