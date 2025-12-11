import pulp

lines = open("input.txt").read().rstrip().split("\n")
C = int(lines[0])
W = []
JOY = []
for line in lines[1:]:
    _, w, joy = line.split(",")
    W.append(int(w))
    JOY.append(int(joy))

model = pulp.LpProblem("Knapsack", pulp.LpMaximize)
X = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Binary") for i in range(len(W))]
model += pulp.lpSum(JOY[i] * X[i] for i in range(len(W)))
model += pulp.lpSum(W[i] * X[i] for i in range(len(W))) <= C
model.solve()

print(f"{int(pulp.value(model.objective))},{int(sum(x.value() for x in X))}")
