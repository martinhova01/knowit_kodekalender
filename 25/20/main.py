import pandas as pd
import pulp

df = pd.read_csv(
    "input.csv",
    header=None,
    names=[
        "name",
        "price",
        "weight",
        "sugar_percent",
        "max_weight",
        "min_boxes",
    ],
)
N = len(df)

model = pulp.LpProblem("candy", pulp.LpMaximize)

X = [
    pulp.LpVariable(f"x_{i}", lowBound=df["min_boxes"][i], cat="Integer")
    for i in range(N)
]

# target-function
model += pulp.lpSum(X[i] * df["sugar_percent"][i] * df["weight"][i] for i in range(N))

# budsjett
model += pulp.lpSum(X[i] * df["price"][i] for i in range(N)) <= 50_000

# vekt
for i in range(N):
    model += X[i] * df["weight"][i] <= df["max_weight"][i]

model.solve()

res = ""
res += str(int(sum(pulp.value(X[i]) * df["price"][i] for i in range(N)))) + ","
for i in range(N):
    res += df["name"][i] + ":" + str(int(pulp.value(X[i]))) + ","

print(res)
