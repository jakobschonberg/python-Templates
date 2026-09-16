s = input().split()
v = map(int, s)
p = all(i > 0 for i in v) and any(j == j[::-1] for j in s)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
values = [None, True, False, False, None, False, True, True]

combined_list = [*letters, *values]
def mod4(number):
  return number % 4
sorted_numbers = sorted(numbers, key = lambda number: mod4(number)) #sort with lambda (takes function)

first, *rest, last = numbers
doubled_numbers = [2 * numbers for number in numbers]
evens = filter(lambda x: x % 2 == 0, numbers)
evens = [number for number in numbers if number % 2 == 0]
set_evens_mod3 = {number % 3 for number in numbers if number % 2 == 0}
squares = {number: number ** 2 for number in numbers}
doubled_squares = {key: value * 2 for key, value in squares.items()}
fruits = ['apple', 'banana', 'cherry']
lengths = list(map(lambda x: len(x), fruits))
 

#generators:
gen = (number * 2 for number in numbers) #will not create a tuple but rather a generator expression

#zip
for number, letter, value in zip(numbers, letters, values):
  print(number, letter, value)
my_dict = dict(zip(numbers, letters))

