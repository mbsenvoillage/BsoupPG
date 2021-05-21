
from os import error
from datetime import datetime

def format_error(e):
    return f'\n{datetime.now()}: {repr(e)}'

def log(e):
    try:
        with open('log.txt', 'a') as f:
            f.write(format_error(e))
    except IOError as e:
        print(e)
    except e:
        print(e)