import numpy as np

last = 167772150
now = 149848566

num_bars = sum(2**(i - 1) for i in range(1, 25))

orig_weight = last // num_bars

mock_weight = int(orig_weight * 0.7)

A = np.array([[10, 7], [1, 1]])
b = np.array([now, num_bars])

solution = np.linalg.solve(A, b)
num_orig, num_mock = solution

num_mock = int(np.round(num_mock))


target = num_mock
def find_sum(i: int, curr_idx: list[int], curr_sum: int):
    
    if i == 25:
        return None
    
    if curr_sum == target:
        return curr_idx
    
    not_include = find_sum(i + 1, curr_idx, curr_sum)
    
    if not_include:
        return not_include
    
    next_sum = curr_sum + 2**(i - 1)
    next_idx = list(curr_idx)
    next_idx.append(i)
    
    if next_sum > target:
        return None
    
    return find_sum(i + 1, next_idx, next_sum)



idx = find_sum(1, [], 0)


print(f"SjokoladeMg:{orig_weight},MockuladeMg:{mock_weight},AntallMockulader:{num_mock},Luker:{",".join(map(str, idx))}")
