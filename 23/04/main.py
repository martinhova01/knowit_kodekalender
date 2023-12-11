import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "reps.txt"
        self.data = eval(f"[{open(self.filename).read()}]")
        
    def solve(self):
        longest = 1
        c = 0
        bestSum = 0
        s = self.data[0]
        for i in range(1, len(self.data)):
            if self.data[i - 1] < self.data[i]:
                c += 1
                s += self.data[i]
            else:
                if c > longest:
                    bestSum = s
                    longest = c
                elif c == longest:
                    bestSum = max(bestSum, s)
                s = self.data[i]
                c = 0
                
        return bestSum
    
    
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