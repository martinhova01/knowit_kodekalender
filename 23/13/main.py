import time


    #Copied from https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def SieveOfEratosthenes(num):
    # boolean array
    prime = [True for _ in range(num+1)]
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    result = []
    for p in range(2, num+1):
        if prime[p]:
            result.append(p)
            
    return result

class Solution():
    def __init__(self):
        self.elvesAtWork = [int(x) for x in open("alver_på_jobb.txt").read().split("\n")]
        self.elvesNotAtWork = [int(x) for x in open("alver_ikke_på_jobb.txt").read().split("\n")]
        self.grichen = [int(x) for x in open("grinchen.txt").read().split("\n")]
        self.numberOfWindows = 400_009
        self.windows = [False for _ in range(self.numberOfWindows)]
        
            #uncoment line below to read primes from file
        # self.primes = [int(x) for x in open("primes.txt").read().split("\n")]
        
        self.primes = SieveOfEratosthenes(198491317)
        self.writePrimes()
        
    def solve(self):
            #elves go to work
        for elf in self.elvesAtWork:
            w1 = (elf * 2) % self.numberOfWindows
            w2 = (elf + self.primes[elf]) % self.numberOfWindows
            self.windows[w1] = True
            self.windows[w2] = True
            
            #find the lucky elves
        luckyElves = []
        for elf in self.elvesNotAtWork:
            w1 = (elf * 2) % self.numberOfWindows
            w2 = (elf + self.primes[elf]) % self.numberOfWindows
            if self.windows[w1] and self.windows[w2]:
                luckyElves.append(elf)
                
            #grinch blows out candles
        for w in self.grichen:
            self.windows[w] = False
            
            #count unlucky elves
        s = 0
        for elf in luckyElves:
            w1 = (elf * 2) % self.numberOfWindows
            w2 = (elf + self.primes[elf]) % self.numberOfWindows
            if self.windows[w1] and self.windows[w2]:
                continue
            s += 1
        return s
    
    def getLargestId(self):
        return max(max((x for x in self.elvesAtWork)), max((x for x in self.elvesNotAtWork)))
    
    def writePrimes(self):
        with open("primes.txt", "w") as f:
            for prime in self.primes:
                f.write(str(prime) + "\n")
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()