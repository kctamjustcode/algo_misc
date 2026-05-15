m = 4
n = 6
#board = [[0 for _ in range(n)] for _ in range(m)]
#print(board_indice)

guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]


def search_guard_view(grds, wals, m, n):
    union_view = []
    for grd in grds:
        horn_viw = []
        for i in range(m):
            if [grd[0]+i, grd[1]] not in wals and grd[0]+i in range(m):
                horn_viw += [[grd[0]+i, grd[1]]]
            else:
                break
        for i in range(m):
            if [grd[0]-i,grd[1]] not in wals and grd[0]-i in range(m):
                horn_viw += [[grd[0]-i, grd[1]]]
            else:
                break
        vert_viw = []
        for j in range(n):
            if [grd[0], grd[1]+j] not in wals and grd[1]+j in range(n):
                vert_viw += [[grd[0], grd[1]+j]]
            else:
                break
        for j in range(n):
            if [grd[0],grd[1]-j] not in wals and grd[1]-j in range(n):
                vert_viw += [[grd[0], grd[1]-j]]
            else:
                break
        union_view += horn_viw+vert_viw
    return union_view

def search_safe_view(grds, wals, m, n):
    guards_view = search_guard_view(grds, wals, m, n)
    board_indice = []
    for i in range(m):
        for j in range(n):
            if [i,j] not in guards_view and [i,j] not in walls:
                board_indice.append([i,j])
    return sorted(board_indice)

#print(sorted(search_guard_view(guards, walls, m, n)))
print(search_safe_view(guards, walls, m, n))

m = 3
n = 3
guards = [[1,1]]
walls = [[0,1],[1,0],[2,1],[1,2]]
print(search_safe_view(guards, walls, m, n))
#print(search_guard_view(guards, walls, m, n))
