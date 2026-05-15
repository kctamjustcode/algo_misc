import math, copy

nums = [-5, 1, 2, -3, 4]

def max_sum_length_divisible_by_k(num, k):
    if len(num) % k == 0 or k == 1:
        return sum(num)
    else:
        max_sum = -1* math.inf
        for i in range(len(num)):
            num_cp = copy.deepcopy(num)
            num_cp.pop(i)
            if i == 0:
                print(num_cp)
            max_sum = max(max_sum, max_sum_length_divisible_by_k(num_cp, k))
        return max_sum
    
print(max_sum_length_divisible_by_k(nums, 2))

