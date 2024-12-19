import time
from functools import cache
from tqdm import tqdm

import sys
sys.set_int_max_str_digits(100_000)

sequences = [-1 for _ in range(9)]

@cache
def alvonacci(n):
    if n == 0 or n == 1:
        return n
    
    if n % 5 == 0:
        i = 0
        while True:
            i += 1
            if n % (5**i) != 0:
                break
        sequences[i] += 1
        return alvonacci(sequences[i])
            
    elif n % 5 == 1:
        return alvonacci(n - 3) + alvonacci(n - 2) + alvonacci(n - 1)
    else:
        return alvonacci(n - 2) + alvonacci(n - 1)

start = time.perf_counter()

for i in range(0, 5**8):
    alvonacci(i)
print(str(alvonacci(5**8 - 1))[-20:])
    
print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
