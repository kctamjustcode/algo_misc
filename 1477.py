import copy, math

substring_with_sum = [[]]

def find_all_sub_arrays(num_list, target):
    print(num_list)
    for item in num_list:
        for i in range(len(item)):
            for j in range(i+1, len(item)+1):
                if sum(item[i:j]) == target:
                    #print(item, i,j )
                    substring_with_sum[0] += [(item[i:j], (i, j-1))]       ## adding indexing item and check overlapping
                    #print(item[i:j])
                    new_num_list = copy.deepcopy(num_list)
                    new_num_list.remove(item)
                    if item[:i] != []:
                        new_num_list += [item[:i]]
                    if item[j:] != []:
                        new_num_list += [item[j:]]
                    
                    #print(new_num_list)
                    #if new_num_list != num_list:
                        #find_all_sub_arrays(new_num_list, target)

def overlapping(item1, item2):
    case1 = item1[0] in range(item2[0], item2[1]+1)
    case2 = item1[1] in range(item2[0], item2[1]+1)
    return case1 or case2

#find_all_sub_arrays([[3,2,2,4,3]], 3)
find_all_sub_arrays([[7,3,4,7]], 7)
print(substring_with_sum[0])

def final_lens(num):
    min_cnt = math.inf
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if not overlapping(num[i][1], num[j][1]):
                min_cnt = min(min_cnt, len(num[i][0])+len(num[j][0]))
    return min_cnt

print(final_lens(substring_with_sum[0]))

