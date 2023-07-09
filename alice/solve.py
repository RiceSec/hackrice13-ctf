import re
import requests

ENDPOINT = "http://ctf.hack.rice.edu:51020"

curr = "index"
body = ""

while True:
    print(curr)

    r = requests.get(f"{ENDPOINT}/{curr}.html")
    body = r.text

    if "hackrice" in body:
        break

    p = re.compile('href="/([^".]+)\.html"')
    [curr] = p.findall(body)

print(body)
