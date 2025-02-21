def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x.upper(), "hello"))
