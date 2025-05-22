import copy

F = [0]

def move_one(Lst, nu, h):
    Lst_cp = copy.deepcopy(Lst)
    if Lst[nu] >= h:
        Lst_cp[nu] -= h
        return sorted(Lst_cp, reverse=True)
    else:
        return Lst

def move_two(Lst, nu, a, b):
    Lst_cp = copy.deepcopy(Lst)
    if Lst_cp[nu] >= 2 and a != 0 and b != 0:
        Lst_cp.pop(nu)
        Lst_cp += [a,b]
        return sorted(Lst_cp, reverse=True)
    else:
        return Lst

def count_exact_one_nonzero(Z):
    cnt = 0
    for z in Z:
        if z != 0:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def player_win(Lst):
    if count_exact_one_nonzero(Lst) and sum(Lst) in [1,2,4,9]:
        return True
    else:
        for i in range(2):
            if i == 0:
                for j in range(len(Lst)):
                    for n in [1,2,4,9]:
                        if move_one(Lst, j, n) != Lst:
                            Lst_new = move_one(Lst, j, n)
                            if not player_win(Lst_new):
                                return True
            if i == 1:
                for j in range(len(Lst)):
                    for alpha in range(Lst[j]):
                        if move_two(Lst, j, alpha, Lst[j]-alpha) != Lst:
                            Lst_new = move_two(Lst, j, alpha, Lst[j]-alpha)
                            if not player_win(Lst_new):
                                return True
        return False

print(player_win(sorted([2,2], reverse=True)))
