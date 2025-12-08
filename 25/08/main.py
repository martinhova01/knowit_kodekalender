import time
from sympy import isprime


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = list(
            map(int, open(self.filename).read().rstrip().replace("\n", " ").split(" "))
        )

    def is_special(self, num):
        num_string = str(num)
        s = sum(int(c) for c in num_string)
        if num % s == 0:
            return isprime(num // s)

    def solve(self):
        s = 0
        for num in self.data:
            if self.is_special(num):
                s += 1

        return s


def main():
    start = time.perf_counter()

    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
