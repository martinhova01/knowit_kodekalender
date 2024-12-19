from more_itertools import distinct_permutations

def thing(n, indexes):
    b = format(n, '016b')
    for idx in indexes:
        part = [b[:idx[0]], b[idx[0]: idx[1]], b[idx[1]: idx[2]], b[idx[2]: idx[3]]]
        part = sorted(part, key=lambda x: len(x))
        if (
            part[0] == part[1] and part[2] == part[3]
            or part[0] == part[2] and part[1] == part[3]
            or part[0] == part[3] and part[1] == part[2]
        ):
            return True
    return False
        
partitions = set()
for part in [(2, 2, 6, 6), (4, 4, 4, 4), (3, 3, 5, 5)]:
    for perm in distinct_permutations(part):
        partitions.add(perm)
    
indexes = []
for lenghts in partitions:
    idx = []
    s = 0
    for lenght in lenghts:
        s += lenght
        idx.append(s)
    indexes.append(idx)
        
    
s = 0
for i in range(65536):
    if thing(i, indexes):
        s += 1
print(s)