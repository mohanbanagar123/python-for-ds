import numpy as np
import time

size = 10**6

python_list = list(range(size))
numpy_array = np.arange(size)

start_time = time.time()
python_list_result = [x + 1 for x in python_list]
end_time = time.time()
python_list_time = end_time - start_time

start_time = time.time()
numpy_array_result = numpy_array + 1
end_time = time.time()
numpy_array_time = end_time - start_time

print(f"Time taken using Python list: {python_list_time:.6f} seconds")
print(f"Time taken using NumPy array: {numpy_array_time:.6f} seconds")
print(f"NumPy is approximately {python_list_time / numpy_array_time:.2f} times faster for this operation.")
