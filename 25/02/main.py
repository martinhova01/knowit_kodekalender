import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = open(self.filename, encoding="utf-8").read().rstrip().split("\n")
        
    def solve(self):
        alph = "abcdefghijklmnopqrstuvwxyzæøå"
        offset = 0
        res = ""
        for line in self.data:
            offset -= 1
            for c in line:
                
                j = alph.index(c.lower()) + offset
                if c.isupper():
                    
                    res += alph[j % len(alph)].upper()
                else:
                    res += alph[j % len(alph)]
        
        return res
            
    
    
    
def main():
    start = time.perf_counter()
    
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()