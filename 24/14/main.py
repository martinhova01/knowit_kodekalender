nums = {i: 100_000 for i in range(10)}
order = []
lines = 0
while any(nums[i] > 0 for i in range(10)):
    lines += 1
    for i in range(9, -1, -1):
        if i in order:
            # det er 0 i-ere igjen
            if i == 0:
                nums[0] = max(0, nums[0] - 2)
            else:   
                nums[0] = max(0, nums[0] - 1)
            if nums[0] == 0 and 0 not in order:
                order.append(0)
            continue
        
        # det er n i-ere igjen
        n = nums[i]
        for c in str(n):
            int_c = int(c)
            if int_c in order:
                continue
            nums[int_c] = max(0, nums[int_c] - 1)
            if nums[int_c] == 0 and int_c not in order:
                order.append(int_c)
                
        nums[i] = max(0, nums[i] - 1)
        if nums[i] == 0 and i not in order:
            order.append(i)
        
print(lines, ",".join(str(x) for x in order))