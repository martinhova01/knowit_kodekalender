import math
import time

class Solution():
    def __init__(self):
        self.data = [eval(line) for line in open("rute.txt").readlines()]
        print(len(self.data))
        
    def solve(self):
        dist = 0
        for i in range(1, len(self.data)):
            x1 = self.data[i - 1][0]
            y1 = self.data[i - 1][1]
            x2 = self.data[i][0]
            y2 = self.data[i][1]
            dist += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            
        return math.ceil((dist / 1000) * 9)
    
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()