import math, copy

#s = "adefaddaccc"
s = "abbaccd"

def conditioning(sub_str, s):
    for char in sub_str:
        for check_char in s:
            if char == check_char:
                return False
    return True

condit_substr = [[]]


for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        test_str = s[i: j]
        #print(test_str, s[:i]+s[j:])
        if conditioning(test_str, s[:i]+s[j:]):
            condit_substr[0] += [(test_str, (i, j))]
                     

#find_cond_substr("", s)
print(condit_substr[0])

def overlapping(item1, item2):
    return item1[0] in range(item2[0], item2[1]) or item1[1] in range(item2[0], item2[1])

def mutually_non_overlapping(item_list):
    for item1 in item_list:
        for item2 in item_list:
            if item1 == item2:
                continue
            else:
                if overlapping(item1, item2):
                    return False
    return True

max_cnt = 0
for i in range(len(condit_substr[0])-1):
    non_overlapping_set = [condit_substr[0][i]]
    for j in range(i+1, len(condit_substr[0])):
        non_overlapping = True
        for item in non_overlapping_set:
            if overlapping(item[1], condit_substr[0][j][1]):
                non_overlapping = False
                break
        if non_overlapping:
            non_overlapping_set += [condit_substr[0][j]]
    max_cnt = max(max_cnt, len(non_overlapping_set))

print(max_cnt)



