from collections import Counter
import time

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mapCharToIndex(c):
        return ord(c) - ord("a")
    
def mapIndexToChar(i):
    return chr(i + ord("a"))

class Solution():
    def __init__(self):
        self.filename = "input.txt"
        self.data = open(self.filename).read()
        
    def solve(self):
        res = ""
        for i in range(len(self.data)):
            c = self.data[i]
            if c == "." or c == " ":
                res += c
                continue
            res += self.decryptChar(c, i)
        return res
    
    def x(self):
        s = 0
        length = (6**6) + 666
        for i in range(3, length - 2, 2):
            if isPrime(i) and isPrime(i + 2):
                s += 1
        return s
    
    def y(self, i):
        r = []
        j = 0
        while len(r) <= i + 1 :
            b = bin(j)[2:]
            c = Counter(b)
            if c["1"] % 2 == 0:
                r.append(j)
            j += 1
        return r[i]
    
    def decryptChar(self, c, i):
        n = self.x() * self.y(i)
        index = mapCharToIndex(c)
        index = (index - n) % 26
        return mapIndexToChar(index)
        
        
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()