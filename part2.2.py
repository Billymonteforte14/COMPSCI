def check_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a positive integer")

try:
    check_age(25)
    check_age(-5)
except ValueError as e:
    print(e)

try:
    check_age("twenty")
except ValueError as e:
    print(e)
