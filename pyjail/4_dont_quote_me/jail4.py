#!/bin/env python3

# def print_flag():
#   from flag import flag
#   print(flag)

# These pages might be helpful:
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3.12/reference/datamodel.html

print('Please enter some Python code to run!')
code = input()

for banned_word in ['eval', 'exec', 'open', 'import', "'", '"', 'chr']:
    if banned_word in code:
        print(f'{banned_word} is not allowed!')
        exit(0)

print(eval(code))
