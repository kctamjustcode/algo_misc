nums = [1,2,3,4,5]

while len(nums) != 1:
    procs_nums = [int(str(nums[i]+nums[i+1])[-1]) for i in range(len(nums)-1)]
    nums = procs_nums

print(nums[0])
