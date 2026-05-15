import copy

def palind_lngth_three(s):
    palindromic_list = []
    for i in range(len(s)-2):
        for j in range(i+1, len(s)-1):
            for k in range(j+1, len(s)):
                s_sub = s[i]+s[j]+s[k]
                if s_sub == s_sub[::-1] and s_sub not in palindromic_list:
                    palindromic_list += [s_sub]
    return len(palindromic_list)

print(palind_lngth_three('aabca'))
print(palind_lngth_three('bbcbaba'))


s_substring = []

def check_palind(v):
    return v == v[::-1] and len(v) > 1

def palind_lngth(s, lst):
    if s not in lst and check_palind(s):
        lst += [s]
    for i in range(len(s)):
        s_subnw = s[:i] + s[i+1:]
        if s_subnw not in lst and check_palind(s_subnw):
            lst += [s_subnw]
            #lst_cp = copy.deepcopy(lst)
        palind_lngth(s_subnw, lst)

palind_lngth('aabca', s_substring)
print(s_substring)
        
