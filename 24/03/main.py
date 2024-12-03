class Elf:
    def __init__(self):
        self.plate = {
            "ris": 100,
            "erter": 100,
            "gulrøtter": 100,
            "reinsdyrkjøtt": 100,
            "julekringle": 100,
        }
        self.refills = [
            [0, 0, 1, 0, 0, 2],
            [0, 3, 0, 0],
            [0, 1, 0, 0, 0, 8],
            [100, 80, 40, 20, 10]
        ]
        self.order = ("ris", "erter", "gulrøtter", "reinsdyrkjøtt", "julekringle")
        self.t = 0
        self.do_refill = [
            lambda t: True,
            lambda t: True,
            lambda t: t >= 30,
            lambda t: False,
            lambda t: False,
            ]
        self.refill_indexes = [0, 0, 0, 0, 0]
        self.no_meat = False
        
    def simulate(self) -> int:
        while self.plate["julekringle"] > 0:
            self.time_step()
        return self.t
    
    def time_step(self):
        
        # find what to eat
        eat = []
        for i, food in enumerate(self.order):
            amount = self.plate[food]
            if amount == 0:
                continue
            
            if i < 3:
                eat.append(food)
                continue
            
            if food == "reinsdyrkjøtt" and len(eat) == 0:
                self.plate[food] = max(0, self.plate[food] - 2)
                if self.plate[food] == 0:
                    if self.no_meat:
                        break
                    next_t = self.t + 50
                    self.do_refill[3] = lambda t: t == next_t
                break
            
            elif food == "julekringle" and len(eat) == 0:
                self.plate[food] -= 1
                break
            
        if eat:
            self.plate[eat[0]] = max(0, self.plate[eat[0]] - 5)
            if len(eat) > 1:
                self.plate[eat[1]] = max(0, self.plate[eat[1]] - 3)
                
        
        # refills
        for i, food in enumerate(self.order):
            if self.do_refill[i](self.t):
                self.plate[food] += self.refills[i][self.refill_indexes[i]]
                
                # done refilling reinsdyrkjøtt
                if i == 3 and self.refill_indexes[i] == 4:
                    self.no_meat = True
                    break
                self.refill_indexes[i] =  (self.refill_indexes[i] + 1) % len(self.refills[i])
        
        self.t += 1
    
    
def main():
    print(Elf().simulate())

if __name__ == "__main__":
    main()
    