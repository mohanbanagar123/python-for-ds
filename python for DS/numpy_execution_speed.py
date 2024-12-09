import numpy as np
import time

size=10**6

list1=list(range(size))
list2=list(range(size))

array1=np.arange(size)
array2=np.arange(size)

start_time=time.time()
list_result = [x * y for x, y in zip(list1, list2)]
list_time = time.time() - start_time


start_time=time.time()
array_result=array1+array2
array_time=time.time()-start_time

print(f"Time taken using python lists: {list_time:.5f}seconds")
print(f"Time taken using numpy arrays: {array_time:.5f}seconds")
print(f"Numpy is approximately {list_time / array_time:.5f}time faster")
