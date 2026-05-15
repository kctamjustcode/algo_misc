import copy

def check_condition(wrd, m, n):
    zero_cnt = 0
    one_cnt = 0
    for ltr in wrd:
        if ltr == '0':
            zero_cnt += 1
        elif ltr == '1':
            one_cnt += 1
    if zero_cnt <= m and one_cnt <= n:
        return True
    else:
        return False


def ones_zeros(wrd, wrd_lst, m, n):
    old_length = wrd_lst
    oz = ['0', '1']
    for dig in oz:
        new_wrd  = wrd + dig
        if check_condition(new_wrd, m, n):
            wrd_lst += [new_wrd]
            ones_zeros(new_wrd, wrd_lst, m, n)
    return wrd_lst

print(ones_zeros("",[],2,2))




    
    