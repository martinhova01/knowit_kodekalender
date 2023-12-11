import time

class Solution():
    def __init__(self):
        self.data = None
        
    def solve(self):
        return None
    
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()