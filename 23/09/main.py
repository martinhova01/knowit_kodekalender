from collections import defaultdict
import time


class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = eval(open(self.filename).read())
        
    def solve(self):
        m = defaultdict(int)
        
        for i in range(len(self.data)):
            u, v = self.data[i]
            if u not in m:
                m[u] = set()
            m[u].add(v)
            if v not in m:
                m[v] = set()
            m[v].add(u)
            
        s = 0
        for node, neighbors in m.items():
            if len(neighbors) == 1:
                s = node
                
        visited = [s]
        currentNode = s
        while True:
            if len(m[currentNode]) == 1 and currentNode != s:
                break
            for node in m[currentNode]:
                if node in visited:
                    continue
                currentNode = node
                visited.append(currentNode)
        
        mid = len(visited ) // 2
        
        return visited[mid] + visited[mid - 1]
                
    
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