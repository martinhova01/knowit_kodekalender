import sys
sys.setrecursionlimit(10000)

digits = {
    "J": 10_000,
    "U": 5_000,
    "L": 1_000,
    "E": 500,
    "T": 100,
    "R": 50,
    "3": 10,
    "V": 5,
    "I": 1
}

def find_positive_nums(row: str, pos: list):
    s = 0
    for i in range(len(row) - 1):
        c = row[i]
        s += digits[c]
        if digits[c] >= digits[row[i + 1]]:
            continue
        
        elif digits[row[i + 1]] > s:
            avsluttende_siffer = row[i + 1]
            return find_positive_nums(row[i + 2:], pos + [avsluttende_siffer])
        
        else:
            avsluttende_siffer = row[0]
            return find_positive_nums(row[1:], pos + [avsluttende_siffer])
      
    return pos + list(row)

def calc(row: str):
    pos = find_positive_nums(row, [])
    values = list(map(lambda c : digits[c], pos))
    if sorted(values, reverse=True) != values:
        return -1
    
    s = 0
    for c in row:
        if c in pos:
            s += digits[c]
            pos.remove(c)
        else:
            s -= digits[c]
    return s
    
print(max(calc(line) for line in open("transaksjoner.txt").read().rstrip().split("\n")))






