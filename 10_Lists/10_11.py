a = [81, 82, 83]
b = [81, 82, 83]

print(a == b)
print(a is b)

b = a

print( a == b )
print(a is b)

b[0] = 5
print(a)
