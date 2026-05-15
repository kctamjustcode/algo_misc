def k_places_away(num, k):
    for i in range(len(num)-1):
        if num[i] == 1:
            for j in range(i+1, len(num)):
                if num[j] == 1:
                    dist = j-i-1
                    if dist < k:
                        return False
    return True

print(k_places_away([1,0,0,0,1,0,0,1], 2))
print(k_places_away([1,0,0,1,0,1], 2))