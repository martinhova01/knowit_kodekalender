grid = open("input.txt").read().rstrip().split("\n")

R = len(grid)
C = len(grid[0])

paths = [[0 for _ in range(C)] for _ in range(R)]
paths[0][0] = 1

DIRECTIONS = {(0, 1), (1, 0), (1, 1)}

for y in range(R):
    for x in range(C):
        if grid[y][x] == "x":
            continue
        curr = paths[y][x]
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= C or ny < 0 or ny >= R:
                continue

            if grid[ny][nx] == "x":
                continue

            paths[ny][nx] += curr

print(paths[R - 1][C - 1])
