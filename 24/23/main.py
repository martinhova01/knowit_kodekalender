import matplotlib.pyplot as plt

data = open("lekescan.txt").read().rstrip().split("\n")

x, y, z = [], [], []

for line in data:
    s = line.split(" ")
    x.append(float(s[0]))
    y.append(float(s[1]))
    z.append(float(s[2]))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
scatter = ax.scatter(x, y, z, s=0.2)
plt.show()
