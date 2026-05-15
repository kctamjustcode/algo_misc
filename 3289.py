nums = [0, 3, 2, 1, 3, 2]

dgv = []
completed = False

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            dgv += [nums[i]]
            if len(dgv) == 2:
                print(dgv)
                completed = True
                break
    if completed:
        break

print('done')
