data = open("commands.txt").read().rstrip()

"""
0: None
1: Large snowball
2: Lagre and medium snowball
3: large, medium and small snowball
4: hat, not carrot
5: carrot, not hat
6: done
"""
snowmen = []

balls = []  # 1: Large, 2: medium, 3: small

res = 0


for line in data.split("\n"):
    print(line, snowmen, balls)
    if line == "ROLL":
        balls.append(3)

    elif line == "ROLL ROLL":
        balls.append(2)

    elif line == "ROLL ROLL ROLL":
        snowmen.append(1)

    elif line == "STACK":
        if not balls:
            continue

        for i, snowman in enumerate(snowmen):
            if snowman == balls[-1] - 1:
                balls.pop()
                snowmen[i] += 1
                break

    elif line == "HAT":
        for i, snowman in enumerate(snowmen):
            if snowman == 5:
                snowmen.pop(i)
                res += 1
                break

            if snowman == 3:
                snowmen[i] = 4
                break

    elif line == "CARROT":
        for i, snowman in enumerate(snowmen):
            if snowman == 4:
                snowmen.pop(i)
                res += 1
                break

            if snowman == 3:
                snowmen[i] = 5
                break

    snowmen = sorted(snowmen, reverse=True)

print(res)
