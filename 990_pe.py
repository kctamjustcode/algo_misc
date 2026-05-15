import math, copy

positive_digits = list(range(1,10))
str_pos_digits = [str(digit) for digit in positive_digits]
digits = list(range(10))
str_digits = [str(digit) for digit in digits]
length = 7

plus_sign = ['+']
equal_sign = ['=']

def check_valid_plus_signs(eq):
    plus_indice = []
    for i in range(len(eq)):
        if eq[i] == '+':
            plus_indice += [i]
    '''
    if eq == '1+1':
        print(plus_indice)
        print(len(eq))
        print(not eq[0] in str_digits)
        print(not eq[2] in str_digits)
    '''
    for index in plus_indice:
        if index == 0 or index == len(eq)-1:
            return False
        if not eq[index-1] in str_digits or not eq[index+1] in str_digits:
            return False
    return True

def check_valid_equal_sign(eq):
    equal_index = []
    for i in range(len(eq)):
        if eq[i] == '+':
            equal_index += [i]
    if len(equal_index) != 1:
        return False
    elif equal_index[0] == 0 or equal_index[0] == len(eq)-1:
        return False
    else:
        return True

def check_leading_zeros(eq):
    total = []
    for item in eq.split('+'):
        total += item.split('=')
    try:
        for item in total:
            if len(str(int(item))) != len(item) or int(item) == 0:
                return True
    except:
        return False
    return False

def check_leading_zeros_item(term):
    #print(term)
    total = term.split('+')
    for item in total:
        try:
            test = int(item)
            if len(str(int(item))) != len(item) or int(item) == 0:
                return True
        except:
            return False
    return False

def invalid_item_double_plus(term):
    for i in range(len(term)-1):
        if term[i] == '+' and term[i] == term[i+1]:
            return True
    return False

lhs_total_digits = [[]]
def generate_lhs_digits_fixed_length(n, item):
    if item == '1+1' or item == '2':
        print('found')
        #return
    if not invalid_item_double_plus(item) and not check_leading_zeros_item(item):
        if len(item) <= n:
            lhs_total_digits[0] += [item]
            for sign in str_digits+plus_sign:
                item_next = copy.deepcopy(item)
                item_next += sign
                #print(item_next)
                if len(item_next) <= n:
                    generate_lhs_digits_fixed_length(n, item_next)

generate_lhs_digits_fixed_length(length-2, "")
#temp_lhs_digits = list(range(10**(length-2)))
#lhs_total_digits[0] += list(range(10**(length-2)))
print(len(lhs_total_digits[0]))
print('assert: ', '1+1' in lhs_total_digits[0] and '2' in lhs_total_digits[0])
print('assert: ', '1+1+1' in lhs_total_digits[0] and '3' in lhs_total_digits[0])

rhs_total_digits = [[]]
def generate_rhs_digits_fixed_length(n, item):
    if len(item) <= n:
        rhs_total_digits[0] += [item]
        for sign in str_digits:
            item_next = copy.deepcopy(item)
            item_next += sign
            #print(item_next)
            if len(item_next) <= n:
                generate_rhs_digits_fixed_length(n, item_next)

#generate_rhs_digits_fixed_length(length-2, "")
#print(rhs_total_digits)

lhs_item_pure_numbers = []
lhs_item_eqs = []

for item in lhs_total_digits[0]:
    try:
        item.index('+')
        if check_valid_plus_signs(item):
            lhs_item_eqs += [item]
    except:
        lhs_item_pure_numbers += [item]

#print(lhs_item_pure_numbers)
#print(lhs_item_eqs)
print('1+1+1' in lhs_item_eqs)

lhs_item_eqs_sum = []
for left_eq in lhs_item_eqs:
    str_lhs = left_eq.split('+')
    lhs_digits = [int(left_digits) for left_digits in str_lhs]
    lhs_sum = sum(lhs_digits)
    lhs_item_eqs_sum += [(left_eq, lhs_sum)]

valid_eqs = []
valid_eqs_cnt = 0
for left_eq_sum in lhs_item_eqs_sum:
    for right_eq_sum in lhs_item_eqs_sum:
        lhs_sum = left_eq_sum[1]
        rhs_sum = right_eq_sum[1]
        if lhs_sum == rhs_sum and len(left_eq_sum[0])+len(right_eq_sum[0])+1 <= length:
            valid_eqs_cnt += 1
        else:
            continue
        
print(len(valid_eqs))
for left_eq in lhs_item_eqs:
    str_lhs = left_eq.split('+')
    lhs_digits = [int(left_digits) for left_digits in str_lhs]
    lhs_sum = sum(lhs_digits)
    lhs_sum_str = str(lhs_sum)
    if left_eq == '1+1':
        print('found', lhs_sum_str)
    left_eq_sum = left_eq + '=' + lhs_sum_str
    if len(left_eq_sum) <= length:
        #valid_eqs += [left_eq_sum]
        valid_eqs_cnt += 1
    right_eq_sum = lhs_sum_str + '=' + left_eq
    if len(right_eq_sum) <= length:
        #valid_eqs += [right_eq_sum]
        valid_eqs_cnt += 1
#print(len(valid_eqs))
for num in lhs_item_pure_numbers:
    if 1 < len(num)*2 + 1 <= length:
        #valid_eqs += [num+'='+num]
        valid_eqs_cnt += 1
        #print(num)

#print(valid_eqs)
#print(len(valid_eqs))

#valid_eqs = list(set(valid_eqs))
print(valid_eqs_cnt)
#print(len(valid_eqs))

'''
if left_item == '1+1' and right_item == '2':
    print('found found found')
    print(not check_valid_plus_signs(left_item))
    print(check_leading_zeros(left_item))
    print(not check_valid_plus_signs(right_item))
    print(check_leading_zeros(right_item))
'''

'''
#brutual_force_approach
valid_eqs = []

for left_item in lhs_total_digits[0]:
    for right_item in lhs_total_digits[0]:
        eq = left_item + '=' + right_item
        #try:
        if len(eq) > length or len(left_item) == 0 or len(right_item) == 0:
            continue
        elif not check_valid_plus_signs(left_item) or not check_valid_plus_signs(right_item):
            continue
        else:
            try:
                str_lhs = left_item.split('+')
                str_rhs = right_item.split('+')
                lhs_digits = [int(left_digits) for left_digits in str_lhs]
                rhs_digits = [int(right_digits) for right_digits in str_rhs]
                if sum(lhs_digits) == sum(rhs_digits):
                    valid_eqs += [eq]
                else:
                    continue
            except:
                print(eq)
        #except:
            #print(eq)
            #continue

#print(valid_eqs)

#valid_eqs = list(set(valid_eqs))
print(valid_eqs)
print(len(valid_eqs))

#valid_eqs = list(set(valid_eqs))
#print(valid_eqs)
#print(len(valid_eqs))
'''
