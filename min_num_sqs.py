import math, copy

def min_sqs(n):
    if n == 0 or n == 1 or n == 2:
        return n
    else:
        min_cnt = n
        for i in range(1, int(math.sqrt(n))+1):
            min_cnt = min(min_cnt, 1+min_sqs(n-i**2))
        return min_cnt


print(min_sqs(3))
print(min_sqs(4))

print(min_sqs(6))
print(min_sqs(17))
