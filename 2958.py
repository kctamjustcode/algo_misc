import math

def max_freq(num):
    corr_freq = dict()
    for item in num:
        if str(item) not in corr_freq.keys():
            corr_freq[str(item)] = 1
        else:
            corr_freq[str(item)] += 1
    #print(corr_freq.values())
    return max(corr_freq.values())

nums = [1,2,2,3,4,5,5,5]
print(max_freq(nums))

def length_of_longest_subarrays(num, k):
    max_cnt = -1*math.inf
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if max_freq(num[i:j]) <= k:
                max_cnt = max(max_cnt, j-i)
    return max_cnt

print(length_of_longest_subarrays(nums, 2))
