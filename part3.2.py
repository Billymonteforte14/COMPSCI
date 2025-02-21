words = ["william", "basketball", "soccer"]
iterator = (word.upper() for word in words)

for word in iterator:
    print(word)
