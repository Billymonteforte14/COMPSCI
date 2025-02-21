def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return "Error: Invalid input, cannot convert to integer"

print(parse_int("123"))
print(parse_int("abc"))
