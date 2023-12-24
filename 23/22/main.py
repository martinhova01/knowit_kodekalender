import time
from collections import deque

class Solution():
    def __init__(self):
        self.stars = self.parseStars()
        self.path = [eval(f"({line})") for line in open("path.txt").read().split("\n")]
        self.observedStars = set()
        # self.stars = [deque([" ", 2, 3]), deque([1, " ", " "])]
        # self.x, self.y = -1, -1
        
    def parseStars(self):
        counter = 0
        stars = []
        for line in open("stars.txt").read().split("\n"):
            new_line = deque()
            for c in line:
                if c == " ":
                    new_line.append(" ")
                if c == "*":
                    new_line.append(counter)
                    counter += 1
            stars.append(new_line)
            
        return stars
        
        
        
        
    def solve(self):
        print(self.path)
        self.x, self.y = self.path[0]
        for i in range(1, len(self.path)):
            next_x, next_y = self.path[i]
            
            dir = None
            if self.x < next_x:
                dir = (1, 0)
            elif self.x > next_x:
                dir = (-1, 0)
            elif self.y < next_y:
                dir = (0, 1)
            elif self.y > next_y:
                dir = (0, -1)
                
            while self.x != next_x or self.y != next_y:
                self.countStars()
                self.x += dir[0]
                self.y += dir[1]
                self.moveStarsLeft()
            
        return len(self.observedStars)
            
    
    def countStars(self):
        for y in range(-2, 3):
            if y == -2 or y == 2:
                for x in range(-2, 3):
                    _x, _y = self.x + x, self.y + y
                    if self.stars[_y][_x] != " ":
                        self.observedStars.add(self.stars[_y][_x])
            if y == -1 or y == 1:
                for x in range(-4, 5):
                    _x, _y = self.x + x, self.y + y
                    if self.stars[_y][_x] != " ":
                        self.observedStars.add(self.stars[_y][_x])
            if y == 0:
                for x in range(-5, 6):
                    _x, _y = self.x + x, self.y + y
                    if self.stars[_y][_x] != " ":
                        self.observedStars.add(self.stars[_y][_x])
    
    def moveStarsLeft(self):
        for i in range(len(self.stars)):
            self.stars[i].append(self.stars[i].popleft())
            
    
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()