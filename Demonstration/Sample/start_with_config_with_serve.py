import os
from Database import database

from ConfigureIt.parser import Parser

config_file = os.path.join(os.getcwd(), "database_with_serve.yml")
if not os.path.exists(config_file):
    print(f"Configuration file not found at {config_file}")

class Serve:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

def Serve_Database(
        configuration: database.Database,
        serve: Serve
    ):
    configuration.serve(host = serve.host, port = serve.port)

prsr = Parser(filename=config_file)
prsr(
        module=database,
        custom_mapping = {
            "DatabaseConfiguration": Serve_Database,
            "Serve": Serve
        }
    )
