import math, copy

nums = [2,1,3,5,2]

def conditioning(i, num):
    valid_indice = []
    for j in range(len(num)):
        if i < j and num[j] < num[i]:
            valid_indice += [j]
        elif i > j and num[j] > num[i]:
            valid_indice += [j]
    return valid_indice

def farthest_possible(i, num):
    max_cnt = i
    for j in range(i+1, len(num)):
        if num[i] > num[j]:
            max_cnt = j
    return max_cnt

def largest_possible(i, num):
    largest_cnt = num[i]
    for j in range(i):
        if num[j] > largest_cnt:
            largest_cnt = num[j]
    return largest_cnt

print(largest_possible(farthest_possible(2, nums), nums))

print([largest_possible(farthest_possible(k, nums), nums) for k in range(len(nums))])
