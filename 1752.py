nums = [2,1,3,4]
#nums = [3,4,5,1,2]

torted_cnt = 0
decreased_cnt_list = []
for i in range(len(nums)):
    decreased_cnt = 0
    for j in range(i+1, len(nums)):
        if nums[j] < nums[i]:
            decreased_cnt += 1
    decreased_cnt_list += [decreased_cnt]

'''
while 0 in decreased_cnt_list:
    decreased_cnt_list.remove(0)
'''
print(decreased_cnt_list)

print(sum(decreased_cnt_list) == (len(decreased_cnt_list)-max(decreased_cnt_list))*max(decreased_cnt_list))
        
