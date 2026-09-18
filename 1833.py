import math, copy

#costs = [1,3,2,4,1]
#coins = 7

costs = [1,6,3,1,2,5]
coins = 20

max_cnt = [0]

def find_max_num_of_ice_creams(cost, bought, coin):
    if sum(bought) <= coin:
        max_cnt[0] = max(max_cnt[0], len(costs)-len(cost))
    for item in cost:
        new_bought = copy.deepcopy(bought)
        new_bought += [item]
        new_cost = copy.deepcopy(cost)
        new_cost.remove(item)
        find_max_num_of_ice_creams(new_cost, new_bought, coin)

find_max_num_of_ice_creams(costs,[],coins)
print(max_cnt[0])
