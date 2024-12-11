import matplotlib.pyplot as plt
from collections import deque
import networkx as nx
import itertools

import sys
sys.path.append("../..")
from utils import adjacent8

def find_reach():
    grid = open("reach.txt").read().rstrip().split("\n")[1:]
    start_positions = []
    for x, c in enumerate(grid[len(grid) - 1]):
        if c == "o":
            start_positions.append((x, len(grid) - 1))
            
    reaches = []
    for start_pos in start_positions:
        q = deque([start_pos])
        visited = set()
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            for _nx, ny in adjacent8(x, y):
                if ny < 0 or ny >= len(grid):
                    continue
                if _nx < 0 or _nx >= len(grid[ny]):
                    continue
                
                if grid[ny][_nx] == "x":
                    q.append((_nx, ny))
        reach = set()
        for x, y in visited:
            if (x, y) == start_pos:
                continue
            reach.add((x - start_pos[0], -y + start_pos[1]))
        reaches.append(reach)
    
    return reaches

def dist(x1, y1, x2, y2):
    return ((x1*10 - x2*10)**2 + (y1*10 - y2*10)**2) **0.5

def plot_grips(grips):
    X = [p[0] for p in grips]
    Y = [p[1] for p in grips]
    
    plt.scatter(X, Y, s=1)
    plt.show()
    
def print_reach(right, left):
    for r in (right, left):
        p = ""
        for y in range(10, 0, -1):
            for x in range(-10, 10):
                if (x, y) in r:
                    p += "x"
                else:
                    p += " "
            p += "\n"
        print(p)
    

def main():
    grips = set()
    lines = open("grep.txt").read().rstrip().split("\n")
    for line in lines:
        y, x = line.split(" ")
        grips.add((int(x), int(y)))
    left, right = find_reach()
    
    G = nx.DiGraph() # (x, y, right/left)
    for x, y in grips:
        
        # right
        for dx, dy in right:
            if (x + dx, y + dy) in grips:
                G.add_edge((x, y, "left"), (x + dx, y + dy, "right"), w=dist(x, y, x + dx, y + dy))
        
        # left
        for dx, dy in left:
            if (x + dx, y + dy) in grips:
                G.add_edge((x, y, "right"), (x + dx, y + dy, "left"), w=dist(x, y, x + dx, y + dy))
    
    best = float("inf")
    best_start = ""
    best_end = ""
    for start_hand, end_hand in itertools.product(("left", "right"), repeat=2):
        try:
            nx.shortest_path(G, (250, 0, start_hand), (749, 999, end_hand), weight="w")
            length = int(nx.shortest_path_length(G, (250, 0, start_hand), (749, 999, end_hand), weight="w"))
            if length < best:
                best = length
                best_start = start_hand
                best_end = end_hand
        except:
            # no path found for this hand-combination
            continue
            
    norsk = {"right": "høyre", "left": "venstre"}
    print(f"{best},{norsk[best_start]},{norsk[best_end]}")
    
    
if __name__ == "__main__":
    main()