data = open("input.txt").read().rstrip()

vocals = "aeiouyæøå"
consonants = "bcdfghjklmnpqrstvwxz"
beans = ""
for i, c in enumerate(data):
    if c.isnumeric():
        continue

    if c in consonants and not (data[i - 2].isnumeric() and data[i + 2].isnumeric()):
        continue

    beans += c

print(beans)
