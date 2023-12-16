from collections import deque
import time
from PIL import Image

class Img():
    def __init__(self, label, taps):
        self.label = label
        self.taps = deque(taps) #[up, right, down, left]
        self.adj = deque([None, None, None, None]) #[up, right, down, left]
        self.rotations = 0
        self.pos = None
        
    def rotateCounterClockWise(self):
        self.taps.append(self.taps.popleft())
        self.adj.append(self.adj.popleft())
        self.rotations += 1
        

class Solution():
    def __init__(self):
        self.data = [Img(line.split(".jpg, ")[0] + ".jpg", eval(line.split(".jpg, ")[1])) for line in open("puzzle.txt").read().rstrip().split("\n")]
        self.inputPaths = [("pieces/" + img.label) for img in self.data]
        self.adjMapping = {0: 2, 1: 3, 2: 0, 3: 1}
        self.topLeft = None
        
    def solve(self):
            #find the top left image
        taps = []
        for img in self.data:
            for tap in img.taps:
                if tap != -1:
                    taps.append(tap)
            if img.taps[0] == img.taps[3] == -1:
                self.topLeft = img
                self.topLeft.pos = (0, 0)
                
        target = sum(taps) / (len(taps) / 2)
                    
        q = deque()
        q.append(self.topLeft)
        visited = set()
        visited.add(self.topLeft)
        
        while q:
            img = q.popleft()
            for i in range(4):
                tap = img.taps[i]
                if tap == -1:
                    continue
                targetTap = target - tap
                nextimg, nextTapOrientation = self.findMatch(targetTap)
                        
                if nextimg in visited:
                    continue
                
                    #rotate next piece to fit correctly
                while self.adjMapping[i] != nextTapOrientation:
                    nextimg.rotateCounterClockWise()
                    nextTapOrientation =  (nextTapOrientation - 1) % 4
                    
                img.adj[i] = nextimg
                nextimg.adj[self.adjMapping[i]] = img
                if i == 0:
                    nextimg.pos = (img.pos[0], img.pos[1] - 1)
                if i == 1:
                    nextimg.pos = (img.pos[0] + 1, img.pos[1])
                if i == 2:
                    nextimg.pos = (img.pos[0], img.pos[1] + 1)
                if i == 3:
                    nextimg.pos = (img.pos[0] - 1, img.pos[1] - 1)
                q.append(nextimg)
                visited.add(nextimg)
        
        self.generateResult()
                
            
    def findMatch(self, targetTap):
        for adjImg in self.data:
            for j in range(4):
                if adjImg.taps[j] == targetTap:
                    return adjImg, j
    
    
    def generateResult(self):
        width = Image.open(self.inputPaths[0]).width
        height = Image.open(self.inputPaths[0]).height
        result = Image.new('RGB', (width * 26, height * 26))
            
        for img in self.data:
            i = Image.open("pieces/" + img.label)
            for _ in range(img.rotations):
                i = i.rotate(90)
            result.paste(i, (img.pos[0] * i.width, img.pos[1] * i.height))
            
        result.save("result.jpg")

    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()