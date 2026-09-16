s = input().split()
v = map(int, s)
p = all(i > 0 for i in v) and any(j == j[::-1] for j in s)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
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
