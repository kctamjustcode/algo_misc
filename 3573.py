import math, copy

prices = [12,16,19,19,8,1,19,13,9]
k = 3

'''
prices = [1,7,9,8,2]
k = 2
'''

normal_trans = []
short_selling_trans = []

for i in range(len(prices)-1):
    for j in range(i+1, len(prices)):
        if prices[j]-prices[i] > 0:
            normal_trans += [(prices[j]-prices[i], i, j, 'n')]
        if prices[j]-prices[i] < 0:
            short_selling_trans += [(prices[i]-prices[j], i, j, 's')]

#normal_trans = sorted(normal_trans, key=lambda x: x[0], reverse=True)
#short_selling_trans = sorted(short_selling_trans, key=lambda x: x[0], reverse=True)
mixed_trans = sorted(normal_trans+short_selling_trans, key=lambda x: x[0], reverse=True)
#print(mixed_trans)

def vaild_member(itm, nwtrm):
    for item in itm:
        if nwtrm[1] in range(item[1], item[2]+1) or nwtrm[2] in range(item[1], item[2]+1) or item[1] in range(nwtrm[1], nwtrm[2]+1) or item[2] in range(nwtrm[1], nwtrm[2]+1):
            return False
    return True

total_list = [[]]
def generate_valid_set_of_trans(trans_lst, lyr, itm):
    if lyr == k:
        total_list[0] += [itm]
    else:
        for i in range(len(trans_lst)):
            trans_lst_cp = copy.deepcopy(trans_lst)
            itm_cp = copy.deepcopy(itm)
            pped = trans_lst_cp.pop(i)
            if vaild_member(itm_cp, pped):
                itm_cp += [pped]
                generate_valid_set_of_trans(trans_lst_cp, lyr+1, itm_cp)

generate_valid_set_of_trans(mixed_trans, 0, [])

def sorting_procedure(ttl_lst):
    ttl_lst_bkup = []
    for itm in ttl_lst:
        sorted_itm = sorted(itm, key=lambda x: x[1])
        if sorted_itm not in ttl_lst_bkup:
            ttl_lst_bkup += [sorted_itm]
    return ttl_lst_bkup

trans_proceeded = sorting_procedure(total_list[0])
#print(trans_proceeded)
#trans_proceeded = list(set(trans_proceeded))
print('length of vaild combinations: ', len(trans_proceeded))

def maxi_profit(ttl_lst):
    maxi = -1 * math.inf
    for itm in ttl_lst:
        maxi = max(maxi, sum([itm[i][0] for i in range(len(itm))]))
    return maxi

maxim = maxi_profit(trans_proceeded)
print('maximum: ', maxim)

for itm in trans_proceeded:
    if sum([itm[i][0] for i in range(len(itm))]) == maxim:
        print(itm)
#print(maxi_profit(total_list[0]))
