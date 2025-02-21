def join_words(*words):
    return ' '.join(words)

join_lambda = lambda *words: ' '.join(words)

print(f"Regular function result: {join_words('Hello', 'world', '!')}")
print(f"Lambda function result: {join_lambda('Hello', 'world', '!')}")
