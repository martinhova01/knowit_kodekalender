import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "rekke.txt"
        self.data = eval(open(self.filename).read().rstrip())
        
    def solve(self):
        firstVal = 1
        while True:
            coins = [firstVal]
            for i in range(1, len(self.data)):
                nextVal = self.findNextVal(self, i, coins)
                if nextVal == -1:
                    firstVal += 1
                    continue
                coins.append(nextVal)
            break
        
        return sum(coins)
    
    def findNextVal(self, i, coins):
        pass
    
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("--TEST--")
    print(f"Result: {s.solve()}")
    
    # s = Solution()
    # print("--MAIN--")
    # print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()