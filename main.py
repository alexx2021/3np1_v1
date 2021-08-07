# import numba as nb
import numpy as np
import matplotlib.pyplot as plt
import time

# there is a chat window xdddddddddddddddddddddddddd

# @nb.njit()
def find_3np1_chain_length(n):
    iterations = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        iterations += 1
    return iterations

size = 10000

# for under 1m : highest reaches peak at   159424614880
# for under 100m : highest reaches peak at 966616035460

"""find_largest_n"""
# @nb.njit()#parallel = True)
def find_biggest_chain_under(n):
    max_chain = 1
    n_at_max_chain = 1
    for i in range(1,n): #nb.prange(1,n):
        new_chain = find_3np1_chain_length(i)
        if new_chain > max_chain:
            max_chain = new_chain
            n_at_max_chain = i
    return max_chain, n_at_max_chain

start = time.time()
print(find_biggest_chain_under(size))
print(time.time() - start)

"""showarray stuff:"""
arr = np.arange(1,size+1)
result_arr = np.zeros(size)

for i in range(len(arr)):
    result_arr[i] = find_3np1_chain_length(arr[i])

plt.scatter(arr, np.exp(result_arr))
plt.show()
