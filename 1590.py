import copy

def divisible_subarray(num, p):
    if sum(num) % p == 0:
        return len(num)
    else:
        max_length = 0
        for i in range(len(num)):
            num_cp = copy.deepcopy(num)
            num_cp.pop(i)
            max_length = max(max_length, divisible_subarray(num_cp, p))
        #print(max_length)
        return max_length
    
print(divisible_subarray([3,1,4,2], 6))
print(divisible_subarray([6,3,5,2], 9))
print(divisible_subarray([1,2,3], 3))
