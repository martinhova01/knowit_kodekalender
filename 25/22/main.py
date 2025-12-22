data = open("input.txt").read().rstrip()

magic_sum = 0
krampus_sum = 0
for i, line in enumerate(data.split("\n")):
    line_score = 0
    for c in line:
        if c in {"M", "d", "+"}:
            line_score += 1

        else:
            krampus_sum += ord(c)

    line_score *= i + 1
    magic_sum += line_score


print(magic_sum - krampus_sum)
