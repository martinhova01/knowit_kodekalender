import networkx as nx
import re

data = open("input.txt").read().rstrip()

G = nx.DiGraph()
for line in data.split("\n"):
    nums = list(map(int, re.findall(r"\d+", line)))
    G.add_edge(nums[0], nums[1], w=nums[2])


cycles = nx.simple_cycles(G)
best = float("inf")
best_cycle = None
for c in cycles:
    cycle = list(c)
    cycle.append(c[0])
    w = nx.path_weight(G, cycle, weight="w")
    if w < best:
        best = w
        best_cycle = cycle

print(best_cycle, best)
