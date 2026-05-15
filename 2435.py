import math

grid = [[5,2,4],[3,0,5],[0,7,2]]

moves = [ (1, 0), (0, 1) ]

def available_move(pos):
    avbl_mv = []
    for move in moves:
        if pos[0]+move[0] in range(len(grid)) and pos[1]+move[1] in range(len(grid[0])):
            avbl_mv += [ (pos[0]+move[0], pos[1]+move[1]) ]
    return avbl_mv

def path_sum(pos, sum):
    max_sum = -1* math.inf
    if pos == (len(grid)-1, len(grid[0])-1):
        if sum % 3 == 0:
            print('counted', sum)
        return sum
    else:
        for mv in available_move(pos):
            sum_cp = sum + grid[mv[0]][mv[1]]
            pos_cp = mv
            max_sum = max(max_sum, path_sum(pos_cp, sum_cp))
        return max_sum
    
print(path_sum((0, 0), grid[0][0]))

grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]]
print(path_sum((0, 0), grid[0][0]))



