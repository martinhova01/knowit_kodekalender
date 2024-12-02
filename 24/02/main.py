def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_special_prime(n, index):
    index = str(index)
    n = str(n)
    s_index = sum(int(c) for c in index)
    s_n = sum(int(c) for c in n)
    return s_n == s_index

def main():
    primes = []
    res = []
    i = 1
    while len(res) < 10000:
        i += 1
        if not is_prime(i):
            continue
        primes.append(i)
        if is_special_prime(i, len(primes)):
            res.append(i)
    print(sum(res))
    
if __name__ == "__main__":
    main()