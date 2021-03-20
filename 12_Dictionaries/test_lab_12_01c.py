from lab_12_01c import countAll
from test import testEqual

testEqual(countAll('aaaaaaaaaaaaaaa'), {'a':15})
testEqual(countAll('aab'), {'a':2, 'b':1})
testEqual(countAll('abcabccbae'), {'a':3, 'b':3, 'c':3, 'e':1})
testEqual(countAll('1231'), {'1':2, '2':1, '3':1})
