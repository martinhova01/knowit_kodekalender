import time

class Solution():
    def __init__(self):
        self.goals = [int(x) for x in open("goals.txt").read().split(",")]
        self.bets = eval(f"[{open("bets.txt").read()}]")
        
    def solve(self):
        sticks = 50000
        for i in range(len(self.bets)):
            betSticks = round(0.175 * sticks)
            bet = self.bets[i][0]
            odds = self.bets[i][1]
            goals = self.goals[i]
            if goals >= bet:
                sticks += round(betSticks * odds)
            else:
                sticks -= betSticks
        
        return 50000 - round(sticks)
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()