nums = [1, -10, 7, 13, 6, 8]
value = 5


def get_min_freq(num):
    num=sorted(num)
    freq_dict = {}
    for i in num:
        freq_dict[str(i)] = 0
    for i in num:
        freq_dict[str(i)] += 1
    min_freq = min(freq_dict.values())
    for i in num:
        #print(i, freq_dict[str(i)], min_freq)
        if freq_dict[str(i)] == min_freq:
            min_elem = i
            break
    return min_freq, min_elem


def MEX(num, val):
    mod_num = [num[i]%val for i in range(len(num))]
    for i in range(1, val):
        if i not in mod_num:
            return i
    min_freq, min_val = get_min_freq(mod_num)
    return min_freq*val+min_val

print(MEX([1, -10, 7, 13, 6, 8], 5))

nums = [1,-10,7,13,6,8]
value = 7

print(MEX(nums, value))

nums = [1, 0, 2, 3, 0, 0, 1]
value = 4
print(MEX(nums, value))
