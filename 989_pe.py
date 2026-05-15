import math

n = 100000

solution = []
for i in range(n):
    #print(i**2 % n)
    if abs(i**2 % n) == abs((i + 1)%n):
        solution += [i]
        print(i)
print(len(solution))
