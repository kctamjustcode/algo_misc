import math, copy

size = 8
board = [[None for _ in range(size)] for _ in range(size)]

def knight_moves(pos):
    directs = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    avalb_mvs = []
    for dir in directs:
        if pos[0]+dir[0] in range(size) and pos[1]+dir[1] in range(size):
            avalb_mvs += [(pos[0]+dir[0], pos[1]+dir[1])]
    return avalb_mvs

def horse_attacks(pos, brd):
    directs = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    barriers_comp = [(-1,0), (0,1), (1,0), (0,-1)]
    barriers = [barriers_comp[i//2] for i in range(8)]
    print(barriers)
    avalb_mvs = []
    for i in range(len(directs)):
        if brd[pos[0]+barriers[i][0]][pos[1]+barriers[i][1]] == None and pos[0]+directs[i][0] in range(size) and pos[1]+directs[i][1] in range(size):
            avalb_mvs += [(pos[0]+directs[i][0], pos[1]+directs[i][1])]
            print(i, pos[0]+barriers[i][0], pos[1]+barriers[i][1], brd[pos[0]+barriers[i][0]][pos[1]+barriers[i][1]])
    return avalb_mvs

#print(board)
board[1][1] = 'H'
#print(board[1][1])
print(horse_attacks((1,0), board))
