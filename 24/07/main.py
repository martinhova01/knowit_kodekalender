import math
import time
memo = {}

def lystig_juletall(n: str, prev: set):
    prev.add(n)
    if n in memo:
        for p in prev:
            memo[p] = memo[n]
        return memo[n]
    
    if n == "1" or n == "0":
        for p in prev:
            memo[p] = True
        return True
    
    s = str(sum(int(d)**2 for d in n))
    if s in prev:
        for p in prev:
            memo[p] = False
        return False
    
    return lystig_juletall(s, prev)

def jule_3_tall(n: str):
    if not lystig_juletall(n, set()):
        return False
    if len(n) == 1:
        return True
    
    first, last = n[:len(n) // 2], n[math.ceil(len(n) / 2):]
    if not (lystig_juletall(first, set()) and lystig_juletall(last, set())):
        return False
    
    if len(n) <= 3:
        return True
    
    for i in range(0, len(n) - 2):
        sl = n[i: i + 3]
        if not lystig_juletall(sl, set()):
            return False
    return True
    

def main():
    start = time.perf_counter()
    
    for n in range(9_999_999, 0, -1):
        if jule_3_tall(str(n)):
            print(n)
            break
        
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


if __name__ == "__main__":
    main()