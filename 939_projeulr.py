import copy

def step_one(sub, nub):
    sub_cp = copy.deepcopy(sub)
    if sub_cp[nub] != 0:
        sub_cp[nub] -= 1
        return sub_cp
    else:
        return sub_cp

def step_two(sub, nub):
    sub_cp = copy.deepcopy(sub)
    if sub_cp[nub] != 0:
        sub_cp[nub] = 0
        return sub_cp
    else:
        return sub_cp

'''
chara = ['0','1']

def recur_len(m, last_list):
    new_list = []
    if len(last_list[0]) == m:
        return last_list
    for item in last_list:
        for cha in chara:
            new_item = item + cha
            new_list.append(new_item)
    return recur_len(m, new_list)

exhu_list = recur_len(4, [''])
print(exhu_list)
'''

def count_exact_one_nonzero(Z):
    cnt = 0
    for z in Z:
        if z != 0:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def non_empty(Z):
    for z in Z:
        if z != 0:
            return True
    return False

#def vaild_pos(X, Y, c):
#    return step_one(X, c) != X or step_two(Y, c) != Y

# player_one can win
def playone_win(A, B): 
    #print(A, B)
    #if sum(A) == 0 and sum(B) == 0:
    #    return
    if sum(B) == 0 and count_exact_one_nonzero(A):
        return True
    elif sum(A) == 0 and sum(B) == 1:
        return True
    else:
        A_cp = copy.deepcopy(A)
        B_cp = copy.deepcopy(B)
        for a in range(len(A_cp)):
            for i in range(2):
                if i == 0:
                    A_cpn = A_cp
                    for b in range(len(B_cp)):
                        if step_one(B_cp, b) != B_cp:
                            B_cpn = step_one(B_cp, b)
                            if not playone_win(B_cpn, A_cpn):
                                return True
                if i == 1:
                    if step_two(A_cp, a) != A_cp:
                        A_cpn = step_two(A_cp, a)
                        B_cpn = B_cp
                        if not playone_win(B_cpn, A_cpn):
                            return True
       
        return False
        
A = [2]
B = [1,1]
# print(playone_win(A, B))

# independent of first move
def positional_win(A, B):
    return playone_win(A, B) and not playone_win(B, A)

print(positional_win(A,B))

trials = [([2],[0]), ([3],[0]), ([2],[1,1]), ([3],[1]), ([1,1,2],[0]),([2,2],[0]),([1,3],[0])]

for trial in trials:
    if not positional_win(trial[0], trial[1]):
        print(trial)

print('all passed.')
