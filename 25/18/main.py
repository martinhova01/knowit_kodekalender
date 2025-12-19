import time


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = open(self.filename).read()

        self.R = 5 if self.test else 10
        self.C = 5 if self.test else 20
        self.gap = 5 if self.test else 3

    def solve(self):

        cards = []

        for i, row in enumerate(self.data.split("\n\n")):

            lines = row.split("\n")

            hole1 = set()
            hole2 = set()
            hole3 = set()

            for r in range(len(lines)):
                for c in range(self.C):
                    if lines[r][c] == "*":
                        hole1.add((c, r))

                for c in range(self.C + self.gap, (self.C * 2) + self.gap):
                    if lines[r][c] == "*":
                        hole2.add((c - (self.C + self.gap), r))

                for c in range(self.C * 2 + self.gap * 2, self.C * 3 + self.gap * 2):
                    if lines[r][c] == "*":
                        hole3.add((c - (self.C * 2 + self.gap * 2), r))

            cards.append(hole1)
            cards.append(hole2)
            cards.append(hole3)

        for i in range(len(cards)):

            target = cards[i]
            res = str(i + 1)

            for j in range(i + 1, len(cards)):
                if cards[j] == target:
                    res += str(j + 1)

            print(i)
            print("res:", res)

        return None


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
