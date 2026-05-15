import math, copy

def recurrsion_demo(n):
    if n == 0:
        print(n)
        return True
    else:
        print(n)
        return recurrsion_demo(n-1)
    
recurrsion_demo(10)

### backtracking: typical example - sudoku
def target_sum(arr, curr, target_num):
    if sum(curr) == target_num:
        print(curr)
        return 1
    elif sum(curr) < target_num:
        for elem in arr:
            curr_cp = copy.deepcopy(curr)
            curr_cp += [elem]
            target_sum(arr, curr_cp, target_num)
        return 0
    else:
        return 0

target_sum([1,2,3],[],5)

'''
alternative demo code

# Function to generate all combinations
# of arr that sums to target.
def makeCombination(arr, remSum, cur, res, index):
    if remSum == 0:
        res.append(list(cur))
        return

    # Invalid Case: If remSum is less than 0 or if index >= len(arr)
    if remSum < 0 or index >= len(arr):
        return

    # Add the current element to the combination
    cur.append(arr[index])

    # Recur with the same index
    makeCombination(arr, remSum - arr[index], cur, res, index)

    # Remove the current element from the combination
    cur.pop()
    makeCombination(arr, remSum, cur, res, index + 1)

# Function to find all combinations of elements
# in array arr that sum to target.
def targetSumComb(arr, target):
    
    # List to store combinations
    cur = []

    # List to store valid combinations
    res = []
    makeCombination(arr, target, cur, res, 0)
    
    return res

if __name__ == "__main__":
    arr = [1,2,3]
    target = 5

    res = targetSumComb(arr, target)

    for v in res:
        print(" ".join(map(str, v)))
'''


def sum_string(str_curr, curr_list):
    #print(str_curr)
    if len(str_curr) == 0:
        if len(curr_list) > 2:
            for i in range(len(curr_list)-2):
                if int(curr_list[i]) + int(curr_list[i+1]) != int(curr_list[i+2]):
                    return 0
            print(curr_list)
            return 1
        else:
            return 0
    elif len(str_curr) != 0:
        for j in range(1, len(str_curr)+1):
            new_split = str_curr[:j]
            remain_str = str_curr[j:]
            curr_list_cp = copy.deepcopy(curr_list)
            curr_list_cp += [new_split]
            sum_string(remain_str, curr_list_cp)

sum_string("12243660", [])
sum_string("1111112223",[])




### dynamic programming

### digit dp

dp = [0 for _ in range(10**5)]
a = 5#23
b = 11#24
dp[0] = 0
dp[1] = 1
for i in range(a, b+1):
    sum_digit = 0
    for digit in str(i):
        sum_digit += int(digit)
    dp[i] = dp[i-1] + sum_digit

print(dp[b])


### stair steps
# running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time
# The task is to implement a method to count how many possible ways the child can run up the stairs

def count_step(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return count_step(n-1) + count_step(n-2) + count_step(n-3)
    elif n < 0:
        return 0

print(count_step(4))


### sum of all subarrays
target = 5
sum_all_subarr = [0]
def sum_of_all_subarrays(lst):
    if len(lst) <= target:
        sum_all_subarr[0] += sum(lst)
        for i in range(1, target+1):
            if (len(lst) != 0 and i not in lst) or len(lst) == 0:
                lst_cp = copy.deepcopy(lst)
                lst_cp += [i]
                if sorted(lst_cp) == lst_cp:
                    print(lst_cp)
                    sum_of_all_subarrays(lst_cp)
sum_of_all_subarrays([])
print(sum_all_subarr[0])


### adding complexity analysis
