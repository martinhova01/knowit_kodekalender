from tqdm import tqdm

def main():
    seq = ""
    s = 0
    for i in tqdm(range(100_000)):
        c = str(i)
        if c in seq:
            continue
        s += 1
        seq += c      
    print(s)

main()