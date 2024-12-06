import itertools
from tqdm import tqdm

segments = {
        0: {"A", "B", "C", "D", "E", "F"},
        2: {"A", "B", "D", "E", "G"},
        3: {"A", "B", "C", "D", "G"},
        5: {"A", "C", "D", "F", "G"},
        6: {"A", "C", "D", "E", "F", "G"},
        7: {"A", "B", "C"},
        8: {"A", "B", "C", "D", "E", "F", "G"},
        9: {"A", "B", "C", "D", "F", "G"},
        1: {"B", "C"},
        4: {"B", "C", "F", "G"}
    }
indexes = {c: i for i, c in enumerate("ABCDEFGHI")}
swaps = []


def main():
    
    for line in open("input.txt").read().split("\n"):
        s1, s2 = line.split(" <-> ")
        swaps.append((s1, s2))
    
    
    s = 0
    for num in tqdm(itertools.product([x for x in range(10)], repeat=9)):
        if test_swap(num):
            s += 1
    print(s)
            
    
def test_swap(num):
    for s1, s2 in swaps:
        index1 = indexes[s1[0]]
        index2 = indexes[s2[0]]
        seg1 = s1[1]
        seg2 = s2[1]
        
        if seg1 in segments[num[index1]] and seg2 not in segments[num[index2]]:
            return False
        if seg1 not in segments[num[index1]] and seg2 in segments[num[index2]]:
            return False
    
    return True
        

if __name__ == "__main__":
    main()