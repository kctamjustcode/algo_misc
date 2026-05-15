import math, copy

table = []

for i in range(1, 7):
    for j in range(1, 7):
        table += [(i, j)]

#threshold = 4
expected_value = 3.5

for threshold in range(1, 7):
    expected_sum = 0
    for item in table:
        if item[0] >= threshold:
            expected_sum += item[0]
        else:
            expected_sum += item[1]
    print(expected_sum, expected_sum/len(table), threshold)

#for threshold in range(1, 7):
expected_sum = 0
for item in table:
    if abs(item[0]-expected_value) < abs(item[1]-expected_value):
        if item[0] < expected_value:
            expected_sum += item[1]
        else:
            expected_sum += item[0]
    elif abs(item[0]-expected_value) > abs(item[1]-expected_value):     # choose the minimum, i.e. item[1], to be main
        if item[1] < expected_value:
            expected_sum += item[0]
        else:
            expected_sum += item[1]
    else:
        if item[0] < expected_value:
            expected_sum += item[1]
        else:
            expected_sum += item[0]
print(expected_sum, len(table), expected_sum/len(table))#, threshold)

print('----------')

table_second = []
item_integrated = []
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            table_second += [(i,j,k)]

for threshold in range(1, 7):
    expected_sum = 0
    for item in table_second:
        if max(item[0], item[1]) < threshold:
            expected_sum += item[2]
        else:
            expected_sum += max(item[0],item[1])
    print(expected_sum, expected_sum/len(table_second), threshold)


expected_sum = 0
for item in table_second:
    adjusted_value = [abs(item[0]-expected_value), abs(item[1]-expected_value), abs(item[2]-expected_value)]
    #adjusted_value = [item[0],item[1],item[2]]
    if max(adjusted_value) == adjusted_value[0]:
        if max(item[1], item[2]) < expected_value:
            expected_sum += item[0]
        else:
            #expected_sum += min(max(item[1], item[2]),item[0])
            expected_sum += max(item[1], item[2])
    elif max(adjusted_value) == adjusted_value[1]:
        if max(item[0], item[2]) < expected_value:
            expected_sum += item[1]
        else:
            #expected_sum += min(max(item[0], item[2]),item[1])
            expected_sum += max(item[0], item[2])
    elif max(adjusted_value) == adjusted_value[2]:
        if max(item[1], item[0]) < expected_value:
            expected_sum += item[2]
        else:
            #expected_sum += min(max(item[1], item[0]),item[2])
            expected_sum += max(item[1], item[0])
print(expected_sum,len(table_second),expected_sum/len(table_second))


print('----------')

table_third = []
item_integrated = []
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            for l in range(1, 7):
                table_third += [(i,j,k,l)]

for threshold in range(1, 7):
    expected_sum = 0
    for item in table_third:
        if max([item[0], item[1], item[2]]) < threshold:
            expected_sum += item[3]
        else:
            expected_sum += max([item[0], item[1], item[2]])
    print(expected_sum, expected_sum/len(table_third), threshold)
#print(len(table))

expected_value = 3.5
expected_sum = 0
for item in table_third:
    adjusted_value = [abs(item[0]-expected_value), abs(item[1]-expected_value), abs(item[2]-expected_value), abs(item[3]-expected_value)]
    #adjusted_value = [item[0],item[1],item[2]]
    if max(adjusted_value) == adjusted_value[0]:
        if max([item[1], item[2], item[3]]) < expected_value:
            expected_sum += item[0]
        else:
            expected_sum += max([item[1], item[2], item[3]])
    elif max(adjusted_value) == adjusted_value[1]:
        if max([item[0], item[2], item[3]]) < expected_value:
            expected_sum += item[1]
        else:
            expected_sum += max([item[0], item[2], item[3]])
    elif max(adjusted_value) == adjusted_value[2]:
        if max([item[0], item[1], item[3]]) < expected_value:
            expected_sum += item[2]
        else:
            expected_sum += max([item[0], item[1], item[3]])
    elif max(adjusted_value) == adjusted_value[3]:
        if max([item[0], item[1], item[2]]) < expected_value:
            expected_sum += item[3]
        else:
            expected_sum += max([item[0], item[1], item[2]])

print(expected_sum,len(table_third), expected_sum/len(table_third))
