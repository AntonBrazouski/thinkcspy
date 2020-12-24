
gg = list(((1.0,0),{0:['a']}))
print(gg)
# gg = list((1.0,0),{0:['a']}) # TypeError: list expected at most 1 argument, got 2
gg = {0:'a', 1:'b'}
gg = list(gg)
print(gg)
