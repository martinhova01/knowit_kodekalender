from collections import deque
from copy import deepcopy
from tqdm import tqdm


import sys
sys.path.append("../..")
from utils import adjacent4



memo = {}

def bfs(board, start_x, start_y):
    R = len(board)
    C = len(board[0])
    label = board[start_y][start_x]
    visited = set()
    q = deque([(start_x, start_y)])
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for nx, ny in adjacent4(x, y):
            if nx < 0 or nx >= C or ny < 0 or ny >= R:
                continue
            if board[ny][nx] == label:
                q.append((nx, ny))
    
    return visited

def find_groups(board):
    R = len(board)
    C = len(board[0])
    groups = []
    done = set()
    for y in range(R):
        for x in range(C):
            if (x, y) in done or board[y][x] == "x":
                continue
            visited = bfs(board, x, y)
            groups.append(visited)
            done.update(visited)
    
    return groups

def remove_group(board, group):
    for (x, y) in group:
        board[y][x] = "x"
    
    R = len(board)
    C = len(board[0])
    for y in range(R - 2, -1, -1):
        for x in range(C):
            label = board[y][x]
            if label == "x":
                continue
            i = 1
            while board[y + i][x] == "x":
                board[y + i][x] = label
                board[y + i - 1][x] = "x"
                i += 1
                if y + i >= R:
                    break
            
    
def solve(board, num_moves, group):
    remove_group(board, group)
    groups = find_groups(board)
    if not groups:
        return num_moves
    
    hashable = (tuple(tuple(line) for line in board), num_moves)
    if hashable in memo:
        return memo[hashable]
    res = min(solve(deepcopy(board), num_moves + 1, g) for g in groups)
    memo[hashable] = res
    return res
            

def main():
    boards = open("stekebrett.txt", encoding="utf-8").read().rstrip().split("\n\n")
    boards = [[list(line) for line in b.split("\n")] for b in boards]
    
    s = 0
    for board in tqdm(boards):
        s += solve(board, 0, {})
    print(s)
    

main()
