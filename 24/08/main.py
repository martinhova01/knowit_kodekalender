import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_gen():
    n = 0
    while True:
        n += 1
        if is_prime(n):
            yield n
            
def primtalv_gen():
    s = 0
    for prime in primes_gen():
        st = str(prime)
        for i in range(len(st)):
            s += (10**i) * int(st[i])
        yield s


def main():
    start = time.perf_counter()
    primtalv_generator = primtalv_gen()
    s = 0
    primtalv = 0
    while primtalv < 10_000_000:
        primtalv = next(primtalv_generator)
        if is_prime(primtalv):
            s += 1
    print(s)
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


if __name__ == "__main__":
    main()