import time

class Solution():
    def __init__(self, test=False):
        self.filename = "push.txt" if not test else "testinput.txt"
        self.data = eval(f"[{open(self.filename).read()}]")
        
    def solve(self):
        longest = 0
        longestSeq = []
        for i in range(len(self.data) - 1):
            seq = self.getSequence(i)
            if len(seq) > longest:
                longest = len(seq)
                longestSeq = seq
        return sum(longestSeq)
            
    def getSequence(self, start):
        i = start + 1
        seq = [self.data[start]]
        while self.data[i] > self.data[i - 1]:
            seq.append(self.data[i])
            i += 1
            if i >= len(self.data) - 1:
                return seq
    
        while self.data[i] < self.data[i - 1]:
            seq.append(self.data[i])
            i += 1
            if i >= len(self.data) - 1:
                return seq
            
        return seq
            
    
    
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