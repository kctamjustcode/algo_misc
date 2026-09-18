import math, copy

n = 5
k = 0
invocations = [[1,2],[0,2],[0,1],[3,4]]

suspicious_methods = [k]

def find_suspicious_methods(invo, sus_mth):
    new_sus_mth = copy.deepcopy(sus_mth)
    for item in invo:
        if item[0] in sus_mth and item[1] not in sus_mth:
            new_sus_mth += [item[1]]
    return new_sus_mth


new_suspicious_methods = find_suspicious_methods(invocations, suspicious_methods)
while suspicious_methods != new_suspicious_methods:
    suspicious_methods = new_suspicious_methods
    new_suspicious_methods = find_suspicious_methods(invocations, suspicious_methods)
    print(suspicious_methods, new_suspicious_methods)


print(suspicious_methods)
print(find_suspicious_methods(invocations, suspicious_methods))

def removable(j, invo, sus_mth):
    for item in invo:
        if item[1] == j and item[0] not in sus_mth:
            return False
    return True

removable_threats = []
for u in suspicious_methods:
    if removable(u, invocations, suspicious_methods):
        removable_threats += [u]

print(removable_threats)

remaining = []
for i in range(n):
    if i not in removable_threats:
        remaining += [i]

print(remaining)
