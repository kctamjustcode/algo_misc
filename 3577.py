import math, copy

def monocity(lst):
    for i in range(1, len(lst)):
        if lst[i] != lst[0]:
            return False
    return True

def decrypted(num, comp):
    assert len(num) == len(comp)
    validity = [False for _ in range(len(num))]
    validity[0] = True
    for i in range(len(num)):
        for j in range(i):
            if comp[num[j]] < comp[num[i]]:
                validity[i] = True
                break
    return monocity(validity)

print(decrypted([0,1,2], [1,2,3]))


complx = [3,3,3,4,4,4]

n = len(complx)
nums = list(range(n))
permu = [[]]

def permutation(num, lst):
    if len(num) == 0:
        return lst
    else:
        for i in range(len(num)):
            num_cp = copy.deepcopy(num)
            num_cp.pop(i)
            lst_cp = copy.deepcopy(lst)
            lst_cp += [num[i]]
            permu[0] += [permutation(num_cp, lst_cp)]
        #return None
    
permutation(nums, [])

def clean_none():
    while None in permu[0]:
        permu[0].remove(None)

clean_none()
print(len(permu[0]))

solu = 0
for perm in permu[0]:
    #if decrypted(perm, [1,2,3]):
    if decrypted(perm, complx):
        solu += 1
print(solu)



