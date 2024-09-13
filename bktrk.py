### Generating All Permutations

import copy

perms = []
def bkprm(nArr, lst):
    for i in range(len(nArr)):
        cnA = copy.deepcopy(nArr)
        nlst = copy.deepcopy(lst)
        u = cnA.pop(i)
        nlst.append(u)
        if len(cnA) == 0:
            perms.append(nlst)
        else:
            bkprm(cnA, nlst)
            
bkprm(list(range(3)),[])
print(perms)



### Subset-Sum Problem

nA = [1,3,4,6,7,8]
nd = 10

import copy

sols = []
def bktrk(Arr, d):
    sumArr = []
    for an in Arr:
        sumArr += [an]
        nArr = copy.deepcopy(Arr)
        nArr.remove(an)
        if sum(sumArr) == d:
            if sumArr not in sols:
                sols.append(sumArr)
            return None
        else:
            bktrk(nArr, d)

bktrk(nA,nd)
print(sols)



### Hamiltonian Circuit Problem

HG = [[0,1,1,1,0,0],[1,0,1,0,0,1],[1,1,0,1,1,0],[1,0,1,0,1,0],[0,0,1,1,0,1],[0,1,0,0,1,0]]

import copy

sols = []
def bktrkg(graph, s, p, vp):
    for i in range(len(graph)):
        if graph[p][i] != 0 and i not in vp:
            nv = copy.deepcopy(vp)
            nv += [i]
            if len(nv) == len(graph) and i == s:
                sols.append(nv)
            else:
                bktrkg(graph,s,i,nv)
    
bktrkg(HG,0,0,[])
print(sols)



### n-queen placement problem

n = 4

def pq(i,j):
    occp = set()
    occp.add((i,j))
    for a in range(n-1,-n,-1):
        if i+a in list(range(n)):
            occp.add((i+a,j))
        for b in range(n-1,-n,-1):
            if j+b in list(range(n)):
                occp.add((i,j+b))
            if i+a in list(range(n)) and j+a in list(range(n)):
                occp.add((i+a,j+a))
            if i+a in list(range(n)) and j-a in list(range(n)):
                occp.add((i+a,j-a))
    return occp

cnt = [0]
init = set()
def bknq(i, pla):
    for b in range(n):
        if pla.isdisjoint({(i,b)}):
            if i == n-1:
                cnt[0] += 1
            else:
                bknq( i+1, pla.union(pq(i,b)))
bknq(0, init)
print('number of solutions: ', cnt[0])



### two simple btrking tasks

bktp = [0,1,2,3,5,6,7]
def bk(i, bktp):
    if i == len(bktp)-1:
        return True
    else:
        if i == bktp[i]:
            return bk(i+1, bktp)
        else:
            return False

bktp2 = [[0,1],[1,2],[0,4],[0,5],[0,7],[3,4]]
def bk2(i, bktp, s):
    for k in bktp[i]:
        if k % 2 == 1:
            if i == len(bktp)-1:
                return True, s+str(k)
            else:
                return bk2(i+1, bktp, s+str(k))
    return False, s



### Knight's tour codes 

n = 3
dcb = [[0]*n for _ in range(n)]

moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

def find_availablemoves(i,j,cb):
    amvs=[]
    for mv in moves:
        try:
            if cb[i+mv[0]][j+mv[1]] == 0 and i+mv[0] in list(range(n)) and j+mv[1] in list(range(n)):
                amvs.append(mv)
        except:
            continue
    return amvs

def isfilled(cb):
    acsum = 0
    for i in range(len(cb)):
        acsum += sum(cb[i])
    return acsum == len(cb)**2

print(find_availablemoves(0,0,dcb))
print(isfilled(dcb))

import copy

def bktrk_moves(i,j,cb):
    amvs = find_availablemoves(i,j,cb)
    #print(ncb)
    if len(amvs) == 0:
        if isfilled(cb):
            return True
    elif len(amvs) != 0:
        for amv in amvs:
            ncb = copy.deepcopy(cb)
            ncb[i+amv[0]][j+amv[1]] = 1
            if bktrk_moves(i+amv[0],j+amv[1],ncb):
                hist.append((i+amv[0],j+amv[1]))
                return True
            else:
                continue
                
hist = [(0,0)]
#dcb[0][0] = 1      # for open tour
dcb[1][1] = 1      # amending for close tour with 3x3 cb

'''                 # testing for 4x4
dcb = [[1]*n for _ in range(n)]
dcb[1][2] = 0
dcb[2][1] = 0
dcb[-1][-1] = 0
'''

tv = bktrk_moves(0,0,dcb)
print(tv)
if tv:
    print(hist)
