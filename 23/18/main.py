import time

class Solution():
    def __init__(self):
        self.filename = "input.txt"
        self.parse()
        
    def solve(self):
        s = 0
        for graph in range(len(self.prices)):
            for transaction in range(len(self.sellAndBuyPoints[graph])):
                x_point = self.sellAndBuyPoints[graph][transaction][1]
                price = self.prices[graph][x_point]
                numberOfStocks = self.stockNumbers[graph][transaction]
                c = self.sellAndBuyPoints[graph][transaction][0]
                
                if c == "K":
                    s -= (numberOfStocks * price)
                else:
                    s += (numberOfStocks * price)
        return s
    
    def parse(self):
        self.stockNumbers = []
        self.sellAndBuyPoints = []
        self.prices = []
        for graph in range(1, 11):
            s = open("graphs/graph_" + str(graph) + ".txt").read()
            self.stockNumbers.append(eval(f"[{s.split("\n")[151]}]"))
            lines = s.split("\n")
            
                #find start y pos
            start_y = -1
            for i in range(len(lines)):
                if lines[i][0] != " ":
                    start_y = i
                    break
                
            prices = [150 - start_y]
            sellAndBuyPoints = []
            x, y = 0, start_y
            while True:
                x += 1
                if x >= len(lines[y]):
                    break
                c = ""
                for dy in (0, 1, -1):
                    if y + dy >= 151:
                        continue
                    if lines[y + dy][x] != " ":
                        y += dy
                        c = lines[y][x]
                        break
                prices.append(150 - y)
                if c == "K" or c == "S":
                    sellAndBuyPoints.append((c, x))
            self.prices.append(prices)
            self.sellAndBuyPoints.append(sellAndBuyPoints)
        
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()