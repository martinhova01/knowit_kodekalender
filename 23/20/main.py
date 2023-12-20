import time

class Solution():
    def __init__(self):
        self.diceRolls = self.getDiceRolls()
        self.diceRollCounter = {4: 0, 6: 0, 8: 0, 10: 0, 20: 0}
        
    def getDiceRolls(self):
        diceRolls = {}
        for i in [4, 6, 8, 10, 20]:
            rolls = [int(x) for x in open("dice/d" + str(i) + ".txt").read().rstrip().split("\n")]
            diceRolls[i] = rolls
        return diceRolls
        
    def solve(self):
        health = 10_000_000
        damage = 0
        attackCounter = 0
        
        while damage < health:
            for i in range(3):
                attackCounter += 1
                    # damage = 2d6K1 + 2 + 1d4
                    # acc = 1d20 + 8
                if i == 0:
                    if self.rollDice(20, 1, True) + 8 >= 18:
                        damage += (self.rollDice(6, 2, True) + 2 + self.rollDice(4, 1, True))
                    # damage = 1d8 + 5
                    # acc = 1d20 + 6
                if i == 1:
                    if self.rollDice(20, 1, True) + 6 >= 18:
                        damage += (self.rollDice(8, 1, True) + 5)
                    # damage = 2d10KL1 + 6
                    # acc = 1d20 + 3
                if i == 2:
                    if self.rollDice(20, 1, True) + 3 >= 18:
                        damage += (self.rollDice(10, 2, False) + 6)
                if damage >= health:
                    break   
        return attackCounter
                       
    def rollDice(self, sides, times, keepHigh):
        eyes = 0 if keepHigh else 100
        for _ in range(times):
            nextEyes = self.diceRolls[sides][self.diceRollCounter[sides]]
            eyes = max(eyes, nextEyes) if keepHigh else min(eyes, nextEyes)
            self.diceRollCounter[sides] = (self.diceRollCounter[sides] + 1) % len(self.diceRolls[sides])
        return eyes
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()