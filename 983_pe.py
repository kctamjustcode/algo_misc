import math, copy

board_size = 10

grids = [(i, j) for i in range(board_size) for j in range(board_size)]

print(grids)

def dist_rad(pnt1, pnt2):
    return math.sqrt((pnt1[0]-pnt2[0])**2+(pnt1[1]-pnt2[1])**2)

possi_rad = list(set([dist_rad((0,0), grid) for grid in grids]))
possi_rad.remove(0)

'''
#center = (2, 2)
#radi = 2

for grid in grids:
    if dist_rad(center, grid) == radi:
        print(grid, radi)
'''

def grid_point_cir(cent, radi):
    pnts = []
    for grid in grids:
        if dist_rad(cent, grid) == radi:
            pnts += [grid]
    return pnts

for radis in possi_rad:
    if radis < 3:
        print(radis)

def valid_cent(cent):
    for radi in possi_rad:
        grid_pnt_cirs = grid_point_cir(cent, radi)
        if len(grid_pnt_cirs) >= 4:
            valid_cnt = [False, False, False, False]
            total_valid = True
            for grid in grid_pnt_cirs:
                if grid[0] > cent[0]:
                    valid_cnt[0] = True
                if grid[0] < cent[0]:
                    valid_cnt[1] = True
                if grid[1] > cent[1]:
                    valid_cnt[2] = True
                if grid[1] < cent[1]:
                    valid_cnt[3] = True
            for valida in valid_cnt:
                if valida == False:
                    total_valid = False
            if total_valid:
                return True
    return False

#print(grid_point_cir(center, radi))
#print(valid_cent((0,0)))

def valid_harmn(cent1, cent2):
    cent_dist = dist_rad(cent1, cent2)
    min_radi = math.inf
    if cent1 == cent2:
        return False, min_radi
    for radi1 in possi_rad:
        #for radi2 in possi_rad:     # invalid due to rule #3
        intesct_cnt = 0
        #if radi1 <= cent_dist: #and radi2 <= cent_dist:
        grids1 = grid_point_cir(cent1, radi1)
        grids2 = grid_point_cir(cent2, radi1)
        #print(grids1)
        if len(grids1) >= 4 and len(grids2) >= 4:
            for grid in grids:
                if grid in grids1 and grid in grids2:
                    intesct_cnt += 1
            if intesct_cnt == 2:
                min_radi = min(min_radi, radi1)
                #print(grids1, grids2)
                return True, min_radi
    return False, min_radi

print(valid_harmn((2,2),(3,3)))
print(valid_harmn((3,3),(3,3)))
print(valid_harmn((0,0),(0,0)))

three_circles_cases = [[]]
min_disct = [math.inf]

def gen_pairs(ls):
    pairs = []
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            pairs += [(ls[i], ls[j])]
    return pairs

ls_testing = [(3,3),(4,4),(4,6),(7,3)]
harmn = True
print(gen_pairs(ls_testing))

def valid_harmn_shrnt(ls):
    harmn = True
    harmn_radi = []
    for pair in gen_pairs(ls):
        vaild_harmn_test = valid_harmn(pair[0], pair[1])
        harmn_radi += [vaild_harmn_test[1]]
        if vaild_harmn_test[0]:
            if len(harmn_radi) >= 2:
                if harmn_radi[-1] == harmn_radi[-2]:
                    continue
                elif harmn_radi[-1] != harmn_radi[-2]:
                    harmn = False
                    break
        else:
            harmn = False
            break
    return harmn

def valid_harmn_radi(cent1, cent2, radi):
    #cent_dist = dist_rad(cent1, cent2)
    if cent1 == cent2:
        return False
    else:
        #for radi2 in possi_rad:     # invalid due to rule #3
        intesct_cnt = 0
        #if radi1 <= cent_dist: #and radi2 <= cent_dist:
        grids1 = grid_point_cir(cent1, radi)
        grids2 = grid_point_cir(cent2, radi)
        #print(grids1)
        if len(grids1) >= 4 and len(grids2) >= 4:
            for grid in grids:
                if grid in grids1 and grid in grids2:
                    intesct_cnt += 1
            if intesct_cnt == 2:
                return True
    return False

def valid_harmn_radi_shrtn(ls):
    min_radi = math.inf
    for radi in possi_rad:
        all_valid = False
        for pair in gen_pairs(ls):
            if not valid_harmn_radi(pair[0], pair[1], radi):    # giving up radi part by a math hypo
                break
            else:
                continue
        if not all_valid:
            continue
        else:
            min_radi = min(min_radi, radi)
            yield True, radi
    return False, min_radi
        

print('tested', harmn)

print(valid_cent((3,3)))
print(valid_cent((4,4)))


def gen_length_sol_radi(ls, n):
    if len(three_circles_cases[0]) > 0:
        print(three_circles_cases[0])
        return
    if len(ls) == n:
        print(ls)
        test_radi = valid_harmn_radi_shrtn(ls)
        if test_radi[0]:
            three_circles_cases[0] += (ls, test_radi[1])

    elif len(ls) < n:
        for grid in grids:
            if valid_cent(grid):
                ls_next = copy.deepcopy(ls)
                ls_next += [grid]
                if len(ls_next) >= 2:
                    if valid_harmn_shrnt(ls_next):
                        gen_length_sol_radi(ls_next, n)
                else:
                    gen_length_sol_radi(ls_next, n)


def gen_length_sol(ls, n):
    if len(three_circles_cases[0]) > 0:
        #print(three_circles_cases[0])
        return
    if len(ls) == n:
        harmn = True
        for pair in gen_pairs(ls):
            vaild_harmn_test = valid_harmn(pair[0], pair[1])
            if vaild_harmn_test[0]:
                continue
            else:
                harmn = False
                break
        if harmn:
            #print(ls)
            min_disct[0] = min(min_disct[0], vaild_harmn_test[1])
            three_circles_cases[0] += [ls]
            print(ls, min_disct[0])

    elif len(ls) < n:
        for grid in grids:
            if valid_cent(grid):
                ls_next = copy.deepcopy(ls)
                ls_next += [grid]
                if len(ls_next) >= 2:
                    if valid_harmn_shrnt(ls_next):
                        gen_length_sol(ls_next, n)
                else:
                    gen_length_sol(ls_next, n)

                    
gen_length_sol([], 4)
print(three_circles_cases[0])
print(min_disct[0])
        


