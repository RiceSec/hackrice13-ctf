#!/bin/env python3

import os

with open('flag.txt') as f:
    flag = f.read()

return_code = os.system('./crashme')
if return_code != 0:
    print("Oops! It looks like the program crashed!")
    print("Here's some debugging info:")
    print(f"  FLAG={flag}")
