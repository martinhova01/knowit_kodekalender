import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "track.txt"
        self.data = open(self.filename).read().rstrip()
        
    def solve(self):
        energy = 3000
        used = []
        cost = {"S": 5, "B": 10, "D": 15, "I": 0, "P": 0}
        for i, c in enumerate(self.data):
            
            energy -= cost[c]
                
            if c == "P":
                energy += used[-1]
                energy += used[-2]
                
            used.append(cost[c])
                
            if energy == 0:
                return (i + 1) * 10
            elif energy < 0:
                return i * 10
            
                
            
    
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()