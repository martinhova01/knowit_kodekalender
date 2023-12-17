import time
import re
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from tqdm import tqdm


class Solution():
    def __init__(self):
        self.filename = "input.txt"
        self.parse()
        
    def solve(self):
        fig, ax = plt.subplots()
        for i in tqdm(range(len(self.lights))):
            a, b, c = self.coeffs[i]
            for arc_length, intensity, r in self.lights[i]:
                x = self.getX(a, b, c, arc_length)
                y = self.getY(a, b, c, x)
                circle = patches.Circle((x, y), r, edgecolor='g', facecolor='g', alpha=intensity)
                ax.add_patch(circle)

        ax.set_xlim(0, 2000)
        ax.set_ylim(0, 2000)
        plt.show()
        
        
    def getX(self, a, b, c, target):
        tol = 10
        approximate = 0
        end = 0
        while abs(approximate - target) > tol:
            end += 1
            x = np.linspace(0, end, num=100)
            integrand = np.sqrt(1 + 4*(a**2)*(x**2) + 4*a*b*x + b**2)
            approximate = np.trapz(integrand, x)
        return end
    
    def getY(self, a, b, c, x):
        return np.polyval([a,b, c], x)
            
    
    def parse(self):
        self.width, self.height = (int(x) for x in re.findall(r"\d+", open(self.filename).read().split("\n")[0]))
        
        lines = open(self.filename).read().split("\n")[1:]
        self.coeffs = []
        self.lights = []
        for line in lines:
            split = line.split(": (")
            self.coeffs.append(eval(split[0].replace(" ", ", ")))
            lights_line = []
            for triplet in split[1].split(") ("):
                if triplet.endswith(")"):
                    triplet = triplet[:-1]
                f = triplet.split()
                lights_line.append((float(f[0]), float(f[1]), float(f[2])))
                
            self.lights.append(lights_line)
            
        
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()