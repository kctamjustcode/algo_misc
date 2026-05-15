import math, copy


init_toekn = [1 for _ in range(8)]

c = 2
d = 1

def valid_available_opera(row, c, d):
    for i in range(len(row)-2):
        if row[i] != 0 and row[i+2] != 0:
            return True
    return False

def valid_first_opera(row, a, b, c):
    if a >= len(row)-2:
        return False
    else:
        return b == a+c and row[a] != 0 and row[b] != 0
    
def valid_second_opera(row, b, d):
    return b+d < len(row)

def second_opera(row, a, b, d):
    row_return = copy.deepcopy(row)
    z = b + d
    row_return[a] = 0
    row_return[b] = 0
    row_return[z] += (row[a]+row[b])
    return row_return

max_num_token = [-1*math.inf]

def dp_sol(row,c,d):
    print(row)
    if valid_available_opera(row, c, d):
        for a_next in range(len(row)):
            if valid_first_opera(row, a_next, a_next+c, c) and valid_second_opera(row, a_next+c, d):
                dp_sol(second_opera(row,a_next,a_next+c,d), c, d)
    else:
        print(row)
        max_num_token[0] = max(max_num_token[0], max(row))

dp_sol(init_toekn, c, d)

print(max_num_token)

test_row = [1, 1, 1, 1, 0, 1, 0, 3]
print(valid_available_opera(test_row, c, d))
