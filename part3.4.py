import itertools

colors = ["red", "blue", "green"]
cycled_colors = itertools.cycle(colors)

for i in range(6):
    print(next(cycled_colors))
