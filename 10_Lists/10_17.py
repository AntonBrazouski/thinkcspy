# lists and for loops
fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits: # by item
    print(afruit)

print('\n')
cars = ["bmw", "tesla", "porsche", 'nissan']
for position in range(len(cars)): # by index
    print(cars[position])

print('\n')
for number in range(20):
    if number % 3 == 0:
        print(number)

print('\n')
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print(numbers)
