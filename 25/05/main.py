import time
from morse3 import Morse


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = open(self.filename).read().rstrip()

    def solve(self):
        print(
            Morse(
                open("input.txt")
                .read()
                .rstrip()
                .replace("-", "")
                .replace("Hooo", "-")
                .replace("Ho", ".")
            ).morseToString()
        )


def main():
    start = time.perf_counter()

    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()


print(
    Morse(
        open("input.txt")
        .read()
        .rstrip()
        .replace("-", "")
        .replace("Hooo", "-")
        .replace("Ho", ".")
    ).morseToString()
)
