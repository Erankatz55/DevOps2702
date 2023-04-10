# 1

import requests
repo = requests.get("https://api.github.com/users/avielb/repos")
assert len(repo.json()) > 5

# 2


import random
import requests


names = ["moshe", "avi", "nofar", "uri", "guy", "udi", "ofir", "michael"]
count = 0
while count < 3:
    count +=1
    name = random.choice(names)
    agi = int(requests.get("https://api.agify.io/?name=", name))
    assert



