data = [line for line in open("input.txt").read().rstrip().split("\n")]

bamse = "01001010"
tog = "01000010"

s = 0
for i, num in enumerate(data):
    if num == bamse and data[i - 1] == tog:
        s += 1

print(s)
