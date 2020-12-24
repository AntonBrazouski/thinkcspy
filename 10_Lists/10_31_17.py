import random

def create_randlist():
    randlist = []
    for i in range(100):
        randlist.append(random.randrange(0,1001))
    return randlist


print(create_randlist())
