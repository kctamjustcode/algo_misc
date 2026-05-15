import copy

nums = [1, 4, 5, 1]
k_rng = 1
numOpratns = 2

nums = sorted(nums)

def get_max_freq(num):
    freq_dict = {}
    for i in num:
        freq_dict[str(i)] = 0
    for i in num:
        freq_dict[str(i)] += 1
    return max(freq_dict.values())

#print(get_max_freq(nums))

#k = k_rng
def modi_max_freq(num, k, nOp, ud_indc):
    max_freq = get_max_freq(num)
    if nOp == 0:
        return max_freq
    else:
        for i in range(len(num)):
            if i not in ud_indc:
                for j in range(-k, k+1):
                    num_cp = copy.deepcopy(num)
                    nOp_cp = nOp
                    num_cp[i] += j
                    nOp_cp -= 1
                    max_freq = max(max_freq, modi_max_freq(num_cp, k, nOp_cp, ud_indc+[i]))
        return max_freq
    
print(modi_max_freq(nums, k_rng, numOpratns, []))
                
nums = [5,11,20,20]
k_rng = 5
numOpratns = 1

print(modi_max_freq(nums, k_rng, numOpratns, []))
