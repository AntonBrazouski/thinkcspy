a = 'a'
b = 'b'

temp = a
a = b
b = temp

(a,b) = (b,a)

# (a, b, c, d) = (1, 2, 3)
# ValueError: need more than 3 values to unpack
