import re
import pulp

data = open("input.txt", encoding="utf-8").read().rstrip()
parts = data.split("\n---\n")

lines = parts[0].split("\n")

T = list(map(int, re.findall(r"\d+", lines[0])))[0]

operations = []
for line in lines[1:]:
    operation, t = line.split(":")
    t = int(t)
    operations.append((operation, t))

lines = parts[1].split("\n")

cookies = []
for line in lines:
    words = line.split(" ")
    name = words[0]
    value = int(words[1])
    cookies.append((name, value, words[2:]))

model = pulp.LpProblem("Opt", pulp.LpMaximize)

# cookie variables
Y = [pulp.LpVariable(f"y_{name}", lowBound=0, cat="Binary") for name, _, _ in cookies]

# target function
model += pulp.lpSum(Y[i] * value for i, (_, value, _) in enumerate(cookies))

# operations variables
X = [pulp.LpVariable(f"x_{name}", lowBound=0, cat="Binary") for name, _ in operations]

# time constraint
model += pulp.lpSum(X[i] * t for i, (_, t) in enumerate(operations)) <= T

# finished recipe constraints
op_index = {name: i for i, (name, _) in enumerate(operations)}
for c_idx, (name, value, ops) in enumerate(cookies):

    # y <= x for all required operations
    for op in ops:
        model += Y[c_idx] <= X[op_index[op]]

    # y >= sum(x_ops) - (k - 1)
    model += Y[c_idx] >= pulp.lpSum(X[op_index[op]] for op in ops) - (len(ops) - 1)

model.solve()

# create result-string
opt_value = int(pulp.value(model.objective))
res_cookies = []
for y in Y:
    if pulp.value(y) == 1:
        res_cookies.append(y.name[2:])

print(str(opt_value) + "," + ",".join(sorted(res_cookies)))
