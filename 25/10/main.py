import time
import re
from collections import defaultdict


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = [
            self.parse_line(line)
            for line in open(self.filename).read().rstrip().split("\n")
        ]

    def parse_line(self, line: str):
        nums = list(map(int, re.findall(r"\d+", line)))
        name = line.split(",")[0][7:]

        return name, nums

    def calculate(self, temp, water, kull):
        if temp < 95 or temp > 105:
            return 0

        if water < 400 or water > 1500:
            return 0

        if kull < 300 or kull > 500:
            return 0

        produce = (water - 100) + kull // 10

        if temp >= 100:
            produce = produce - produce // 40

        return int(produce)

    def solve(self):
        res = defaultdict(int)
        for name, (temp, water, kull) in self.data:
            res[name] += self.calculate(temp, water, kull)

        best = sorted(res.items(), key=lambda x: x[1], reverse=True)[0][0]
        return f"{sum(res.values())} {best}"


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
