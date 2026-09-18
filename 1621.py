import copy

lines_set = [[]]

def conditioning(lines):
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            case1 = lines[i][0] in range(lines[j][0], lines[j][1]) or lines[i][1] in range(lines[j][0]+1, lines[j][1]+1)
            case2 = lines[j][0] in range(lines[i][0], lines[i][1]) or lines[j][1] in range(lines[i][0]+1, lines[i][1]+1)
            if case1 or case2:
                return False
    return True

def draw_line_segments(n, lines, k):
    if len(lines) == k and conditioning(lines):
        lines_set[0] += [sorted(lines)]
        #lines_set[0] += [lines]
    if len(lines) < k:
        for i in range(len(lines), n-1):
            #if i == n-1
            for j in range(i+1, n):
                new_lines = copy.deepcopy(lines)
                new_lines += [(i, j)]
                if conditioning(new_lines):
                    draw_line_segments(n, new_lines, k)

draw_line_segments(30, [], 7)
print(lines_set[0])

def remove_duplicate(list):
    list_clone = copy.deepcopy(list)
    new_list = []
    for i in range(len(list)):
        cnt_dup = 0
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                cnt_dup += 1
        while cnt_dup > 0:
            list_clone.remove(list[i])
            cnt_dup -= 1
    return list_clone
    #return new_list

print(remove_duplicate([1,1,2,3,3,4,5]))
print(len(remove_duplicate(lines_set[0])))

### or, in reversed manner, remove points or lines from the fundamental line