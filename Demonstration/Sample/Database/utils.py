import random

def generate_password(n):
    # defining the list of choices of characters.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!#$%^&*()"

    """
    The random.sample() method returns a list, so we need to convert it into a string before returning it.
    """

    chosenLetter = random.sample(characters, n)

    # finally converting the list into a string
    password = "".join(chosenLetter)

    return password

class STYLE:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    HEADERBOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def write_in(*data, style = []):
    return "".join(style) + " ".join([str(d) for d in data]) + STYLE.ENDC
