import time


class Solution():
    def __init__(self):
        self.filename = "transaksjoner.txt"
        self.data = [(line.split(";")[0], int(line.split(";")[1]), int(line.split(";")[2])) for line in open(self.filename, encoding="UTF-8").read().rstrip().split("\n")]
        print(self.data)
        
    def solve(self):
        word = ""
        for line in self.data:
            if not self.isValid(line):
                word += line[0][0]
        return word
            
                
    def mapCharToIndex(self, c):
            if c == "æ":
                return 27
            elif c == "ø":
                return 28
            elif c == "å":
                return 29
            return ord(c) - ord("a") + 1
        
    def isValid(self, line):
        s = 0
        for c in line[0]:
            c = c.lower()
            if not c.isalpha():
                continue
            s += self.mapCharToIndex(c)
        
        res = s * line[1]
        mod = int("beef", 16)
        res = res % mod
        return res == line[2]
        
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()