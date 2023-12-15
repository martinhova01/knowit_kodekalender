import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "sjokkis.txt"
        self.data = [x for x in open(self.filename).read().split("\n")]
        
    def solve(self):
        return None
    
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("--TEST--")
    print(f"Result: {s.solve()}")
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()