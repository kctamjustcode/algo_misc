import copy, math

def greatest_sum_divisible_by_three(num, sum):
    if sum % 3 == 0 and sum != 0:
        return sum
    else:
        max_sum = -1*math.inf
        for i in range(len(num)):
            num_cp = copy.deepcopy(num)
            num_cp.pop(i)
            sum_cp = sum + num[i]
            max_sum = max(max_sum, greatest_sum_divisible_by_three(num_cp, sum_cp))
        return max_sum

print(greatest_sum_divisible_by_three([3,6,5,1,8], 0))

print(greatest_sum_divisible_by_three([4], 0))

print(greatest_sum_divisible_by_three([1,2,3,4,4], 0))
