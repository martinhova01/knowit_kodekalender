import time
import math as m

#breddegrad: grader nord for ekvator (større verdier betyr lenger nord)
#lengdegrad: grader øst for greenwitch (større verdier betyr lenger øst)

def dist(x1, y1, x2, y2):
    return m.sqrt((x1 - x2)**2 + (y1 - y2)**2) * 55_500
    
     
class Solution():
    def __init__(self):
        self.filename = "gateadresser_oslo_koordinater_liten.txt"
        self.data = [(float(line.split()[0]), float(line.split()[1])) for line in open(self.filename).read().rstrip().split("\n")]
        self.dirs = [self.get_north, self.get_east, self.get_south, self.get_west]
    
    
    def get_north(self, l):
        largest = l[0]
        for coord in l:
            if coord[0] > largest[0]:
                largest = coord
            elif coord[0] == largest[0]:
                if coord[1] > largest[1]:
                    largest = coord
        return largest
        
    def get_east(self, l):
        largest = l[0]
        for coord in l:
            if coord[1] > largest[1]:
                largest = coord
            elif coord[1] == largest[1]:
                if coord[0] < largest[0]:
                    largest = coord
        return largest
    
    def get_south(self, l):
        largest = l[0]
        for coord in l:
            if coord[0] < largest[0]:
                largest = coord
            elif coord[0] == largest[0]:
                if coord[1] < largest[1]:
                    largest = coord
        return largest
    
    def get_west(self, l):
        largest = l[0]
        for coord in l:
            if coord[1] < largest[1]:
                largest = coord
            elif coord[1] == largest[1]:
                if coord[0] > largest[0]:
                    largest = coord
        return largest
        
    def solve(self):
        times = []
        times.append(self.mode1(2000, 62, 0.1))
        times.append(self.mode1(1000, 22, 0.05))
        times.append(self.mode1(500, 16, 0.002))
        
        times.append(self.mode2(2000, 62, 0.1))
        times.append(self.mode2(1000, 22, 0.05))
        times.append(self.mode2(500, 16, 0.002))
        
        times.append(self.mode3(2000, 62, 0.1))
        times.append(self.mode3(1000, 22, 0.05))
        times.append(self.mode3(500, 16, 0.002))
        
        print(times)
        return min(times)
    
    def mode1(self, radius, reload_time, overheat_cooeff):
        min_radius = radius * 0.2
        overheat = 1 - overheat_cooeff
        l = list(self.data)
        time = 0
        r = radius
        while l:
            point = self.get_north(l)
            new_l = []
            for (x, y) in l:
                if dist(x, y, point[0], point[1]) > r:
                    new_l.append((x, y))
            l = new_l
            r = max(min_radius, radius * overheat)
            overheat -= overheat_cooeff
            time += reload_time
        
        time -= reload_time
        
        return time 
        
        
        
    def mode2(self, radius, reload_time, overheat_cooeff):
        r = radius
        dir_counter = 0
        min_radius = radius * 0.2
        overheat = 1 - overheat_cooeff
        l = list(self.data)
        time = 0
        while l:
            point = self.dirs[dir_counter](l)
            dir_counter = (dir_counter + 1) % 4
            new_l = []
            for (x, y) in l:
                if dist(x, y, point[0], point[1]) > r:
                    new_l.append((x, y))
            l = new_l
            r = max(min_radius, radius * overheat)

            overheat -= overheat_cooeff
            time += reload_time
        
        time -= reload_time
        
        return time 
        
        
    def mode3(self, radius, reload_time, overheat_cooeff):
        r = radius
        dir_counter = 0
        min_radius = radius * 0.2
        overheat = 1 - overheat_cooeff
        l = list(self.data)
        time = 0
        while l:
            point = self.dirs[dir_counter](l)
            new_l = []
            for (x, y) in l:
                if dist(x, y, point[0], point[1]) > r:
                    new_l.append((x, y))
            l = new_l
            r = max(min_radius, radius * overheat)
            overheat -= overheat_cooeff
            time += reload_time
            if len(l) % 5 == 0:
                continue
            elif len(l) % 2 == 0:
                dir_counter = (dir_counter - 1) % 4
            else:
                dir_counter = (dir_counter + 1) % 4
        
        time -= reload_time
        
        return time 
    
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()