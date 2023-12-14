from collections import deque
import time
import networkx as nx

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "kart.txt"
        self.data = [list(x) for x in open(self.filename).read().split("\n")]
        self.visited = set()
        
    def solve(self):
        s = 0
        for y in range(len(self.data)):
           for x in range(len(self.data[y])):
                if (x, y) in self.visited or self.data[y][x] == ".":
                   continue
                self.traverse((x, y))
                s += 1
        return s
    
    def traverse(self, source: (int, int)):
        x, y = source
        dirs = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        q = deque()
        q.append(source)
        self.visited.add(source)
        while q:
            x, y = q.popleft()
            for (dx, dy) in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= len(self.data[y]) or ny < 0 or ny >= len(self.data):
                    continue
                if self.data[ny][nx] == "X" and (nx, ny) not in self.visited:
                    q.append((nx, ny))
                    self.visited.add((nx, ny))
                    
    def altSolve(self):
        g = nx.Graph()
        for y in range(len(self.data)):
           for x in range(len(self.data[y])):
                if self.data[y][x] != "X":
                    continue
                g.add_node((x, y))
                for (dx, dy) in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                    if (x + dx, y + dy) in g:
                        g.add_edge((x, y), (x + dx, y + dy))
                        
                    
                    
                    
        return nx.algorithms.number_connected_components(g)
               
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("--TEST--")
    # print(f"Result: {s.solve()}")
    print(f"Result: {s.altSolve()}")
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    print(f"Result: {s.altSolve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()