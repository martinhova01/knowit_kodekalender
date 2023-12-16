import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "rekke.txt"
        self.data = eval(open(self.filename).read().rstrip())
        
    def solve(self):
        coins = [1] * len(self.data)
        changed = True
        while changed:
            changed = False
            for i in range(len(coins)):
                if not self.isValid(coins, i):
                    coins[i] += 1
                    changed = True
        return sum(coins)
            
    def isValid(self, coins, i):
        for j in range(-2, 3):
            if i + j < 0 or i + j >= len(coins) or j == 0:
                continue
            index = i + j
            if self.data[index] < self.data[i] and coins[index] >= coins[i]:
                return False
            elif self.data[index] == self.data[i] and coins[index] > coins[i]:
                return False
        return True
    
    
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