import math, copy

nEmplee = 2
present = [1, 2]
future = [4, 3]

hierarchy = [[1, 2]]

budget = 3

buy_own_stock = [False for _ in range(nEmplee)]
buy_own_stock[0] = True
buying_initial = copy.deepcopy(buy_own_stock)
#buyable = [False for _ in range(nEmplee)]
maxi_profit = [future[i] - math.floor(present[i]/2) for i in range(nEmplee)]
cost = [math.floor(present[i]/2) for i in range(nEmplee)]

def count_buyable_updated_once(bos):
    bos_cp = copy.deepcopy(bos)
    for i in range(nEmplee):
        for hier in hierarchy:
            if hier[1] == i and bos[hier[0]]:
                bos_cp[i] = True
                break
    return bos_cp

def count_buyable_update(bos):
    bos_cp = copy.deepcopy(bos)
    bos_updated = count_buyable_updated_once(bos)
    while bos_updated != bos_cp:
        bos_cp = bos_updated
        bos_updated = count_buyable_updated_once(bos)
    return bos_updated

print(count_buyable_update(buy_own_stock))

buyable = count_buyable_update(buy_own_stock)

'''
def max_profit(bdgt, pft):
    if bdgt < budget:
        return pft
    else:
        maxi = -1 * math.inf
        for i in range(nEmplee):
            pft_cp = pft
            bdgt_cp = bdgt
            if buyable[i] and maxi_profit[i] > 0:
                pft_cp_buy += maxi_profit[i]
                bdgt_cp_buy += cost[i]
                maxi = max(max(maxi, max_profit(bdgt_cp, pft_cp)), max_profit(bdgt_cp_buy, pft_cp_buy))
        return maxi
'''

pft = [1,2,3,4,5,6,4]
cst = [1,1,1,2,2,2,3]

nEp = list(range(len(pft)))
bg = 6

total_list = [ [] ]
length = len(nEp)
def generate_sublist(lst, ppng):
    for i in range(len(lst)):
        lst_cp = copy.deepcopy(lst)
        ppng_cp = copy.deepcopy(ppng)
        popped = lst_cp.pop(i)
        ppng_cp += [popped]
        total_list[0] += [ppng_cp]
        #total_list[0] += [[popped]]
        generate_sublist(lst_cp, ppng_cp)

generate_sublist(list(range(length)),[])
#print(total_list[0])
print(len(total_list[0]))



buying = []
#def max_prft(remn, buying):
maxi = -1* math.inf
for item in total_list[0]:
    if sum(cst[i] for i in item) <= bg:
        maxi = max(maxi, sum([pft[i] for i in item]))
print(maxi)

#print(max_prft(nEp, []))
