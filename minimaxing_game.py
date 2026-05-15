import math, copy, random

n = 8
arr = list(range(n))
random.shuffle(arr)
print(arr)
arr_cp = copy.deepcopy(arr)

count = [0]

def minimax(lst, round, max_sum):
    count[0] += 1
    if len(lst) == 0 and round == 1:
        return max_sum
    elif len(lst) == 1 and round == -1:
        return max_sum+lst[0]
    elif len(lst) == 2 and round == 1:
        return max_sum + max(lst)
    elif len(lst) == 3 and round == -1:
        mini = math.inf
        for i in [0, -1]:
            lst_cp = copy.deepcopy(lst)
            lst_cp.pop(i)
            mini = min(mini,minimax(lst_cp, 1, max_sum))
            #print(mini, i)
        return mini
    elif len(lst) > 3:
        game_range = [0, -1]
        if len(lst) % 2 == 0 and round == 1:
            maxi = max_sum
            for i in game_range:
                lst_cp = copy.deepcopy(lst)
                pop_term = lst_cp.pop(i)
                maxi = max(maxi, minimax(lst_cp, -1, max_sum+pop_term))
            return maxi
        elif len(lst) % 1 == 0 and round == -1:
            mini = math.inf
            for j in game_range:
                lst_cp = copy.deepcopy(lst)
                lst_cp.pop(j)
                mini = min(mini, minimax(lst_cp, 1, max_sum))
            return mini
        
print('v1', minimax(arr, 1, 0))
print(count[0])

def tranpose(i,j, lst):
    a, b = lst[i], lst[j]
    lst[i], lst[j] = b, a
    return

list_sample = list(range(n))
cnt = 0

while arr != list_sample:
    alpha, beta = random.randint(0, n-1), random.randint(0, n-1)
    tranpose(alpha, beta, arr)
    cnt += 1

print('done', arr)
print(cnt)

cnt = [0]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] # Current element to insert
        j = i - 1
        # Shift elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            cnt[0] += 1
        arr[j + 1] = key

insertion_sort(arr_cp)
print(cnt)
