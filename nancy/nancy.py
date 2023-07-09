from secret import flag

print(
    r"""

    __  __           __   ____  _           __________________
   / / / /___ ______/ /__/ __ \(_)_______  / ____/_  __/ ____/
  / /_/ / __ `/ ___/ //_/ /_/ / / ___/ _ \/ /     / / / /_
 / __  / /_/ / /__/ ,< / _, _/ / /__/  __/ /___  / / / __/
/_/ /_/\__,_/\___/_/|_/_/ |_/_/\___/\___/\____/ /_/ /_/

  """
)
print()

string = input(f"enter a string in the HackRiceCTF flag format: ")

if string.startswith("hackrice{") and string.strip().endswith("}"):
    print("you got it! here's the real flag:", flag)
else:
    print("oops. try again. remember, the flag format is hackrice{...}")
