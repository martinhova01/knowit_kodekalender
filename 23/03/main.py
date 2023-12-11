import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.startValue = 1000 if test else 200000
        self.data = [eval(f"[{line}]") for line in open(self.filename).readlines()]
        
        
    def solve(self):
        money = self.startValue
        for day in self.data:
            money = self.solveDay(day, money)
        return money
            
    def solveDay(self, day, money):
        m = 0
        for i in range(len(day) - 1):
            buyPrice = day[i]
            numberOfStocks = money // buyPrice
            moneyLeft = money - (numberOfStocks * buyPrice)
            sellPrice = max(day[i+1:])
            m = max(m, sellPrice * numberOfStocks + moneyLeft)
        return m
        
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("TEST")
    print(f"Result: {s.solve()}")
    
    s = Solution()
    print("MAIN")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()