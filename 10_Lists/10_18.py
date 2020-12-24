sum = 0
for num in [1, 3, 5, 7, 9]:
    sum = sum + num
print(sum)


counter_long_names = 0
for name in ["Joe", "Sally", "Amy", "Brad"]:
    if len(name) > 3:
        counter_long_names += 1
print(counter_long_names)


s = "what if we went to the zoo"
print(s)

num_vowels = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        num_vowels += 1
print(num_vowels)
