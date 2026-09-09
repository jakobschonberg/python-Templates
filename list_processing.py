s = input().split()
v = map(int, s)
p = all(i > 0 for i in v) and any(j == j[::-1] for j in s)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers)

fruits = ['apple', 'banana', 'cherry']
lengths = list(map(lambda x: len(x), fruits))
