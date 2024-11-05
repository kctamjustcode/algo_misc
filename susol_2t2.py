import copy, random

gameboard = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def clean_zero(array):
    cpary = copy.deepcopy(array)
    while 0 in cpary:
        cpary.remove(0)
    return cpary

def row_check(i, gb):
    rcary = copy.deepcopy(gb[i])
    stary = set(rcary)
    stary.discard(0)
    if stary is not None:
        return len(clean_zero(rcary)) == len(list(stary))
    else:
        return True
    
def col_check(j, gb):
    ccary = copy.deepcopy([gb[i][j] for i in range(len(gb))])
    stary = set(ccary)
    stary.discard(0)
    if stary is not None:
        return len(clean_zero(ccary)) == len(list(stary))
    else:
        return True

def r_check(gb):
    for i in range(len(gb)):
        if row_check(i, gb) is not True:
            return False
    return True

def c_check(gb):
    for j in range(len(gb)):
        if col_check(j, gb) is not True:
            return False
    return True

def block_check(gb):
    blk = [[(0,0),(0,1),(1,0),(1,1)],[(0,2),(0,3),(1,2),(1,3)],[(2,0),(2,1),(3,0),(3,1)],[(2,2),(2,3),(3,2),(3,3)]]
    for bk in blk:
        chkary = copy.deepcopy([gb[itn[0]][itn[1]] for itn in bk])
        stary = set(chkary)
        stary.discard(0)
        if stary is not None:
            if len(clean_zero(chkary)) != len(list(stary)):
                return False
    return True

def board_fillup(gb):
    for a in range(len(gb)):
        for b in range(len(gb)):
            if gb[a][b] == 0:
                ngb = copy.deepcopy(gb)
                nrt = list(range(1,5))
                random.shuffle(nrt)
                for i in nrt:
                    ngb[a][b] = i
                    if r_check(ngb) and c_check(ngb) and block_check(ngb):
                        return board_fillup(ngb)
            if a == len(gb)-1 and b == len(gb)-1 and gb[a][b] != 0:
                return gb

print(board_fillup(gameboard))
