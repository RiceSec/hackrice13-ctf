#!/bin/env python3

import re

# The flag is in its own file called "flag.py"

# def print_flag():
#   from flag import flag
#   print(flag)

print('Please enter a line of Python code to run!')
code = input().strip()

if re.match(r'import', code) or re.match(r'from.*import', code):
    print("Imports are not allowed!")
    exit(0)
elif 'open' in code:
    print("open() is not allowed!")
    exit(0)

exec(code)
