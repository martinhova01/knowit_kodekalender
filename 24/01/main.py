
def place_blanket(start_x, start_y, blanket: set, joe: dict) -> int:
    s = 0
    for (x, y) in blanket:
        nx, ny = start_x + x, start_y + y
        if (nx, ny) not in joe.keys():
            continue
        s += joe[(nx, ny)]
    return s
            

def main():
    blanket_input = open("blanket.txt").read().split("\n")
    
    blanket = set()
    for y in range(len(blanket_input)):
        for x in range(len(blanket_input[y])):
            if blanket_input[y][x] == "x":
                blanket.add((x, y))
    
    joe = {}
    joe_input = open("joe.txt").read().rstrip().split("\n")
    for y in range(len(joe_input)):
        for x in range(len(joe_input[y])):
            c = joe_input[y][x]
            if c == " ":
                joe[(x, y)] = 0
            else:
                joe[(x, y)] = int(c)
    
    res = 0
    for y in range(len(joe_input)):
        for x in range(len(joe_input[y])):
            res = max(res, place_blanket(x, y, blanket, joe))
    
    print(res)
    

if __name__ == "__main__":
    main()