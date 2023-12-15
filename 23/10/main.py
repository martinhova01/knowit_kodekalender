import time
import networkx as nx
import sys

sys.path.append("../..")
from utils import directions4

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "sjokkis.txt"
        self.data = [x for x in open(self.filename).read().split("\n")]
        
    def solve(self):
        s = 0
        for line in self.data:
            if self.isValid(line):
                s += 1
        return s
    
    def printChoco(self, string):
        for i in range(8):
            print(string[8 * i : 8 * (i + 1)])
    
    def isValid(self, line):
        G = nx.Graph()
        choco = []
        for i in range(8):
            choco.append(line[8 * i : 8 * (i + 1)])
            
            #build graph
        for y in range(8):
            for x in range(8):
                if choco[y][x] == "0":
                    continue
                for (dx, dy) in directions4():
                    _x, _y = x + dx, y + dy
                    if _x < 0 or _x > 7 or _y < 0 or _y > 7:
                        continue
                    if choco[_y][_x] == "1":
                        G.add_edge((x, y), (_x, _y))
        
            #try cuts on rows
        for y in range(7):
            edgesToRemove = []
            for u, v in G.edges:
                if (u[1] == y and v[1] == y + 1) or (v[1] == y and u[1] == y + 1):
                    edgesToRemove.append((u, v))
                    
            edgesToRemove = sorted(edgesToRemove, key= lambda e : min(e[0][0], e[1][0]))
            if self.tryCut(edgesToRemove, G): return True
                
            #try cuts on cols
        for x in range(7):
            edgesToRemove = []
            for u, v in G.edges:
                if (u[0] == x and v[0] == x + 1) or (v[0] == x and u[0] == x + 1):
                    edgesToRemove.append((u, v))
                    
            edgesToRemove = sorted(edgesToRemove, key= lambda e : min(e[0][1], e[1][1]))       
            if self.tryCut(edgesToRemove, G): return True
                
        return False
    
    def tryCut(self, edgesToRemove, g):
        for start in range(len(edgesToRemove)):
            for stop in range(start + 1, len(edgesToRemove) + 1):
                    #remove
                for k in range(start, stop):
                    g.remove_edge(edgesToRemove[k][0], edgesToRemove[k][1])
                
                if nx.number_connected_components(g) == 2:
                    d1, d2 = nx.connected_components(g)
                    if len(d1) == len(d2):
                        return True
                    #add back
                for k in range(start, stop):
                    g.add_edge(edgesToRemove[k][0], edgesToRemove[k][1])
        return False
    
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