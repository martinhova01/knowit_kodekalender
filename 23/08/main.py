import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.poem = open("cypher.txt", encoding="utf-8").read()
        self.keys = [eval(line) for line in open("input.txt").readlines()]
        
    def solve(self):
        key = 0
        res = ""
        for i in range(len(self.poem)):
            c = self.poem[i]
            if c == "\n":
                res += "\n"
                continue
            if c == " ":
                key += 1
                res += " "
                continue
            res += self.decryptChar(c, self.keys[key])
            
        word = ""
        for line in res.split("\n"):
            if len(line) > 0:
                word += line[0]
        return word
                
    def decryptChar(self, c, key):
            if c == ",":
                return ","
            
            index = key.index(self.mapCharToIndex(c))
            decipherC = self.mapIndexToChar(index)
            return decipherC
            
        
    def mapCharToIndex(self, c):
        if c == "æ":
            return 26
        elif c == "ø":
            return 27
        elif c == "å":
            return 28
        return ord(c) - ord("a")
    
    def mapIndexToChar(self, i):
        if i == 26:
            return "æ"
        elif i == 27:
            return "ø"
        elif i == 28:
            return "å"
        return chr(i + ord("a"))
        
    
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()