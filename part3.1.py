numbers = [5, 4, 3, 2, 1]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("End of list reached")
