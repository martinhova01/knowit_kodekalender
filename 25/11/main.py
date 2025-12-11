import time
import pulp

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = [self.parse_line(line) for line in open(self.filename).read().split("\n")[1:]]
        self.C = int(open(self.filename).read().split("\n")[0])
        
    def parse_line(self, line):
        _, w, joy = line.split(",")
        w = int(w)
        joy = int(joy)
        return w, joy
        
    def solve(self):
        W = []
        joys = []
        for w, joy in self.data:
            W.append(w)
            joys.append(joy)
        
        model = pulp.LpProblem("Knapsack", pulp.LpMaximize)
        X = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Binary") for i in range(len(W))]
        
        model += pulp.lpSum(joys[i] * X[i] for i in range(len(W)))
        
        model += pulp.lpSum(W[i] * X[i] for i in range(len(W))) <= self.C
        
        model.solve()
        
        return f"{int(pulp.value(model.objective))},{int(sum(x.value() for x in X))}"
        
    
    
    
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