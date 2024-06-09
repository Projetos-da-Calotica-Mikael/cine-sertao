import re
from random import random

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def clear():
    print('\033c')

def generate_id():
    return str(random()).split('.')[1]
