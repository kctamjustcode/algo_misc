import copy

power = [1,1,3,4]

max_dmge = [0]

def pwr_in_used_range(pw, usd_pwr):
    return not (pw - 2 not in usd_pwr and pw - 1 not in usd_pwr and pw not in usd_pwr and pw+1 not in usd_pwr and pw+2 not in usd_pwr)

def all_used(pwls, usd_pwr):
    default = True
    for pw in pwls:
        if not pwr_in_used_range(pw, usd_pwr):
            default = False
    return default

def max_damage(pwr, dmg_sum, usd_pwr):
    if pwr == [] or all_used(pwr, usd_pwr):
        return dmg_sum
    else:
        for i in range(len(pwr)):
            if not pwr_in_used_range(pwr[i], usd_pwr):
                pwr_cp = copy.deepcopy(pwr)
                dmg_sum_cp = copy.deepcopy(dmg_sum)
                pwr_term = copy.deepcopy(pwr_cp[i])
                dmg_sum_cp += pwr_term
                pwr_cp.remove(pwr_term)
                usd_pwr_cp = copy.deepcopy(usd_pwr)
                usd_pwr_cp += [pwr_term]
                while pwr_term in pwr_cp:
                    dmg_sum_cp += pwr_term
                    pwr_cp.remove(pwr_term)
                print(pwr_cp, dmg_sum_cp, usd_pwr_cp, max_dmge[0])
                max_dmge[0] = max(max_dmge[0], max_damage(pwr_cp, dmg_sum_cp, usd_pwr_cp))
            else:
                continue
        return max_dmge[0]

max_damage(power, 0, [])
print(max_dmge)
            
        
power = [7,1,6,6]
max_dmge = [0]
max_damage(power, 0, [])
print(max_dmge)