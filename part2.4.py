def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    finally:
        print("Division attempted")

print(safe_divide(10, 2))
print(safe_divide(10, 0))
