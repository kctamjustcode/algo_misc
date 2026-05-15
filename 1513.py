def largest_one_substring(num):
    max_cnt = 1
    for i in range(len(num)-1):
        if num[i] == '1':
            cnt = 1
            while num[i+cnt] == '1':
                cnt += 1
                max_cnt = max(max_cnt, cnt)
                if i+cnt == len(num):
                    break
    return max_cnt

print(largest_one_substring('01100111'))

def number_of_substrings_with_ones(num):
    repeated = 0
    max_cnt = largest_one_substring(num)
    for i in range(1, max_cnt+1):
        for k in range(len(num)-i+1):
            if num[k:k+i] == '1'*i:
                repeated += 1
                #print(i)
    return repeated

print(number_of_substrings_with_ones('01100111'))
print(number_of_substrings_with_ones('101'))
print(number_of_substrings_with_ones('111111'))
