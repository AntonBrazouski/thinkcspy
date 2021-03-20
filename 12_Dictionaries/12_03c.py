# dictionary methods
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k, v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "taht maps to", inventory[k])
    
