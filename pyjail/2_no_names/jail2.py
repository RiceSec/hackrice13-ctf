#!/bin/env python3

# def print_flag():
#   from flag import flag
#   print(flag)

print('Please enter some Python code to run!')
code = input()

banned_funcs = [eval, exec, open]
for banned_function in banned_funcs:
    if banned_function.__name__ in code:
        print(f'"{banned_function.__name__}" is not allowed!')
        exit(0)

print(eval(code))
