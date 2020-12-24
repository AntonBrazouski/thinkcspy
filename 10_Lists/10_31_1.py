# Draw a reference diagram for a and b before and after the third line
# of the following python code is executed:
a = [1, 2, 3]
b = a[:]
print("before")
print(f"a == b {a==b} " )
print(f"a is b {a is b} ")

b[0] = 5
print("b[0] = 5")

print("after")
print(f"a == b {a==b} " )
print(f"a is b {a is b} ")
