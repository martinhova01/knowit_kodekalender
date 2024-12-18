import time
from more_itertools import set_partitions, distinct_permutations



def all_splits(string):
    for comb in ["".join(p) for p in distinct_permutations(string)]:
        for part_length in range(2, len(comb)):
            for part in set_partitions(comb, part_length):
                yield ["".join(p) for p in part]
    

def valid(n):
    st = str(n)
    for split in all_splits(st):
        p = 1
        for s in split:
            p *= int(s)
        if p == n:
            return True
    
    return False

start = time.perf_counter()
nums = list(map(int, open("tall.txt").read().rstrip().split("\n")))
s = 0
for n in nums:
    if valid(n):
        s += n
print(s)
print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")