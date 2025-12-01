import time
from collections import deque


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n")

    def solve(self):
        q = deque()
        res = ""

        for line in self.data:
            if line.startswith("ADD"):
                q.append(line.split(" ")[1])
            elif line.startswith("PROCESS"):
                try:
                    item = q.popleft()
                    res += item[0]
                except:
                    res += "X"
            else:
                n = len(q)
                res += str(n)[-1]

        return res


def main():
    start = time.perf_counter()

    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
