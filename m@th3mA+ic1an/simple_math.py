#!/bin/env python3

import random
import time

FLAG = "hackrice{yay!_completed_elementary_school!!}"
def game_logic():
    s = 0
    print(("To get this flag, I'll need to you do some math.\n Actually - a lot of them. Don't be nervous - it's just elementary" +
    "school level math.\nI'll let you use a calculator.\n"))
    while s < 1000:
        prompt = generate_random_eq()
        print(prompt[0])
        start_time = time.time()
        response = input(">> ")
        end_time = time.time()
        response_time = end_time - start_time
        if int(response) == prompt[1] and response_time <= 3:
            s += 1
        else:
            if int(response) != prompt[1]:
                print("I don't think that's right...\n")
            elif response_time > 3:
                print("You are too slow\n") 
    print(f"Very impressive. Here is the flag {FLAG}")

def generate_random_eq():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    operator = random.randint(0, 3)
    if (operator == 0):
        return [f"What is {x} * {y}?", x * y]
    elif (operator == 1):
        return [f"What is {x} % {y}?", x % y]
    elif (operator == 2):
        return [f"What is {x} + {y}?", x + y]
    elif (operator == 3):
        return [f"What is {x} - {y}?", x - y]

game_logic()
