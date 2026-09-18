import math, copy

def conditioning(nums):
    for i in range(1, len(nums)-1):
        if nums[i-1] < nums[i] < nums[i+1] or nums[i-1] > nums[i] > nums[i+1]:
            return False
        if nums[i-1] == nums[i]:
            return False
    if nums[-1] == nums[-2]:
        return False
    return True

