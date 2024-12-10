import sys
sys.path.append("../..")
from utils import rot90

def rotate_blanket(blanket: dict):
    new_blanket = {}
    for (x, y), value in blanket.items():
        new_blanket[(rot90(x, y))] = value
    return new_blanket

def flip_blanket(blanket: dict, dim):
    new_blanket = {}
    if dim == 0:
        # flip along x-axis
        for (x, y), value in blanket.items():
            new_blanket[(x, -y)] = value
    else:
        # flip along y-axis
        for (x, y), value in blanket.items():
            new_blanket[(-x, y)] = value
    return new_blanket
            

def place_blanket(start_x, start_y, blanket: dict, joe: dict) -> int:
    best = 0
    for _ in range(4):
        # try 4 rotations
        for dim in range(2):
            # try to flip along both axis
            blanket = flip_blanket(blanket, dim)
            s = 0
            for (x, y), value in blanket.items():
                nx, ny = start_x + x, start_y + y
                if (nx, ny) not in joe.keys():
                    continue
                s += joe[(nx, ny)] * value
            best = max(best, s)
            blanket = flip_blanket(blanket, dim)
        blanket = rotate_blanket(blanket)
    return best
            

def main():
    blanket_input = open("teppe.txt").read().split("\n")
    blanket = {}
    for y in range(len(blanket_input)):
        for x in range(len(blanket_input[y])):
            if blanket_input[y][x] == " ":
                continue
            else:
                blanket[(x, y)] = int(blanket_input[y][x])
    
    joe = {}
    joe_input = open("joe.txt").read().rstrip().split("\n")
    for y in range(len(joe_input)):
        for x in range(len(joe_input[y])):
            c = joe_input[y][x]
            if c == " ":
                joe[(x, y)] = 0
            elif c == "x":
                joe[(x, y)] = -2
            else:
                joe[(x, y)] = int(c)
    
    res = 0
    for y in range(len(joe_input)):
        for x in range(len(joe_input[y])):
            res = max(res, place_blanket(x, y, blanket, joe))
    print(res)
    

if __name__ == "__main__":
    main()