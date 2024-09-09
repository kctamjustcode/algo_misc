### different sorting codes implementation

def insertionsort(nums):
    arr = nums
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i > -1 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr
    
print(insertionsort([1,5,3,7,9,2,8]))

def insertionsort_rev(nums):
    arr = nums
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i > -1 and arr[i] < key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr
    
print(insertionsort_rev([1,5,3,7,9,2,8]))

def selectionsort(nums):
    if nums == []:
        return nums
    minn = nums[0]
    ind = 0
    for i in range(1,len(nums)):
        if nums[i] < minn:
            minn = nums[i]
            ind = i
    nums[0], nums[ind] = nums[ind], nums[0]
    return [minn] + selectionsort(nums[1:])

print(selectionsort([1,5,3,7,9,2,8]))

def bubblesort(nums):
    for _ in range(len(nums)-1):
        for j in range(1,len(nums)):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums

print(bubblesort([1,5,3,7,9,2,8]))


def mergesort(nums):
    if len(nums) <= 1:
        return nums
    else:
        return merge(mergesort(nums[:len(nums)//2]), mergesort(nums[len(nums)//2:]))

def merge(left,right):
    m, n = len(left), len(right)
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def bfcntinv(left,right):
    array = left+right
    cnt = 0
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                cnt += 1
    return cnt

#print(bfcntinv([],[2,8,99,1,6,25,9,3,255,11,33,7,5,4,101,10]))


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    q, snums = partition(nums)
    return quicksort(snums[:q]) + [snums[q]] + quicksort(snums[q+1:])

def partition(nums):
    if len(nums) == 0:
        return -1, nums
    cpnums = nums
    x = cpnums[-1]
    cpnums = cpnums[:-1]
    i = -1
    for j in range(len(cpnums)):
        if cpnums[j] <= x:
            i += 1
            cpnums[i], cpnums[j] = cpnums[j], cpnums[i]
    cpnums = cpnums[:i+1]+[x]+cpnums[i+1:]
    return i+1, cpnums


def quicksort_first(nums):
    if len(nums) <= 1:
        return nums
    q, snums = partition_first(nums)
    return quicksort_first(snums[:q]) + [snums[q]] + quicksort_first(snums[q+1:])

def partition_first(nums):
    if len(nums) == 0:
        return -1, nums
    cpnums = nums
    x = cpnums[0]
    cpnums = cpnums[1:]
    i = -1
    for j in range(len(cpnums)):
        if cpnums[j] <= x:
            i += 1
            cpnums[i], cpnums[j] = cpnums[j], cpnums[i]
    cpnums = cpnums[:i+1]+[x]+cpnums[i+1:]
    return i+1, cpnums


def quicksort_midd(nums):
    if len(nums) <= 1:
        return nums
    q, snums = partition_midd(nums)
    return quicksort_midd(snums[:q]) + [snums[q]] + quicksort_midd(snums[q+1:])

def partition_midd(nums):
    if len(nums) == 0:
        return -1, nums
    cpnums = nums

    m = len(nums)// 2 - 1 + len(nums)%2
    x = cpnums[m]
    cpnums = cpnums[:m]+cpnums[m+1:]
    i = -1
    for j in range(len(cpnums)):
        if cpnums[j] <= x:
            i += 1
            cpnums[i], cpnums[j] = cpnums[j], cpnums[i]
    cpnums = cpnums[:i+1]+[x]+cpnums[i+1:]
    return i+1, cpnums


def ifmonotonic(nums):
    if nums[0] > nums[1]:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                return False
    else:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
    return True
        
a = [2,1,6,3,5,4]
print(quicksort(a))
print(mergesort(a))
print(quicksort_midd([2,1,6]))
print(quicksort_first([2,3,1,4,5,8,6,7]))
