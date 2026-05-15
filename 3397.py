import copy

nums = [1, 4, 5, 1]
k_rng = 1
numOpratns = 2

nums = sorted(nums)

def get_distinct_elem(num):
    freq_dict = {}
    disct_num = []
    for i in num:
        freq_dict[str(i)] = 0
    for i in num:
        freq_dict[str(i)] += 1
    for i in num:
        if freq_dict[str(i)] == 1:
            disct_num += [i]
    return disct_num

print(get_distinct_elem(nums))


### brute force approach
def modi_max_disct_elem(num, k, nOp, ud_indc):
    max_disct_freq = len(get_distinct_elem(num))
    if nOp == 0:
        return max_disct_freq
    else:
        for i in range(len(num)):
            if i not in ud_indc:
                for j in range(-k, k+1):
                    num_cp = copy.deepcopy(num)
                    nOp_cp = nOp
                    num_cp[i] += j
                    nOp_cp -= 1
                    max_disct_freq = max(max_disct_freq, modi_max_disct_elem(num_cp, k, nOp_cp, ud_indc+[i]))
        return max_disct_freq
    
#print(modi_max_disct_elem(nums, 2, len(nums), []))


nums = [1,2,2,3,3,4]

def max_disct_freq(num, k):
    srtd_num = sorted(num)
    lwr_lmt = min(srtd_num) - k
    upr_lmt = max(srtd_num) + k
    lmt_rnge = list(range(lwr_lmt, upr_lmt+1))
    usd_lst = []
    for i in range(len(num)):
        for j in range(-k, k+1):
            if srtd_num[i]+j not in usd_lst:
                usd_lst += [srtd_num[i]+j]
                break
    return len(usd_lst)

print(max_disct_freq(nums, 2))


nums = [4,4,4,4]
print(max_disct_freq(nums, 1))
