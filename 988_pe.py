import math, copy

a, b = 3, 5

# co-primes problems to lcm
# spanning problem: find lcm~


a_b_lcm = math.lcm(a, b)
lcm_occps = []

for i in range(b+1):
    for j in range(a+1):
        spanning = a*i+b*j
        if spanning <= a_b_lcm:
            lcm_occps += [spanning]

print(lcm_occps)


testing_spaces = []
for i in range(a_b_lcm+1):
    if i not in lcm_occps:
        testing_spaces += [i]

print(testing_spaces)

### additional validation_test
