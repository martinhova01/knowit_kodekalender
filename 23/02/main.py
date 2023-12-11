import time

class Solution():
    def __init__(self):
        self.data = [x for x in open("log.txt").read().split(", ")]
        self.clicks = [s[:5] == "klikk" for s in self.data]
        self.nums = [int(s[len(s)-1:]) for s in self.data]
        
    def solve(self):
        pins = [False for _ in range(7)]
        s = 0
        for i in range(len(self.clicks)):
            if self.clicks[i]:
                pins[self.nums[i] - 1] = True
            else:
                pins[self.nums[i] - 1] = False
            if all(x for x in pins):
                s += 1
                pins = [False for _ in range(7)]
                
        return s
    
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()