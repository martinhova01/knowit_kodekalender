from collections import defaultdict

def alvesort(input: list):
    n = len(input)
    swap_counter = 0
    fest_counts = defaultdict(int)
    i = 1
    while i < n:
        if i > 0 and input[i][1] < input[i - 1][1]:
            input[i], input[i - 1] = input[i - 1], input[i]
            swap_counter += 1
            if swap_counter % 7 == 0:
                #fest
                for j in range(i, min(i + 5, n)):
                    fest_counts[input[j][0]] += 1
                input = input[:i] + input[i + 4: i - 1: -1] + input[i + 5:]
            i -= 1
        else:
            i += 1
    return fest_counts


alver = [(x[0], int(x[1])) for line in open("usorterte_alver.txt").read().rstrip().split("\n") for x in [line.split(" ")]]
fest_counts = alvesort(alver)
print(max(fest_counts.items(), key=lambda x: x[1]))