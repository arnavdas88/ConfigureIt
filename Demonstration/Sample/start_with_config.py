import os
from Database import database

from ConfigureIt.parser import Parser

config_file = os.path.join(os.getcwd(), "database.yml")
if not os.path.exists(config_file):
    print(f"Configuration file not found at {config_file}")

prsr = Parser(filename=config_file)
prsr( module=database, )

prsr.Database.serve()