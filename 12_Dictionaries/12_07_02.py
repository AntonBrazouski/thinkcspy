# a
d = {'apples': 15, 'bananas': 35, 'grapes': 12}
try:
    d['banana'] # key error
except(KeyError):
    print('key error')

# b
d['oranges'] = 20
print(len(d)) # 4

# c
print('grapes' in d) # True

# d
try:
    print(d['pears']) #
except(KeyError):
    print('KeyError')

# e.
print(d.get('pears', 0)) # 0

# f.
fruits = d.keys()
try:
    fruits.sort() # attribute error - try sorted(fruits)?
except(AttributeError):
    print('AttributeError')

print(fruits) # apples,bananas, grapes, oranges

# g.
del d['apples']
print('apples' in d) # False
