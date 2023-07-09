#!/bin/env python3

# The flag is in its own file called "flag.py"

# def print_flag():
#   from flag import flag
#   print(flag)

# This page should have the help you need:
# https://docs.python.org/3/library/functions.html

print('Please enter a line of Python code to run!')
code = input().strip()

if len(code) > 6:
    print("I'm not reading all of that! Give it to me in 6 characters or less.")
    exit(0)

exec(code)
