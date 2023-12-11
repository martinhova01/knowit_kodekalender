from tqdm import tqdm

def main():
    target = 100_000_001
    print(sum(isSpecialPrime(i) for i in tqdm(range(1, target))))
    
def isSpecialPrime(n):
    
    s = sum(int(c) for c in str(n))
    m = n / s
    if int(m) == m:
        return isPrime(int(m))
    return False

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
main()