import numpy as np
import time

size = 1_000_000

py_list = list(range(size))
numpy_array = np.arange(size)

start = time.time()
py_result = [x ** 2 for x in py_list]
end = time.time()
py_time = end - start

start = time.time()
numpy_result = numpy_array ** 2
end = time.time()
numpy_time = end - start

print(f"Python list time: {py_time:.6f} seconds")
print(f"NumPy array time: {numpy_time:.6f} seconds")

"NumPy is faster because it does math using super-fast C code instead of slower Python loops."