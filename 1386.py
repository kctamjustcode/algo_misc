import math, copy

n = 3
reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]

reservable = []
cnt = 0
for i in range(n):
    for j in range(10-3):
        blocked = False
        #conten_row = (i+1, j)
        for item in reservedSeats:
            if item[0]-1 == i and item[1]-1 in range(j, j+4):
                blocked = True
                break
        if not blocked:
            #print(i,j)
            reservable += [(i, j)]
            cnt += 1

print(cnt)
print(reservable)
#min_cnt = [math.inf]
max_cnt = [-1*math.inf]

def over_lapping(candidates, reservedSeats_cand):
    for reserved in candidates:
        new_reservedSeats = copy.deepcopy(reservedSeats_cand)
        seat = reserved
        blocked = False
        for i in range(4):
            new_seat = [seat[0]+1, seat[1]+1+i]
            #print(new_seat)
            if new_seat in reservedSeats_cand:
                blocked = True
        if not blocked:
            for i in range(4):
                new_reservedSeats += [[seat[0]+1, seat[1]+1+i]]
        new_candidates = copy.deepcopy(candidates)
        #if not blocked:
        new_candidates.remove(reserved)
        max_cnt[0] = max(max_cnt[0], len(new_reservedSeats))
        over_lapping(new_candidates, new_reservedSeats)

over_lapping(reservable, reservedSeats)
print((max_cnt[0]-len(reservedSeats))//4)