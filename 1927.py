import copy

def indentify_question_marks(num_str):
    return [i for i in range(len(num_str)) if num_str[i] == '?']

exmp_str0 = '54??'
print(indentify_question_marks(exmp_str0))
exmp_str1 = '25??'

def sum_of_digits(num_str):
    cnt = 0
    for s in num_str:
        cnt += int(s)
    return cnt

def sum_game(num_str, i):
    #print(num_str)
    if indentify_question_marks(num_str) == []:
        half_len = len(num_str)//2
        if sum_of_digits(num_str[:half_len]) == sum_of_digits(num_str[half_len:]):
            return False
        else:
            return True
    elif len(indentify_question_marks(num_str)) == 1:
        if i%2 == 0:
            return True
        elif i%2 == 1:
            for k in range(10):         # !!! 
                indx = indentify_question_marks(num_str)[0]
                new_num_str = num_str[:indx] + str(k) + num_str[indx+1:]
                assert(indentify_question_marks(new_num_str)==[])
                if not(sum_game(new_num_str, i+1)):
                    return False
            return True
    else:
        if i%2 == 0:
            for ind in indentify_question_marks(num_str):
                for k in range(10):
                    new_num_str = num_str[:ind] + str(k) + num_str[ind+1:]
                    if sum_game(new_num_str, i+1):
                        #print(new_num_str,i+1)
                        return True
            return False
        elif i%2 == 1:
            for ind in indentify_question_marks(num_str):
                for k in range(10):
                    new_num_str = num_str[:ind] + str(k) + num_str[ind+1:]
                    if not(sum_game(new_num_str, i+1)):
                        return False
            return True

    
print(sum_game(exmp_str0, 0))
print(sum_game(exmp_str1, 0))

exmp_str1 = '?3295???'
print(sum_game(exmp_str1, 0))

