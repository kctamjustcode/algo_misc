import math, copy

def n_max(num, k):
    max_num = []
    num_cp = copy.deepcopy(num)
    while len(max_num) < k:
        max_num += [max(num_cp)]
        num_cp.remove(max(num_cp))
    return max_num

def n_max_indc(num, k):
    max_num = n_max(num, k)
    max_indice = []
    for i in range(len(max_num)):
        for j in range(len(num)):
            if num[j] == max_num[i] and j not in max_indice:
                max_indice += [j]
                break
    return max_indice

def count_available_batteries(num):
    cnt = 0
    for n in num:
        if n != 0:
            cnt += 1
    return cnt


nums = [1,2,3,3,0]

#print(n_max(nums, 3))
#print(n_max_indc(nums, 3))


n = 2
batteries = [3, 3, 3]
cnt = 0
#while 0 not in batteries:
while count_available_batteries(batteries) >= n:
    max_indice = n_max_indc(batteries, 2)
    #print(max_indice)
    for i in range(len(max_indice)):
        batteries[max_indice[i]] -= 1
    cnt += 1
    print(batteries)

print(cnt)

n = 2
batteries = [1, 1, 1, 1]
cnt = 0
#while 0 not in batteries:
while count_available_batteries(batteries) >= n:
    max_indice = n_max_indc(batteries, 2)
    #print(max_indice)
    for i in range(len(max_indice)):
        batteries[max_indice[i]] -= 1
    cnt += 1
    print(batteries)

print(cnt)
