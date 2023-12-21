import time

class Solution():
    def __init__(self):
        self.filename = "kredittkort.txt"
        self.data = [line for line in open(self.filename).read().rstrip().split("\n")]
        
    def solve(self):
        s = 0
        for card in self.data:
            if not self.isValid(card):
                s += 1
        return s
    
    def isValid(self, card):
        sliceCard = card[:-2]
        num = int(card[-2:])
        cardList = [int(x) for x in sliceCard]
        newList = []
        for i in range(len(cardList)):
            if i % 2 == 0:
                newList.append(cardList[i] * 2)
            else:
                newList.append(cardList[i])
        s = sum(newList)
        return (24 - (s % 24)) % 24 == num
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()