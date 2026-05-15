import math, copy

def min_num_opera(num, cnt):
    print(num,cnt)
    if sum(num) == len(num) and num[0] == 1:    # do a checking
        return cnt
    #cnt = 0
    min_gcd = math.inf
    #last_index = math.inf
    for i in range(len(num)-1):
        min_gcd = min(min_gcd, math.gcd(num[i], num[i+1]))
    if min_gcd > 1:
        return -1
    elif min_gcd == 1:
        for i in range(len(num)-1):
            if math.gcd(num[i], num[i+1]) == min_gcd:
                num_cp = copy.deepcopy(num)
                if num_cp[i] != 1:
                    num_cp[i] = 1
                    cnt += 1
                elif num_cp[i+1] != 1:
                    num_cp[i+1] = 1
                    cnt += 1
                else:
                    continue
                return min_num_opera(num_cp, cnt)

print(min_num_opera([2,6,3,4],0))
