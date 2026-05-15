import math, copy

def vaild_containing_set(intvls, num):
    for intvl in intvls:
        cnt = 0
        for inte in range(intvl[0], intvl[-1]+1):
            if inte in num:
                cnt += 1
                if cnt > 2:
                    continue
        if cnt < 2:
            return False
    return True

intervals = [[1,3],[1,4],[2,5],[3,5]]
print(vaild_containing_set(intervals, [2,3,4]))

max_intvl = list(range(intervals[0][0], intervals[-1][-1]+1))
print(max_intvl)

total_lvl_lst = [ [] for _ in range(len(max_intvl))]
def minimal_length(intvls, num, k):
    if vaild_containing_set(intvls, num) and len(num) == k:
        total_lvl_lst[k] += [num]
        return  # ***
    else:
        #mini = math.inf
        for i in range(len(num)):
            num_cp = copy.deepcopy(num)
            #pped = num_cp.pop(i)
            num_cp.pop(i)
            minimal_length(intvls, num_cp, k)

for i in range(2, len(max_intvl)):
    minimal_length(intervals, max_intvl, i)
    if total_lvl_lst[i] != []:
        print(i)
        break

#print(total_lvl_lst)