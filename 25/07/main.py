import time


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "input.txt"
        self.data = None

    def find_nisse_in_word(self, nisse, word, chars_since_last):
        if not nisse:
            return True

        if chars_since_last > 2:
            return False

        if not word:
            return False

        use = False
        if nisse[0] == word[0]:
            use = self.find_nisse_in_word(nisse[1:], word[1:], 0)

        not_use = False
        if chars_since_last == -1:
            not_use = self.find_nisse_in_word(nisse, word[1:], -1)
        else:
            not_use = self.find_nisse_in_word(nisse, word[1:], chars_since_last + 1)

        return use or not_use

    def find_troll_in_word(self, troll, word, chars_since_last):
        if not troll:
            return True

        if chars_since_last > 5:
            return False

        if not word:
            return False

        use = False
        if troll[0] == word[0]:
            use = self.find_troll_in_word(troll[1:], word[2:], 1)

        not_use = False
        if chars_since_last == -1:
            not_use = self.find_troll_in_word(troll, word[1:], -1)
        else:
            not_use = self.find_troll_in_word(troll, word[1:], chars_since_last + 1)

        return use or not_use

    def is_nisse(self, word: str):
        if word[0] == "n" or word[-1] == "e":
            return False

        return self.find_nisse_in_word("nisse", word, -1)

    def is_troll(self, word: str):
        return self.find_troll_in_word("troll", word, -1)

    def is_valid(self, word: str):
        return self.is_nisse(word) or self.is_troll(word)

    def solve(self):
        data = open("ordliste.txt", encoding="utf-8").read().rstrip().split("\n")
        s = 0
        for word in data:
            if self.is_valid(word.lower()):
                s += 1
        return s


def main():
    start = time.perf_counter()

    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")  # 908

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
