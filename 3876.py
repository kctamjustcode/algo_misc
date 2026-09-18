import copy

num1 = [1, 4, 7]

def mono_parity(num):
    return sum([num[i]%2 for i in range(len(num))]) == 0 or sum([num[i]%2 for i in range(len(num))]) == len(num)

def constructing_arrays(num, num1):
    if len(num) == len(num1):
        if mono_parity(num):
            print(num)
            return True
        else:
            return False
    else:
        for i in range(len(num), len(num1)):
            for j in range(2):
                if j == 0:
                    new_num = copy.deepcopy(num)
                    new_num += [num1[i]]
                    if constructing_arrays(new_num, num1):
                        return True
                if j == 1:
                    for u in range(len(num1)):
                        if i == u:
                            continue
                        else:
                            new_num = copy.deepcopy(num)
                            new_num += [num1[i]-num1[u]]
                            if constructing_arrays(new_num, num1):
                                return True
    

print(constructing_arrays([],num1))

num2 = [2, 3]
print(constructing_arrays([],num2))


def second_condition(num1,num2):
    assert len(num1) == len(num2)
    for i in range(len(num1)):
        if num1[i] == num2[i]:
            continue
        else:
            if num1[i] < 1:
                return False
    return True

def constructing_arrays_II(num, num1, times):
    #print(num,times)
    if len(num) == len(num1) and len(num)==times:
        if mono_parity(num) and second_condition(num, num1):
            print(num,times)
            return True
        else:
            return False
    else:
        for i in range(len(num1)):
            for j in range(2):
                if j == 0:
                    new_num = copy.deepcopy(num)
                    print(i)
                    new_num[i] = num1[i]
                    #print(new_num, i, j)
                    if constructing_arrays_II(new_num, num1, times+1):
                        return True
                if j == 1:
                    for u in range(len(num1)):
                        if i == u:
                            continue
                        else:
                            new_num = copy.deepcopy(num)
                            new_num[i] = num1[i]-num1[u]
                            #print(new_num, i, j , u)
                            if constructing_arrays_II(new_num, num1, times+1):
                                return True
        return False

print(constructing_arrays_II(num1,num1,0))

num2 = [2, 3]
print(constructing_arrays_II(num2,num2,0))
