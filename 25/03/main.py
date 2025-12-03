import time
import pandas as pd


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.csv" if test else "input.csv"

    def solve(self):
        df = pd.read_csv(self.filename)
        df["score"] = (2 * df["snill"] - df["slem"]) * 25 + df["pepperkaker"] * 15
        df = df.sort_values(by="score", ascending=False)

        combined = pd.concat([df.head(3), df.tail(3)])

        return ",".join(
            f"{row["navn"]} {row["score"]}" for _, row in combined.iterrows()
        )


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
