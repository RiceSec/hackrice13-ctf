import random
from secret import flag

print("=== welcome to the lottery game ===")

inp = input(
    "enter up to 5 numbers between 1 and 1,000,000 (exclusive) separated by spaces: "
)

random.seed(len(inp))

nums = list(map(int, inp.split()))
if len(nums) > 5:
    print("too many numbers")
    exit()

for i in range(len(nums)):
    if nums[i] < 1 or nums[i] >= 1_000_000:
        print("number out of range")
        exit()

winning_number = random.randrange(1, 1_000_000)
if winning_number in nums:
    print("you won!")
    print(flag)
else:
    print("you lost :(")
