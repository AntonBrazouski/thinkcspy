# dictionary operations

# delete item
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

del inventory['pears']

# another way
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

inventory['pears'] = 0


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['bananas'] = inventory['bananas'] + 200

numItems = len(inventory)
