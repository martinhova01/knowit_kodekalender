import re

nums = {
    # "ti": 54, #!
    "seks": 6,
    "tolv": 12,
    "atten": 18,
    "tjuefire": 24,
    "tretti": 30,
    "trettiseks": 36,
    "førtito": 42,
    "førtiåtte": 48,
    "femtifire": 54,
    "seksti": 60,
    "syttito": 72,
    "syttiåtte": 78,
    "åttifire": 84,
    "nitti": 90,
}

def main():
    s = open("tall.txt", encoding="utf-8").read().rstrip()
    patterns = "|".join(list(sorted(nums.keys(), key=lambda x: len(x), reverse=True)))
    matches = re.findall(patterns, s)
    print(sum(nums[match] for match in matches) // 6)
    
    
if __name__ == "__main__":
    main()