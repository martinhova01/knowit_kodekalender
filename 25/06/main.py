import time
from collections import deque


def directions4() -> list:
    return [(0, 1), (1, 0), (0, -1), (-1, 0)]


def adjacent4(x: int, y: int) -> list:
    return [(x + dx, y + dy) for dx, dy in directions4()]


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = open(self.filename).read()

    def bfs(self, grid, start, goal):
        R = len(grid)
        C = len(grid[0])
        visited = set()
        q = deque([(start[0], start[1], 0)])
        while q:
            x, y, step = q.popleft()

            if (x, y) in visited:
                continue

            if (x, y) == goal:
                return step
            visited.add((x, y))

            for nx, ny in adjacent4(x, y):
                if nx < 0 or nx >= C or ny < 0 or ny >= R:
                    continue

                if grid[ny][nx] == "#":
                    continue
                q.append((nx, ny, step + 1))

        return 0

    def solve(self):
        tot = 0
        for sone in self.data.split("\n;\n"):
            grid = sone.split("\n")
            R = len(grid)
            C = len(grid[0])
            start = None
            goal = None
            for y in range(R):
                for x in range(C):
                    c = grid[y][x]
                    if c == "S":
                        start = (x, y)
                        continue
                    if c == "*":
                        goal = (x, y)
                        continue
            if not start or not goal:
                continue

            tot += self.bfs(grid, start, goal)

        return tot


def main():
    start = time.perf_counter()

    s = Solution(test=True)
    print("--TEST--")
    print(f"Result: {s.solve()}")

    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
