import random

num = 5525

def operation_one(num, a):
    str_num = str(num)
    new_num = ""
    for i in range(len(str_num)):
        if i%2 == 1:
            new_segm_digit = str( (int(str_num[i]) + a) % 10 )
            new_num += new_segm_digit
        else:
            new_num += str_num[i]
    return int(new_num)

print(operation_one(3456, 5))


def operation_two(num, b):
    str_num = str(num)
    new_num = str_num[-b:] + str_num[:-b]
    return int(new_num)

print(operation_two(3456, 1))

def monte_carlo_approch(num, a, b):
    possi_seq = []
    for _ in range(len(str(num))):
        cnt_limit = 10*10*len(str(num))
        cnt = 0
        while cnt != cnt_limit:
            dice = random.randint(0, 1)
            if dice == 0:
                num = operation_one(num, a)
            elif dice == 1:
                num = operation_two(num, b)
            possi_seq += [num]
            cnt += 1
    return min(possi_seq)

print(monte_carlo_approch(5525, 9, 2))
print(monte_carlo_approch(74, 5, 1))



def operation_one_str(str_num, a):
    new_num = ""
    for i in range(len(str_num)):
        if i%2 == 1:
            new_segm_digit = str( (int(str_num[i]) + a) % 10 )
            new_num += new_segm_digit
        else:
            new_num += str_num[i]
    return new_num

def operation_two_str(str_num, b):
    new_num = str_num[-b:] + str_num[:-b]
    return new_num


def monte_carlo_approch_str(str_num, a, b):
    possi_seq = []
    opr_num = str_num
    for _ in range(len(str_num)):
        cnt_limit = 10*10*len(str_num)
        cnt = 0
        while cnt != cnt_limit:
            dice = random.randint(0, 1)
            if dice == 0:
                opr_num = operation_one_str(opr_num, a)
            elif dice == 1:
                opr_num = operation_two_str(opr_num, b)
            possi_seq += [int(opr_num)]
            cnt += 1
    return min(possi_seq)

print(monte_carlo_approch_str('0011',4,2))

def padding_zero(num1, num2):
    return 0
