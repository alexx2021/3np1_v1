  # import numba as nb
import numpy as np
import matplotlib.pyplot as plt
import time
from variables import getSize

size = getSize()

# @nb.njit()
def find_3np1_chain_length(n):
    iterations = 1
    while n > 1:
        is_even = n % 2 == 0
        if is_even:
            n = n / 2
        if not is_even:  #odd number
            n = 3 * n + 1
        iterations += 1
    return iterations


"""find_largest_chain_under_n"""
# @nb.njit()#parallel = True)
def find_biggest_chain_under(n):
    max_chain_length = 1
    n_at_max_chain = 1
    for current_n in range(1, n):  #nb.prange(1,n):
        new_chain_length = find_3np1_chain_length(current_n)
        if new_chain_length > max_chain_length:
            max_chain = new_chain_length
            n_at_max_chain = current_n
    return max_chain, n_at_max_chain


start = time.time()
print(f'Largest chain length {find_biggest_chain_under(size)[0]} at number {find_biggest_chain_under(size)[1]}')
print(f'Time elapsed: {round(time.time() - start, 4)}')


"""showarray stuff:"""
arr = np.arange(1, size + 1)
result_arr = np.zeros(size)

for i in range(len(arr)):
    result_arr[i] = find_3np1_chain_length(arr[i])

plt.scatter(arr, result_arr, np.ones(size))
plt.xlabel('Number')
plt.ylabel('Chain length')
plt.show()
